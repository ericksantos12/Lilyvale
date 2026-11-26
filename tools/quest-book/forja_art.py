# -*- coding: utf-8 -*-
"""Decoração de Forja e Legado: Fogo, Martelo e Aço (overgeared.snbt) e Além da Netherita (FL02).

Rode da raiz: python tools/quest-book/forja_art.py   (depois: gen.py --only FL02)
Gera PNGs em kubejs/assets/lilyvale/textures/quests/forja/. Fogo, Martelo e Aço é mantido à
mão: o script reescreve só o bloco `images` dele (core.apply_images), em unidades do FTB
Quests. As imagens de Além da Netherita entram por chapters_b.py.

Tudo em 2D: pixel art desenhada aqui (bigorna, forja, plaquinhas rebitadas) e um corte do
Nether montado com as texturas do próprio jogo.
"""
import io
import os
import sys
import zipfile

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
from tide_art import MC_JAR, McFont, gradient_text  # noqa: E402

ROOT = core.ROOT
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'forja')
TEX = 'lilyvale:textures/quests/forja/'
OVERGEARED = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters', 'overgeared.snbt')

FULIGEM = (0x1E, 0x10, 0x0A)
ACO = [(0xC8, 0xCC, 0xD4), (0x9A, 0xA0, 0xAC), (0x6C, 0x72, 0x80), (0x40, 0x44, 0x4E)]
BRASA = [(0xFF, 0xF4, 0xC0), (0xFF, 0xC8, 0x48), (0xF0, 0x7A, 0x20), (0xC0, 0x34, 0x14)]

# Plaquinhas de cada ramo: (png, texto, borda direita em x, y). A borda fica 1 unidade antes
# da primeira quest da fileira.
PLACAS = [
    ('placa_ferro', 'Ferro', -5.0, 0.0, 'Molde de argila, lingote aquecido, pinças, cabeça de picareta e bigorna'),
    ('placa_projetos', 'Projetos', -1.0, -4.0, 'Mesa de desenho e projetos que aprendem com o uso'),
    ('placa_aco', 'Aço', -5.0, 6.0, 'Fundição, alto-forno, liga, aço e as ferramentas da oficina'),
    ('placa_nether', 'Nether', -1.0, 10.0, 'Fornos do Nether e a liga de netherita'),
]
# (png, x, y, altura, hover) em unidades do FTB Quests
OVER = [
    ('titulo_forja', 6.0, -7.2, 2.4, ['&6&lFogo, Martelo e Aço', 'A oficina do Overgeared']),
    ('bigorna', 12.2, -1.0, 4.4, ['Bata enquanto o ferro está quente']),
    ('forja', 6.0, 11.4, 2.6, ['O fogo da oficina não se apaga']),
]


def up(img, k):
    return img.resize((img.width * k, img.height * k), Image.NEAREST)


def contorno(img, cor=FULIGEM, raio=3, alpha=230):
    base = Image.new('RGBA', img.size, cor + (0,))
    base.putalpha(img.getchannel('A').filter(ImageFilter.MaxFilter(raio)).point(lambda v: alpha if v else 0))
    return Image.alpha_composite(base, img)


def pad(img, n):
    out = Image.new('RGBA', (img.width + 2 * n, img.height + 2 * n), (0, 0, 0, 0))
    out.alpha_composite(img, (n, n))
    return out


def textura(nome):
    z = zipfile.ZipFile(MC_JAR)
    return Image.open(io.BytesIO(z.read('assets/minecraft/textures/block/%s.png' % nome))).convert('RGBA').crop((0, 0, 16, 16))


