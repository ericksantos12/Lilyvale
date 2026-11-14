# -*- coding: utf-8 -*-
"""Parser SNBT mínimo para checar a estrutura dos capítulos. Uso: python tools/quest-book/verify.py"""
import glob, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def parse(s):
    i = 0
    def ws():
        nonlocal i
        while i < len(s) and s[i] in ' \t\r\n,': i += 1
    def val():
        nonlocal i
        ws()
        c = s[i]
        if c == '{':
            i += 1; d = {}
            while True:
                ws()
                if s[i] == '}': i += 1; return d
                m = re.compile(r'[A-Za-z0-9_.]+').match(s, i)
                assert m, 'chave inválida em %d: %r' % (i, s[i:i+30])
                k = m.group(0); i = m.end(); ws()
                assert s[i] == ':', 'faltou : em %d' % i
                i += 1
                assert k not in d, 'chave repetida %s' % k
                d[k] = val()
        if c == '[':
            i += 1; l = []
            while True:
                ws()
                if s[i] == ']': i += 1; return l
                l.append(val())
        if c == '"':
            j = i + 1; out = []
            while s[j] != '"':
                if s[j] == chr(92): j += 1
                out.append(s[j]); j += 1
            i = j + 1; return ''.join(out)
        m = re.compile(r'[^\s,\]\}]+').match(s, i)
        i = m.end(); return m.group(0)
    v = val(); ws()
    assert i == len(s), 'lixo após o fim'
    return v

bad = 0; nq = nt = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'config/ftbquests/quests/chapters/*.snbt'))):
    try:
        d = parse(open(f, encoding='utf-8').read())
        assert d['filename'] == os.path.basename(f)[:-5], 'filename diverge'
        for q in d['quests']:
            nq += 1; nt += len(q['tasks'])
            assert q['tasks'], 'quest sem task %s' % q['id']
            for k in ('id', 'x', 'y'): assert k in q, 'falta %s em %s' % (k, q['id'])
            for t in q['tasks']: assert 'type' in t and 'id' in t
    except Exception as e:
        bad += 1; print('FALHA', os.path.basename(f), e)
print('%d quests, %d tasks, %d arquivos com falha' % (nq, nt, bad))
sys.exit(1 if bad else 0)
