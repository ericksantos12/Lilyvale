# -*- coding: utf-8 -*-
"""Decoração do capítulo Primeiros Passos (PD02, mantido à mão).

Rode da raiz: python tools/quest-book/primeiros_passos_art.py

Gera os PNGs em kubejs/assets/lilyvale/textures/quests/primeiros_passos/ e reescreve só o
bloco `images` de config/ftbquests/quests/chapters/primeiros_passos.snbt; as quests do arquivo
ficam como estão. Coordenadas aqui são unidades do FTB Quests (as quests do capítulo ficam a
2.0 de distância), não as unidades de grade do gen.py.

Tema: o caminho da árvore à primeira forja. Título em tons de madeira e cobre, uma faixa por
fileira (Madeira e Pedra em cima, Cobre e Forja embaixo), itens da trilha em 3D e pegadas
marcando a curva entre as fileiras.
"""
import glob
import io
import os
import sys
import zipfile

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
from tide_art import MC_JAR, McFont, gradient_text, render_fish, section  # noqa: E402

ROOT = core.ROOT
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'primeiros_passos')
CHAPTER = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters', 'primeiros_passos.snbt')
TEX = 'lilyvale:textures/quests/primeiros_passos/'

MADEIRA = ((0xF2, 0xE2, 0xB0), (0x8A, 0x5A, 0x2E))
COBRE = ((0xFF, 0xD2, 0xA0), (0xC0, 0x5A, 0x28))

# (arquivo de saída, jar, textura, ângulos)
ITENS = [
    ('muda', MC_JAR, 'assets/minecraft/textures/block/oak_sapling.png', (-24, 12, 0)),
    ('martelo', 'overgeared', 'assets/overgeared/textures/item/copper_smithing_hammer.png', (28, 16, 0)),
    ('picareta_cobre', 'overgeared', 'assets/overgeared/textures/item/copper_pickaxe.png', (-30, 16, 0)),
]

# (png, x, y, altura, hover) em unidades do FTB Quests; a largura sai da proporção do PNG
LAYOUT = [
    ('pegadas', 7.6, 1.5, 2.2, ['Um passo de cada vez']),
    ('titulo', 2.0, -3.4, 2.2, ['&6&lPrimeiros Passos', 'Da árvore à primeira forja']),
    ('secao_madeira', 3.0, -1.15, 0.8, ['Madeira e Pedra', 'Tronco, bancada, lascas e a picareta de pedra']),
    ('secao_cobre', 2.0, 4.2, 0.8, ['Cobre e Forja', 'Fornalha, martelo, bigorna e polimento']),
    ('muda', -2.0, 0.0, 1.4, ['Tudo começa com uma árvore']),
    ('martelo', 3.0, 1.5, 1.7, ['Martelo de ferreiro de cobre']),
    ('picareta_cobre', -4.3, 3.0, 2.2, ['Sua primeira obra de metal']),
]


def jar(name):
    return zipfile.ZipFile(name if os.path.isfile(name) else glob.glob(os.path.join(ROOT, 'mods', name + '*.jar'))[0])


def titulo(font):
    text = gradient_text(font, 'Primeiros Passos', MADEIRA[0], COBRE[1], 6, outline=(0x24, 0x14, 0x0A))
    sub = gradient_text(font, 'Da árvore à primeira forja', (0xE8, 0xF0, 0xC8), (0x7C, 0xB0, 0x5A), 3,
                        outline=(0x18, 0x22, 0x10))
    w = max(text.width, sub.width) + 40
    img = Image.new('RGBA', (w, text.height + sub.height + 34), (0, 0, 0, 0))
    img.alpha_composite(text, ((w - text.width) // 2, 0))
    d = ImageDraw.Draw(img)
    y = text.height + 8
    # tábua com pregos de cobre separando título e subtítulo
    d.rectangle((24, y, w - 25, y + 5), fill=(0xA8, 0x74, 0x40, 255))
    d.rectangle((24, y + 6, w - 25, y + 8), fill=(0x5C, 0x3A, 0x1C, 255))
    for x in range(24, w - 25, 18):
        d.rectangle((x, y + 1, x + 9, y + 1), fill=(0xC8, 0x94, 0x58, 255))
    for x in (30, w - 36):
        d.rectangle((x, y + 1, x + 3, y + 4), fill=(0xE0, 0x86, 0x48, 255))
    img.alpha_composite(sub, ((w - sub.width) // 2, y + 14))
    return img


def pegadas():
    """Trilha de pegadas descendo em leve curva: esquerda, direita, esquerda..."""
    pe = [
        '#.#.',
        '.###',
        '####',
        '####',
        '.##.',
        '.##.',
        '.##.',
    ]
    w, h = 20, 64
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    px = img.load()
    for n in range(6):
        cx = 8 + (-4 if n % 2 == 0 else 4) + round(2 * ((n - 2.5) / 2.5) ** 2) - 1
        cy = 2 + n * 10
        rows = pe if n % 2 == 0 else [r[::-1] for r in pe]   # pé esquerdo e direito espelhados
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                if ch == '#':
                    px[cx + c - 2, cy + r] = (0x6E, 0x4A, 0x2C, 230)
        # contorno claro de terra batida
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                if ch != '#':
                    continue
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = cx + c - 2 + dx, cy + r + dy
                    if 0 <= x < w and 0 <= y < h and px[x, y][3] == 0:
                        px[x, y] = (0xC8, 0xA8, 0x78, 140)
    return img.resize((w * 6, h * 6), Image.NEAREST)


def gerar():
    os.makedirs(OUT, exist_ok=True)
    font = McFont()
    titulo(font).save(os.path.join(OUT, 'titulo.png'))
    section(font, 'Madeira e Pedra', *MADEIRA).save(os.path.join(OUT, 'secao_madeira.png'))
    section(font, 'Cobre e Forja', *COBRE).save(os.path.join(OUT, 'secao_cobre.png'))
    pegadas().save(os.path.join(OUT, 'pegadas.png'))
    for nome, jname, path, ang in ITENS:
        sprite = Image.open(io.BytesIO(jar(jname).read(path)))
        render_fish(sprite, ang, px=22).save(os.path.join(OUT, nome + '.png'))


def aplicar():
    imgs = []
    for nome, x, y, h, hover in LAYOUT:
        pw, ph = Image.open(os.path.join(OUT, nome + '.png')).size
        imgs.append(dict(path=TEX + nome + '.png', x=x, y=y, w=h * pw / ph, h=h, hover=hover))
    core.apply_images(CHAPTER, imgs)

if __name__ == '__main__':
    gerar()
    aplicar()
    for f in sorted(os.listdir(OUT)):
        print(f, Image.open(os.path.join(OUT, f)).size)