# ---------------------------------------------------------------- Fogo, Martelo e Aço
def titulo_forja(font):
    t = gradient_text(font, 'Fogo, Martelo e Aço', BRASA[0], BRASA[3], 6, outline=FULIGEM)
    # lâmina em brasa: aço frio nas pontas, incandescente no meio
    w = t.width // 3
    lam = Image.new('RGBA', (w, 5), (0, 0, 0, 0))
    d = ImageDraw.Draw(lam)
    for x in range(4, w - 4):
        k = 1 - abs(x - w / 2) / (w / 2)
        if k > 0.55:
            cor = BRASA[0] if k > 0.85 else BRASA[1] if k > 0.7 else BRASA[2]
        else:
            cor = ACO[0] if k > 0.3 else ACO[1]
        d.line((x, 1, x, 2), fill=cor + (255,))
        d.point((x, 3), fill=tuple(int(c * 0.55) for c in cor) + (255,))
    d.polygon([(0, 2), (4, 1), (4, 3)], fill=ACO[1] + (255,))                    # ponta
    d.rectangle((w - 4, 0, w - 1, 4), fill=(0x5A, 0x38, 0x1C, 255))             # cabo
    lam = up(contorno(pad(lam, 1), raio=3), 3)
    img = Image.new('RGBA', (max(t.width, lam.width), t.height + lam.height + 4), (0, 0, 0, 0))
    img.alpha_composite(t, ((img.width - t.width) // 2, 0))
    img.alpha_composite(lam, ((img.width - lam.width) // 2, t.height + 2))
    return img


def bigorna():
    """Bigorna com martelo apoiado, lingote em brasa e faíscas voando."""
    w, h = 56, 40
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # base, cintura, corpo e chifre
    d.rectangle((14, 34, 41, 38), fill=ACO[3] + (255,))
    d.rectangle((14, 34, 41, 34), fill=ACO[2] + (255,))
    d.rectangle((20, 26, 35, 33), fill=ACO[2] + (255,))
    d.line((20, 26, 20, 33), fill=ACO[1] + (255,))
    d.rectangle((10, 18, 45, 25), fill=ACO[1] + (255,))
    d.line((10, 18, 45, 18), fill=ACO[0] + (255,))
    d.line((10, 25, 45, 25), fill=ACO[3] + (255,))
    d.polygon([(10, 18), (2, 19), (10, 23)], fill=ACO[1] + (255,))               # chifre
    d.line((2, 19, 10, 18), fill=ACO[0] + (255,))
    d.rectangle((45, 19, 49, 22), fill=ACO[2] + (255,))                         # rabo
    # lingote em brasa
    d.rectangle((22, 15, 33, 17), fill=BRASA[2] + (255,))
    d.line((22, 15, 33, 15), fill=BRASA[0] + (255,))
    d.line((23, 16, 32, 16), fill=BRASA[1] + (255,))
    # martelo apoiado no corpo
    d.line((38, 9, 47, 17), fill=(0x6E, 0x48, 0x24, 255), width=2)
    d.rectangle((33, 4, 41, 9), fill=ACO[2] + (255,))
    d.line((33, 4, 41, 4), fill=ACO[0] + (255,))
    # faíscas
    for x, y, c in ((18, 9, 0), (14, 5, 1), (24, 7, 0), (28, 3, 2), (12, 11, 2), (20, 2, 1), (9, 7, 1), (30, 10, 0)):
        d.point((x, y), fill=BRASA[c] + (255,))
        if c == 0:
            d.point((x + 1, y), fill=BRASA[1] + (200,))
    return up(contorno(pad(img, 2)), 6)


def forja():
    """Forja de tijolos com boca acesa, chaminé e um pouco de fumaça."""
    w, h = 44, 40
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tijolo, rejunte = (0x9A, 0x4C, 0x36), (0x5E, 0x2E, 0x22)
    d.rectangle((17, 3, 27, 14), fill=tijolo + (255,))                          # chaminé
    for y in range(3, 15, 3):
        d.line((17, y, 27, y), fill=rejunte + (255,))
    d.rectangle((4, 14, 40, 39), fill=tijolo + (255,))
    for y in range(14, 40, 4):
        d.line((4, y, 40, y), fill=rejunte + (255,))
        for x in range(4 + (y // 4 % 2) * 4, 41, 8):
            d.line((x, y, x, y + 3), fill=rejunte + (255,))
    d.rectangle((2, 13, 42, 15), fill=(0x6A, 0x6A, 0x72, 255))                  # tampo de pedra
    # boca da forja
    d.rectangle((12, 22, 32, 36), fill=FULIGEM + (255,))
    d.pieslice((12, 16, 32, 30), 180, 360, fill=FULIGEM + (255,))
    for i, cor in enumerate(BRASA[::-1]):
        d.polygon([(14 + i * 2, 36), (22, 22 + i * 3), (30 - i * 2, 36)], fill=cor + (255,))
    d.line((12, 37, 32, 37), fill=(0x3A, 0x3A, 0x40, 255))
    d.rectangle((22, 1, 24, 2), fill=(0xB0, 0xB0, 0xB8, 170))                    # fumaça
    d.rectangle((19, 0, 20, 0), fill=(0xC8, 0xC8, 0xD0, 120))
    return up(contorno(pad(img, 3)), 6)


def placa(font, texto):
    """Plaquinha de aço rebitada com o texto gravado."""
    m = font.mask(texto)
    tw = sum(font.glyphs[c][1] + 1 for c in texto)
    w, h = tw + 14, m.height + 4
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for y in range(h):
        cor = ACO[0] if y < 2 else ACO[1] if y < h - 3 else ACO[2]
        d.line((0, y, w - 1, y), fill=cor + (255,))
    d.rectangle((0, 0, w - 1, h - 1), outline=ACO[3] + (255,))
    for x in (2, w - 3):
        for y in (2, h - 3):
            d.point((x, y), fill=ACO[3] + (255,))
            d.point((x - 1, y - 1), fill=(0xF0, 0xF2, 0xF6, 255))
    sx = (w - tw) // 2
    for yy in range(m.height):
        for xx in range(tw):
            if m.getpixel((xx, yy)):
                d.point((sx + xx, yy), fill=(0x22, 0x24, 0x2C, 255))           # sulco
                if yy + 1 >= m.height or not m.getpixel((xx, yy + 1)):
                    d.point((sx + xx, yy + 1), fill=ACO[0] + (255,))           # brilho da gravação
    return up(contorno(pad(img, 1), raio=3), 5)


# ---------------------------------------------------------------- Além da Netherita
def titulo_netherita(font):
    return gradient_text(font, 'Além da Netherita', (0xFF, 0xE8, 0x90), (0xA8, 0x86, 0x94), 6, outline=(0x14, 0x0C, 0x12))


def corte_nether():
    """Corte do Nether com texturas do jogo: nílio carmesim, netherrack, detritos ancestrais,
    lava, bloco de magma, basalto e pedra-negra."""
    tiles = {k: textura(v) for k, v in {
        'n': 'crimson_nylium_side', 'r': 'netherrack', 'd': 'ancient_debris_side', 'l': 'lava_still',
        'b': 'basalt_side', 'k': 'blackstone', 'm': 'magma'}.items()}
    mapa = [
        'nnn..nnnn',
        'rrrlllrdr',
        'rdrmllrrb',
        'kkrrrrdkb',
    ]
    img = Image.new('RGBA', (16 * len(mapa[0]), 16 * len(mapa)), (0, 0, 0, 0))
    for y, linha in enumerate(mapa):
        for x, ch in enumerate(linha):
            if ch != '.':
                img.alpha_composite(tiles[ch], (x * 16, y * 16))
    d = ImageDraw.Draw(img)
    # vão sobre a lava: borda iluminada e brilho subindo
    for x in range(48, 80):                       # colunas 3 e 4, o vão aberto da primeira fileira
        d.point((x, 15), fill=BRASA[1] + (200,))
        d.point((x, 13 + (x % 3)), fill=BRASA[2] + (90,))
    # escurece as fileiras de baixo para dar profundidade
    sombra = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra)
    for y in range(img.height):
        ds.line((0, y, img.width, y), fill=(0x10, 0x04, 0x08, int(150 * y / img.height)))
    img = Image.alpha_composite(img, Image.composite(sombra, Image.new('RGBA', img.size), img.getchannel('A')))
    return up(contorno(pad(img, 2)), 4)


def gerar():
    os.makedirs(OUT, exist_ok=True)
    font = McFont()
    s = lambda img, nome: img.save(os.path.join(OUT, nome + '.png'))  # noqa: E731
    s(titulo_forja(font), 'titulo_forja')
    s(bigorna(), 'bigorna')
    s(forja(), 'forja')
    for nome, texto, _, _, _ in PLACAS:
        s(placa(font, texto), nome)
    s(titulo_netherita(font), 'titulo_netherita')
    s(corte_nether(), 'corte_nether')


def aplicar():
    imgs = []
    for nome, x, y, h, hover in OVER:
        pw, ph = Image.open(os.path.join(OUT, nome + '.png')).size
        imgs.append(dict(path=TEX + nome + '.png', x=x, y=y, w=h * pw / ph, h=h, hover=hover))
    for nome, texto, direita, y, dica in PLACAS:
        pw, ph = Image.open(os.path.join(OUT, nome + '.png')).size
        h = 0.9
        w = h * pw / ph
        imgs.append(dict(path=TEX + nome + '.png', x=direita - w / 2, y=y, w=w, h=h, hover=[texto, dica]))
    core.apply_images(OVERGEARED, imgs)


if __name__ == '__main__':
    gerar()
    aplicar()
    for f in sorted(os.listdir(OUT)):
        print('%-22s %s' % (f, Image.open(os.path.join(OUT, f)).size))
