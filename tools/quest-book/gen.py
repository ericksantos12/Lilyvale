# -*- coding: utf-8 -*-
"""Gera os capítulos do livro de quests do Lilyvale. Rode da raiz: python tools/quest-book/gen.py"""
import glob
import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
import chapters_a, chapters_b, chapters_c  # noqa: E402

ROOT = core.ROOT
CH = 'config/ftbquests/quests/chapters/'


def jar_tag(pat, path):
    z = zipfile.ZipFile(glob.glob(os.path.join(ROOT, 'mods', pat + '*.jar'))[0])
    return [v if isinstance(v, str) else v['id'] for v in json.loads(z.read(path))['values']]


def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def main():
    reg = core.Registry()
    errors, warns = [], []

    api = 'data/perfectplushieapi/tags/items/'
    village = jar_tag('perfectplushies', api + 'village_plushies.json')
    treasure = jar_tag('perfectplushies', api + 'treasure_plushies.json')
    rare = jar_tag('perfectplushies', api + 'rare_treasure_plushies.json') + jar_tag('perfectplushies', api + 'rare_village_plushies.json')
    village = [p for p in village if p not in rare]

    chapters = chapters_a.build() + chapters_b.build() + chapters_c.build(village, treasure, rare)
    by_code = {c.code: c for c in chapters}

    # ---------------- legado: quests antigas de Create e Immersive Melodies
    # A divisão do Create (EF01–EF03) e a revisão dos instrumentos já estão nos arquivos.
    # Aqui os blocos com IDs legados (fora do prefixo 7A) são relidos e copiados verbatim:
    # edições feitas nesses blocos, no jogo ou à mão, são preservadas.
    def current(fn):
        return core.legacy_blocks(open(os.path.join(ROOT, CH, fn + '.snbt'), encoding='utf-8').read())

    blocks = {}
    for code, fn in (('EF02', 'logistica_em_movimento'), ('EF03', 'estacoes_e_ferrovias'), ('CC03', 'immersive_melodies')):
        head, bl, od = current(fn)
        by_code[code].raw = [bl[i] for i in od if not i.startswith('7A')]
        blocks.update({i: bl[i] for i in od if not i.startswith('7A')})
        if code == 'CC03':
            by_code[code].header = head
    head, bl, od = current('create_mod')
    ef01 = core.Chapter(0x1A, 'EF01', 'create_mod', 'EF', 0, '&b&lOficina de Engenhos', 'create:wrench')
    ef01.raw = [bl[i] for i in od]
    ef01.header = head
    blocks.update(bl)
    mblocks = {}

    chapters.append(ef01)

    # ---------------- resolução de dependências
    legacy_ids = set()
    for f in glob.glob(os.path.join(ROOT, CH, '*.snbt')):
        legacy_ids |= set(re.findall(r'"([0-9A-F]{16})"', open(f, encoding='utf-8').read()))
    legacy_ids |= set(blocks) | set(mblocks)

    def resolve(ch, d, errs, where):
        if re.fullmatch(r'[0-9A-F]{16}', d):
            if d not in legacy_ids:
                errs.append('%s: dependência legada inexistente %s' % (where, d))
            return d
        if '/' in d:
            code, key = d.split('/')
            ch = by_code[code]
        else:
            key = d
        if key not in ch.keys:
            errs.append('%s: dependência inexistente %s' % (where, d))
            return '0' * 16
        return ch.keys[key]

    # ---------------- escrita
    for c in chapters:
        text = core.chapter_snbt(c, reg, errors, resolve, header=getattr(c, 'header', None))
        write(CH + c.filename + '.snbt', text)

    # ---------------- tags de apoio (datapack do KubeJS)
    for name, biomes in chapters_b.RU_FAMILIES.items():
        for b in biomes:
            if 'regions_unexplored:' + b not in reg.biomes:
                errors.append('tag %s: bioma inexistente %s' % (name, b))
        write('kubejs/data/lilyvale/tags/worldgen/biome/%s.json' % name, json.dumps(
            {'replace': False, 'values': [{'id': 'regions_unexplored:' + b, 'required': False} for b in biomes]}, indent=4) + '\n')
    for t in chapters_b.AN_TIERS:
        vals = ['advancednetherite:netherite_%s_%s' % (t, g) for g in chapters_b.AN_GEAR]
        for v in vals:
            if v not in reg.items:
                errors.append('tag gear: item inexistente ' + v)
        write('kubejs/data/lilyvale/tags/items/advanced_netherite_%s_gear.json' % t,
              json.dumps({'replace': False, 'values': vals}, indent=4) + '\n')
    write('kubejs/data/lilyvale/tags/items/endrem_eyes.json',
          json.dumps({'replace': False, 'values': ['endrem:' + e for e in chapters_c.EYES]}, indent=4) + '\n')

    # ---------------- validação estática sobre os arquivos finais
    ids, pos, deps, where_q = {}, {}, {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, CH, '*.snbt'))):
        t = open(f, encoding='utf-8').read()
        name = os.path.basename(f)
        if t.count('{') != t.count('}') or t.count('[') != t.count(']'):
            errors.append('%s: chaves/colchetes desbalanceados' % name)
        for i in re.findall(r'\bid: "([0-9A-F]{16})"', t):
            if i in ids:
                errors.append('ID duplicado %s em %s e %s' % (i, ids[i], name))
            ids[i] = name
        for bad in re.findall(r'\bid: "([^"]{16})"', t):
            if not re.fullmatch(r'[0-9A-F]{16}', bad) or int(bad, 16) > 0x7FFFFFFFFFFFFFFF or int(bad, 16) <= 1:
                errors.append('%s: ID inválido %s' % (name, bad))
        _, bl, od = core.legacy_blocks(t)
        seen = {}
        for q in od:
            b = bl[q]
            x = float(re.search(r'^\t\t\tx: ([-\d.]+)d', b, re.M).group(1))
            y = float(re.search(r'^\t\t\ty: ([-\d.]+)d', b, re.M).group(1))
            if (x, y) in seen:
                errors.append('%s: posição repetida %s (%s e %s)' % (name, (x, y), seen[(x, y)], q))
            seen[(x, y)] = q
            pos[q] = (name, x, y)
            m = re.search(r'^\t\t\tdependencies: \[(.*?)\]', b, re.M | re.S)
            deps[q] = re.findall(r'"([0-9A-F]{16})"', m.group(1)) if m else []
            where_q[q] = name
    for q, ds in deps.items():
        for d in ds:
            if d not in pos:
                errors.append('%s: %s depende de quest inexistente %s' % (where_q[q], q, d))
            elif pos[d][0] == pos[q][0] and pos[d][1] != pos[q][1] and pos[d][2] != pos[q][2]:
                warns.append('%s: linha diagonal %s -> %s' % (where_q[q], d, q))
    state = {}

    def visit(q):
        if state.get(q) == 1:
            errors.append('ciclo de dependências em ' + q)
            return
        if state.get(q) == 2:
            return
        state[q] = 1
        for d in deps.get(q, []):
            if d in deps:
                visit(d)
        state[q] = 2
    for q in deps:
        visit(q)

    # ---------------- índice gerado
    rows = []
    total = 0
    for f in sorted(glob.glob(os.path.join(ROOT, CH, '*.snbt'))):
        t = open(f, encoding='utf-8').read()
        n = len(core.legacy_blocks(t)[2])
        total += n
        title = re.sub(r'&.', '', re.search(r'\n\ttitle: "(.*)"\n\}', t).group(1))
        group = re.search(r'\n\tgroup: "(.*)"', t).group(1)
        rows.append((group, int(re.search(r'order_index: (-?\d+)', t).group(1)), title, os.path.basename(f), n,
                     t.count('subtitle: "&bA'), t.count('subtitle: "&6M'), t.count('subtitle: "&dC')))
    gorder = list(core.GROUPS.values())
    rows.sort(key=lambda r: (gorder.index(r[0]), r[1]))
    print('| Capítulo | Arquivo | Quests | A | M | C |')
    for r in rows:
        print('| %s | %s | %d | %d | %d | %d |' % r[2:])
    print('TOTAL', total, 'quests em', len(rows), 'capítulos')
    for w in warns:
        print('AVISO', w)
    for e in errors:
        print('ERRO', e)
    print('%d erros, %d avisos' % (len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
