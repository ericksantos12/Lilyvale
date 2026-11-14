# -*- coding: utf-8 -*-
"""Núcleo do gerador do livro de quests do Lilyvale (FTB Quests 2001.4.22, MC 1.20.1).

Uso: python tools/quest-book/gen.py   (a partir da raiz da instância)
Não faz commits. Blocos legados (IDs fora de 7A) são relidos dos arquivos atuais e copiados verbatim.
"""
import glob
import json
import os
import re
import subprocess
import zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CH_DIR = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters')
MC_JAR = os.path.join(ROOT, '..', '..', '..', 'libraries', 'com', 'mojang', 'minecraft', '1.20.1',
                      'minecraft-1.20.1-client.jar')

GROUPS = {
    'PD': '048ED71F33A9801E', 'VC': '2F3E0F43CC0404AB', 'EF': '6F00000000000001',
    'MF': '2E622CDAB0B6B1F2', 'AH': '6E00000000000001', 'FL': '6E00000000000002',
    'CC': '4DFBF6E45E6929B8', 'LR': '1DA3993DEE28D0C0', 'JE': '6E00000000000003',
}
SUB = {'A': '&bA — Aprendizado', 'M': '&6M — Marco', 'C': '&dC — Opcional'}
SHAPE = {'A': 'circle', 'M': 'hexagon', 'C': 'square'}
SIZE = {'A': '1.0d', 'M': '1.25d', 'C': '1.0d'}
XP = {'A': 50, 'M': 150, 'C': 25}


# ---------------------------------------------------------------- registro
class Registry:
    def __init__(self):
        self.items, self.advs, self.ents = set(), set(), set()
        self.biomes, self.structs, self.dims = set(), set(), set()
        jars = glob.glob(os.path.join(ROOT, 'mods', '*.jar')) + [MC_JAR]
        for jar in jars:
            try:
                z = zipfile.ZipFile(jar)
            except Exception:
                continue
            for n in z.namelist():
                m = re.match(r'assets/([^/]+)/models/item/([^/]+)\.json$', n)
                if m:
                    self.items.add(m.group(1) + ':' + m.group(2))
                    continue
                m = re.match(r'data/([^/]+)/advancements/(.+)\.json$', n)
                if m:
                    self.advs.add(m.group(1) + ':' + m.group(2))
                    continue
                m = re.match(r'data/([^/]+)/worldgen/biome/(.+)\.json$', n)
                if m:
                    self.biomes.add(m.group(1) + ':' + m.group(2))
                    continue
                m = re.match(r'data/([^/]+)/worldgen/structure/(.+)\.json$', n)
                if m:
                    self.structs.add(m.group(1) + ':' + m.group(2))
                    continue
                m = re.match(r'data/([^/]+)/dimension/(.+)\.json$', n)
                if m:
                    self.dims.add(m.group(1) + ':' + m.group(2))
                    continue
                m = re.match(r'assets/([^/]+)/lang/en_us\.json$', n)
                if m:
                    try:
                        d = json.loads(z.read(n).decode('utf-8-sig'), strict=False)
                    except Exception:
                        continue
                    for k in d:
                        p = k.split('.')
                        if len(p) == 3 and p[0] == 'entity':
                            self.ents.add(p[1] + ':' + p[2])
        self.dims |= {'minecraft:the_end', 'minecraft:the_nether', 'minecraft:overworld'}


# ---------------------------------------------------------------- modelo
def esc(s):
    # FTB Quests rejeita "& " literal: o & precisa de barra invertida antes do espaço
    s = s.replace('& ', chr(92) + '& ')
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


