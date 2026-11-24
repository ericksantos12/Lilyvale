# -*- coding: utf-8 -*-
"""Plantas de casco do aleki's Nifty Ships para o capítulo Estaleiro.

Rode da raiz: python tools/quest-book/ship_diagrams.py
Gera PNGs em kubejs/assets/lilyvale/textures/quests/estaleiro/.

Cada célula é uma armação vista de cima, com a proa no alto da imagem:
  ^ > v <  armação inclinada; a seta é para onde você olha ao colocá-la
           (a borda alta fica do lado de fora do casco)
  #        armação plana
  .        vazio
Marcadores: F = forqueta em cima da armação, C = cunho em cima da armação
(desenhados na margem, ao lado da armação, com o ícone do item).
Layouts conferidos contra ShipbuildingMultiblocks e as estruturas
unfinished_rowboat_oak / unfinished_sloop_oak do mod 1.0.14.
"""
import glob
import os
import zipfile

from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'estaleiro')

ROWBOAT = [
    '^^',
    '<>',
    'vv',
]
ROWBOAT_MARKS = {(1, 0): 'F', (1, 1): 'F'}

SLOOP = [
    '.^^.',
    '.<>.',
    '^<>^',
    '<##>',
    '<##>',
    '<##>',
    'vvvv',
]
SLOOP_MARKS = {(2, 0): 'C', (2, 3): 'C', (6, 0): 'C', (6, 3): 'C'}

CELL = 20           # pixels de arte por célula
SCALE = 5           # ampliação nearest-neighbour
PAD = 1             # células de margem

# paleta (madeira de carvalho + painel escuro)
PANEL = (24, 20, 16, 230)
GRID = (60, 52, 44, 255)
WOOD_LOW = (92, 62, 34, 255)
WOOD_HIGH = (176, 128, 74, 255)
FLAT_A = (184, 148, 96, 255)
FLAT_B = (160, 126, 80, 255)
ARROW = (250, 244, 228, 255)
ARROW_SHADOW = (40, 26, 14, 255)
TEXT = (232, 214, 170, 255)

# fonte 3x5 só com as letras usadas
FONT = {
    'P': ['111', '101', '111', '100', '100'],
    'R': ['110', '101', '110', '101', '101'],
    'O': ['111', '101', '101', '101', '111'],
    'A': ['010', '101', '111', '101', '101'],
}


def mod_texture(name):
    jar = glob.glob(os.path.join(ROOT, 'mods', 'alekiNiftyShips-*.jar'))[0]
    with zipfile.ZipFile(jar) as z, z.open('assets/alekiships/textures/item/%s.png' % name) as f:
        return Image.open(f).convert('RGBA').copy()


def arrow_pixels():
    """Seta apontando para cima, centrada na célula."""
    px = set()
    mid = CELL // 2
    for y in range(5, CELL - 5):    # haste
        for x in (mid - 1, mid):
            px.add((x, y))
    for i in range(5):              # ponta
        y = 5 + i
        for x in range(mid - 1 - i, mid + 1 + i):
            px.add((x, y))
    return px


ROT = {'^': 0, '>': 1, 'v': 2, '<': 3}


def rotate(p, turns):
    x, y = p
    for _ in range(turns):
        x, y = CELL - 1 - y, x
    return x, y


def draw_slope(img, ox, oy, d):
    turns = ROT[d]
    # rampa: escuro no lado de dentro, claro no lado alto (para onde a seta aponta)
    for y in range(CELL):
        t = 1 - y / (CELL - 1)
        c = tuple(int(WOOD_LOW[i] + (WOOD_HIGH[i] - WOOD_LOW[i]) * t) for i in range(3)) + (255,)
        for x in range(CELL):
            img.putpixel((ox + rotate((x, y), turns)[0], oy + rotate((x, y), turns)[1]), c)
    pts = arrow_pixels()
    # contorno escuro de 1 pixel em volta da seta
    for p in pts:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (p[0] + dx, p[1] + dy)
            if q not in pts:
                x, y = rotate(q, turns)
                img.putpixel((ox + x, oy + y), ARROW_SHADOW)
    for p in pts:
        x, y = rotate(p, turns)
        img.putpixel((ox + x, oy + y), ARROW)


def draw_flat(img, ox, oy):
    for y in range(CELL):
        for x in range(CELL):
            band = (y // 4) % 2
            c = FLAT_A if band == 0 else FLAT_B
            if y % 4 == 3:
                c = WOOD_LOW
            img.putpixel((ox + x, oy + y), c)


def draw_text(d, x, y, word):
    for ch in word:
        for r, row in enumerate(FONT[ch]):
            for c, bit in enumerate(row):
                if bit == '1':
                    d.point((x + c, y + r), fill=TEXT)
        x += 4


def render(layout, marks, filename):
    rows, cols = len(layout), len(layout[0])
    w, h = (cols + 2 * PAD) * CELL, (rows + 2 * PAD) * CELL
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, h - 1], fill=PANEL)
    tex = {'F': mod_texture('oarlock'), 'C': mod_texture('cleat')}
    for r, line in enumerate(layout):
        for c, ch in enumerate(line):
            ox, oy = (c + PAD) * CELL, (r + PAD) * CELL
            if ch in ROT:
                draw_slope(img, ox, oy, ch)
            elif ch == '#':
                draw_flat(img, ox, oy)
            else:
                d.rectangle([ox + 3, oy + 3, ox + CELL - 4, oy + CELL - 4], outline=GRID)
                continue
            d.rectangle([ox, oy, ox + CELL - 1, oy + CELL - 1], outline=GRID)
    for (r, c), m in marks.items():
        # selo na margem, ao lado da armação marcada, ligado a ela por um traço
        cy = (r + PAD) * CELL + CELL // 2
        left = c < cols / 2
        edge = (c + PAD) * CELL if left else (c + PAD + 1) * CELL - 1
        ox = edge - 14 if left else edge + 4
        d.line([(edge - 4, cy) if left else (edge + 1, cy), (edge - 1, cy) if left else (edge + 4, cy)], fill=TEXT)
        d.rectangle([ox, cy - 5, ox + 10, cy + 5], fill=PANEL[:3] + (255,), outline=TEXT)
        img.alpha_composite(tex[m].resize((9, 9), Image.NEAREST), (ox + 1, cy - 4))
    # proa em cima, popa embaixo
    draw_text(d, w // 2 - 7, (CELL - 5) // 2, 'PROA')
    draw_text(d, w // 2 - 7, h - CELL + (CELL - 5) // 2, 'POPA')
    img = img.resize((w * SCALE, h * SCALE), Image.NEAREST)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, filename)
    img.save(path, optimize=True)
    return path, (w, h)


def main():
    for layout, marks, name in ((ROWBOAT, ROWBOAT_MARKS, 'barco_a_remo.png'), (SLOOP, SLOOP_MARKS, 'sloop.png')):
        path, size = render(layout, marks, name)
        print(os.path.relpath(path, ROOT), 'arte %dx%d' % size)


if __name__ == '__main__':
    main()
