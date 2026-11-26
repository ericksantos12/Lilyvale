# -*- coding: utf-8 -*-
"""Decoração do capítulo Estaleiro (MF04): título, flâmulas, rosa dos ventos e uma marinha.

Rode da raiz: python tools/quest-book/estaleiro_art.py   (depois: gen.py --only MF04)
Gera PNGs em kubejs/assets/lilyvale/textures/quests/estaleiro/, ao lado das plantas de
ship_diagrams.py. Tudo é pixel art 2D desenhada aqui em resolução nativa e ampliada sem
suavização; o texto usa a fonte bitmap do Minecraft (tide_art.McFont).
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
from tide_art import McFont, gradient_text  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'estaleiro')

MARINHO = (0x12, 0x22, 0x3A)
LATAO = (0xE8, 0xC0, 0x6A)
CORDA = ((0xD8, 0xB8, 0x80), (0x9A, 0x74, 0x44))
VELA = (0xF4, 0xEE, 0xDC)

ANCORA = [
    '...###...',
    '...#.#...',
    '...###...',
    '#######..',
    '....#....',
    '....#....',
    '....#....',
    '#...#...#',
    '##..#..##',
    '.#######.',
    '..#####..',
]

# (arquivo, texto, cor da flâmula)
FLAMULAS = [
    ('flamula_remo', 'Barco a remo', (0xC8, 0x3C, 0x32)),
    ('flamula_sloop', 'Sloop', (0x2E, 0x7C, 0xC8)),
    ('flamula_bordo', 'Vida a bordo', (0xE0, 0xA8, 0x30)),
]


def up(img, k):
    return img.resize((img.width * k, img.height * k), Image.NEAREST)


def stamp(d, pat, x, y, col, mirror=False):
    for r, row in enumerate(pat):
        for c, ch in enumerate(row[::-1] if mirror else row):
            if ch == '#':
                d.point((x + c, y + r), fill=col)


def corda(d, x0, x1, y):
    """Corda torcida de 3 px de altura: listras diagonais em dois tons."""
    for x in range(x0, x1):
        for dy in range(3):
            d.point((x, y + dy), fill=CORDA[(x + dy) // 2 % 2] + (255,))
        d.point((x, y + 3), fill=(0x4A, 0x34, 0x1C, 255))


def titulo(font):
    text = gradient_text(font, 'Estaleiro', VELA, (0xC8, 0x92, 0x4E), 7, outline=MARINHO)
    sub = gradient_text(font, 'Do andaime ao alto-mar', (0xB8, 0xEC, 0xFF), (0x3C, 0x9C, 0xD8), 3, outline=MARINHO)
    # faixa nativa (escala 3) com âncoras nas pontas e corda no meio
    k = 3
    w = (max(text.width, sub.width) + 60) // k
    faixa = Image.new('RGBA', (w, 13), (0, 0, 0, 0))
    d = ImageDraw.Draw(faixa)
    corda(d, 11, w - 11, 5)
    for x, m in ((0, False), (w - 9, True)):
        stamp(d, ANCORA, x + 1, 1, MARINHO + (255,), m)
        stamp(d, ANCORA, x, 0, LATAO + (255,), m)
    faixa = up(faixa, k)
    W = faixa.width
    img = Image.new('RGBA', (W, text.height + faixa.height + sub.height + 8), (0, 0, 0, 0))
    img.alpha_composite(text, ((W - text.width) // 2, 0))
    img.alpha_composite(faixa, (0, text.height - 4))
    img.alpha_composite(sub, ((W - sub.width) // 2, text.height + faixa.height + 4))
    return img


def flamula(font, texto, cor):
    """Mastro com flâmula triangular e o nome da fileira ao lado."""
    t = gradient_text(font, texto, VELA, (0xC8, 0xD8, 0xE8), 4, outline=MARINHO)
    f = Image.new('RGBA', (16, 18), (0, 0, 0, 0))
    d = ImageDraw.Draw(f)
    d.rectangle((1, 0, 2, 17), fill=(0x6A, 0x48, 0x28, 255))
    d.point((1, 0), fill=LATAO + (255,))
    d.point((2, 0), fill=LATAO + (255,))
    escuro = tuple(int(c * 0.6) for c in cor) + (255,)
    for i in range(12):
        h = max(1, round(5 * (1 - i / 12)))
        y0 = 1 + round(i * 0.25)
        d.line((3 + i, 1 + 5 - h + y0 - 1, 3 + i, 1 + 5 + h + y0 - 1), fill=cor + (255,))
        d.point((3 + i, 1 + 5 + h + y0 - 1), fill=escuro)
    f = up(f, 4)
    img = Image.new('RGBA', (f.width + 8 + t.width, max(f.height, t.height)), (0, 0, 0, 0))
    img.alpha_composite(f, (0, 0))
    img.alpha_composite(t, (f.width + 8, (f.height - t.height) // 2 + 4))
    return img


def rosa(font):
    """Rosa dos ventos de 8 pontas com anel de latão e N no alto."""
    n = 49
    img = Image.new('RGBA', (n, n + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = (24, 30)
    d.ellipse((c[0] - 18, c[1] - 18, c[0] + 18, c[1] + 18), outline=MARINHO + (255,), width=3)
    d.ellipse((c[0] - 17, c[1] - 17, c[0] + 17, c[1] + 17), outline=LATAO + (255,), width=1)
    for a in range(0, 360, 30):
        x = c[0] + round(15 * math.sin(math.radians(a)))
        y = c[1] - round(15 * math.cos(math.radians(a)))
        d.point((x, y), fill=LATAO + (255,))

    def ponta(ang, comp, larg, claro, escuro):
        a = math.radians(ang)
        tip = (c[0] + comp * math.sin(a), c[1] - comp * math.cos(a))
        esq = (c[0] + larg * math.sin(a - math.pi / 2), c[1] - larg * math.cos(a - math.pi / 2))
        r = (c[0] + larg * math.sin(a + math.pi / 2), c[1] - larg * math.cos(a + math.pi / 2))
        d.polygon([c, esq, tip], fill=claro + (255,))
        d.polygon([c, tip, r], fill=escuro + (255,))

    for ang in (45, 135, 225, 315):
        ponta(ang, 13, 3, (0x9C, 0xC4, 0xE0), (0x3C, 0x6C, 0x9C))
    for ang in (0, 90, 180, 270):
        claro, escuro = ((0xF0, 0x5A, 0x48), (0xA8, 0x28, 0x22)) if ang == 0 else (VELA, (0xB8, 0xA8, 0x88))
        ponta(ang, 22, 4, claro, escuro)
    d.rectangle((c[0] - 1, c[1] - 1, c[0], c[1]), fill=LATAO + (255,))
    letra = font.mask('N')
    lw = font.glyphs['N'][1]
    for y in range(letra.height):
        for x in range(lw):
            if letra.getpixel((x, y)):
                d.point((c[0] - lw // 2 + x, y - 1), fill=LATAO + (255,))
    # contorno escuro de 1 px para destacar do fundo do livro
    a = img.getchannel('A')
    base = Image.new('RGBA', img.size, MARINHO + (0,))
    base.putalpha(a.filter(ImageFilter.MaxFilter(3)))
    return up(Image.alpha_composite(base, img), 6)


def marinha():
    """Faixa de mar: farol no rochedo, ondas, um sloop de vela cheia e gaivotas."""
    w, h = 180, 46
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    mar = [(0x2E, 0x7C, 0xC8), (0x22, 0x5E, 0xA8), (0x1A, 0x46, 0x84), (0x14, 0x30, 0x5C)]
    topo = 32
    for x in range(w):
        crista = topo + round(1.5 * math.sin(x / 6.0))
        for y in range(crista, h):
            banda = min(3, (y - crista) // 4)
            d.point((x, y), fill=mar[banda] + (255,))
        d.point((x, crista), fill=(0xC8, 0xEC, 0xFF, 255))
        if x % 12 in (3, 4):
            d.point((x, crista + 6), fill=(0x6C, 0xB4, 0xE8, 255))
    # rochedo e farol à esquerda
    d.polygon([(2, h), (6, 30), (14, 26), (24, 29), (30, h)], fill=(0x5A, 0x58, 0x62, 255))
    d.line((7, 30, 13, 27), fill=(0x8A, 0x88, 0x92, 255))
    for i, y in enumerate(range(10, 27, 3)):
        d.rectangle((12 - (y - 10) // 8, y, 18 + (y - 10) // 8, y + 2), fill=(0xD8, 0x3A, 0x32, 255) if i % 2 else VELA + (255,))
    d.rectangle((11, 7, 19, 9), fill=MARINHO + (255,))
    d.rectangle((12, 3, 18, 6), fill=(0xFF, 0xE0, 0x6A, 255))
    d.rectangle((14, 0, 16, 2), fill=MARINHO + (255,))
    # facho de luz: cone que abre e esmaece para a direita
    for x in range(19, 46):
        k = (x - 19) / 27
        meia = 0.5 + 5 * k
        for y in range(round(4.5 - meia), round(4.5 + meia) + 1):
            if 0 <= y < h:
                d.point((x, y), fill=(0xFF, 0xF4, 0xB0, round(230 - 190 * k)))
    # sloop navegando
    bx = 104
    d.polygon([(bx, 29), (bx + 36, 29), (bx + 31, 35), (bx + 5, 35)], fill=(0x7A, 0x4E, 0x2A, 255))
    d.line((bx + 1, 29, bx + 35, 29), fill=(0xB0, 0x7C, 0x48, 255))
    d.line((bx + 4, 32, bx + 32, 32), fill=(0x5A, 0x38, 0x1C, 255))
    d.line((bx + 17, 4, bx + 17, 28), fill=(0x5A, 0x38, 0x1C, 255))
    d.polygon([(bx + 18, 5), (bx + 18, 26), (bx + 33, 26)], fill=VELA + (255,))
    d.polygon([(bx + 16, 7), (bx + 16, 26), (bx + 4, 26)], fill=(0xE4, 0xDC, 0xC4, 255))
    d.line((bx + 19, 26, bx + 33, 26), fill=(0x5A, 0x38, 0x1C, 255))
    d.polygon([(bx + 17, 1), (bx + 17, 4), (bx + 22, 2)], fill=(0xD8, 0x3A, 0x32, 255))
    # gaivotas
    for gx, gy in ((60, 8), (72, 4), (84, 12), (150, 6)):
        stamp(d, ['#...#', '.#.#.', '..#..'], gx, gy, (0xF0, 0xF0, 0xF0, 255))
    return up(img, 5)


def main():
    os.makedirs(OUT, exist_ok=True)
    font = McFont()
    titulo(font).save(os.path.join(OUT, 'titulo.png'))
    for arq, texto, cor in FLAMULAS:
        flamula(font, texto, cor).save(os.path.join(OUT, arq + '.png'))
    rosa(font).save(os.path.join(OUT, 'rosa_dos_ventos.png'))
    marinha().save(os.path.join(OUT, 'marinha.png'))
    for f in sorted(os.listdir(OUT)):
        print('%-24s %s' % (f, Image.open(os.path.join(OUT, f)).size))


if __name__ == '__main__':
    main()