class Chapter:
    def __init__(self, cc, code, filename, group, order, title, icon):
        self.cc, self.code, self.filename = cc, code, filename
        self.group, self.order, self.title, self.icon = GROUPS[group], order, title, icon
        self.id = '7A%02X0%011X' % (cc, 1)
        self.quests = []        # dicts novos
        self.raw = []           # blocos legados (texto SNBT verbatim)
        self.keys = {}
        self.n = {'q': 0, 't': 0, 'r': 0}

    def _id(self, kind):
        self.n[kind] += 1
        return '7A%02X%s%011X' % (self.cc, {'q': '1', 't': '2', 'r': '3'}[kind], self.n[kind])

    def q(self, key, kind, title, icon, x, y, tasks, desc, deps=(), req=None, sub=None, xp=None,
          optional=None):
        """x, y em unidades de grade (1 unidade = 2.0 no FTB Quests)."""
        qid = self._id('q')
        assert key not in self.keys, key
        self.keys[key] = qid
        self.quests.append(dict(key=key, kind=kind, title=title, icon=icon, x=x * 2.0, y=y * 2.0,
                                tasks=tasks, desc=desc if isinstance(desc, list) else [desc],
                                deps=list(deps), req=req, sub=sub, id=qid,
                                xp=XP[kind] if xp is None else xp,
                                optional=(kind == 'C') if optional is None else optional))
        return qid

    def gallery(self, prefix, items, ox, oy, desc, cols=6, kind='C'):
        """Álbum: uma folha independente por identidade, sem setas."""
        for n, it in enumerate(items):
            spec, icon = (it, None) if isinstance(it, str) else it
            if icon is None:
                icon = spec.split('|')[0].split('*')[0]
            self.q('%s%02d' % (prefix, n + 1), kind, None, icon, ox + (n % cols), oy + n // cols, [spec], desc)


# ---------------------------------------------------------------- SNBT
def task_snbt(ch, spec, reg, errors, where):
    title = None
    if '|' in spec:
        spec, title = spec.split('|', 1)
    tid = ch._id('t')
    L = []

    def emit(pairs):
        for k, v in sorted(pairs.items()):
            L.append('\t\t\t\t%s: %s' % (k, v))

    kind = spec.split(':', 1)[0]
    if kind == 'adv':
        a = spec[4:]
        if a not in reg.advs:
            errors.append('%s: avanço inexistente %s' % (where, a))
        p = {'advancement': esc(a), 'criterion': '""', 'id': esc(tid), 'type': '"advancement"'}
    elif kind == 'dim':
        d = spec[4:]
        if d not in reg.dims:
            errors.append('%s: dimensão inexistente %s' % (where, d))
        p = {'dimension': esc(d), 'id': esc(tid), 'type': '"dimension"'}
    elif kind == 'biome':
        b = spec[6:]
        if not b.startswith('#') and b not in reg.biomes:
            errors.append('%s: bioma inexistente %s' % (where, b))
        p = {'biome': esc(b), 'id': esc(tid), 'type': '"biome"'}
    elif kind == 'struct':
        s = spec[7:]
        if s not in reg.structs:
            errors.append('%s: estrutura inexistente %s' % (where, s))
        p = {'structure': esc(s), 'id': esc(tid), 'type': '"structure"'}
    elif kind == 'ent':
        e = spec[4:]
        if e not in reg.ents:
            errors.append('%s: entidade inexistente %s' % (where, e))
        p = {'id': esc(tid), 'observe_type': '5', 'timer': '0L', 'to_observe': esc(e), 'type': '"observation"'}
    elif kind == 'check':
        p = {'id': esc(tid), 'type': '"checkmark"'}
    elif kind == 'tag':
        t = spec[4:]
        p = {'consume_items': 'false', 'id': esc(tid), 'type': '"item"',
             'item': '{\n\t\t\t\t\tCount: 1\n\t\t\t\t\tid: "itemfilters:tag"\n\t\t\t\t\ttag: {\n\t\t\t\t\t\tvalue: %s\n\t\t\t\t\t}\n\t\t\t\t}' % esc(t)}
    else:
        count = None
        if '*' in spec:
            spec, c = spec.split('*')
            count = int(c)
        if spec not in reg.items:
            errors.append('%s: item inexistente %s' % (where, spec))
        p = {'consume_items': 'false', 'id': esc(tid), 'item': esc(spec), 'match_nbt': 'false', 'type': '"item"'}
        if count:
            p['count'] = '%dL' % count
    if title:
        p['title'] = esc(title)
    emit(p)
    return '{\n' + '\n'.join(L) + '\n\t\t\t}'


def quest_snbt(ch, q, reg, errors, resolve):
    where = '%s/%s' % (ch.code, q['key'])
    L = []
    deps = [resolve(ch, d, errors, where) for d in q['deps']]
    if deps:
        L.append(('dependencies', '[' + ', '.join(esc(d) for d in deps) + ']'))
    if q['req']:
        L.append(('dependency_requirement', esc(q['req'])))
    L.append(('description', '[\n' + '\n'.join('\t\t\t\t' + esc(d) for d in q['desc']) + '\n\t\t\t]'))
    L.append(('hide_details_until_startable', 'false'))
    L.append(('hide_text_until_complete', 'false'))
    if q['icon']:
        if q['icon'] not in reg.items:
            errors.append('%s: ícone inexistente %s' % (where, q['icon']))
        L.append(('icon', esc(q['icon'])))
    L.append(('id', esc(q['id'])))
    if q['optional']:
        L.append(('optional', 'true'))
    if q['xp']:
        L.append(('rewards', '[{\n\t\t\t\tid: %s\n\t\t\t\ttype: "xp"\n\t\t\t\txp: %d\n\t\t\t}]' % (esc(ch._id('r')), q['xp'])))
    else:
        L.append(('rewards', '[ ]'))
    L.append(('shape', esc(SHAPE[q['kind']])))
    L.append(('size', SIZE[q['kind']]))
    L.append(('subtitle', esc(q['sub'] or SUB[q['kind']])))
    tasks = [task_snbt(ch, t, reg, errors, where) for t in q['tasks']]
    L.append(('tasks', '[' + '\n\t\t\t'.join(tasks) + ']' if len(tasks) == 1 else '[\n\t\t\t' + '\n\t\t\t'.join(tasks) + '\n\t\t\t]'))
    if q['title']:
        L.append(('title', esc(q['title'])))
    L.append(('x', '%.1fd' % q['x']))
    L.append(('y', '%.1fd' % q['y']))
    return '\t\t{\n' + '\n'.join('\t\t\t%s: %s' % kv for kv in L) + '\n\t\t}'


def chapter_snbt(ch, reg, errors, resolve, header=None):
    blocks = list(ch.raw) + [quest_snbt(ch, q, reg, errors, resolve) for q in ch.quests]
    if header is None:
        if ch.icon not in reg.items:
            errors.append('%s: ícone de capítulo inexistente %s' % (ch.code, ch.icon))
        header = ('{\n\tdefault_hide_dependency_lines: false\n\tdefault_quest_shape: "circle"\n'
                  '\tfilename: %s\n\tgroup: %s\n\ticon: %s\n\tid: %s\n\torder_index: %d\n\tquest_links: [ ]\n'
                  % (esc(ch.filename), esc(ch.group), esc(ch.icon), esc(ch.id), ch.order))
    return header + '\tquests: [\n' + '\n'.join(blocks) + '\n\t]\n\ttitle: %s\n}\n' % esc(ch.title)


# ---------------------------------------------------------------- legado
def git_head(path):
    return subprocess.run(['git', 'show', 'HEAD:' + path], cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8')


def legacy_blocks(text):
    """Devolve (cabeçalho, {id: bloco verbatim}, ordem)."""
    i = text.index('\tquests: [')
    head = text[:i]
    blocks, order = {}, []
    for m in re.finditer(r'\t\t\{\n.*?\n\t\t\}', text[i:], re.S):
        b = m.group(0)
        qid = re.search(r'^\t\t\tid: "([0-9A-F]{16})"', b, re.M).group(1)
        blocks[qid] = b
        order.append(qid)
    return head, blocks, order


def move(block, x, y):
    block = re.sub(r'^(\t\t\tx: ).*$', r'\g<1>%.1fd' % x, block, flags=re.M)
    return re.sub(r'^(\t\t\ty: ).*$', r'\g<1>%.1fd' % y, block, flags=re.M)


def set_field(block, key, value):
    """Insere ou troca um campo de primeiro nível do bloco (linha única)."""
    pat = r'^\t\t\t%s: .*$' % key
    line = '\t\t\t%s: %s' % (key, value)
    if re.search(pat, block, re.M):
        return re.sub(pat, lambda m: line, block, count=1, flags=re.M)
    return block.replace('\t\t{\n', '\t\t{\n' + line + '\n', 1)
