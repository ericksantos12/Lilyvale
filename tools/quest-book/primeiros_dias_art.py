# -*- coding: utf-8 -*-
"""Decoração dos capítulos de Primeiros Dias: Início, Mochila e Organização e Tips & Tricks.

Rode da raiz: python tools/quest-book/primeiros_dias_art.py   (depois: gen.py --only PD04)
Gera PNGs em kubejs/assets/lilyvale/textures/quests/primeiros_dias/. Início e Mochila são
mantidos à mão: o script reescreve só o bloco `images` deles (core.apply_images), com
coordenadas em unidades do FTB Quests. As imagens de Tips & Tricks entram por chapters_a.py.

Tudo é 2D: o logo do pack, pixel art desenhada aqui, texturas do jogo montadas em cena e
sprites de itens ampliados sem suavização.
"""
import glob
import io
import os
import sys
import zipfile

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
from tide_art import MC_JAR, McFont, gradient_text  # noqa: E402

ROOT = core.ROOT
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'primeiros_dias')
TEX = 'lilyvale:textures/quests/primeiros_dias/'
CH = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters')
LOGO = os.path.join(ROOT, '.github', 'assets', 'Lilyvale.png')

ESCURO = (0x1A, 0x14, 0x10)
MADEIRA = [(0xC8, 0x94, 0x58), (0xA0, 0x6C, 0x38), (0x6E, 0x48, 0x24)]
TEAL = ((0xB8, 0xF8, 0xF0), (0x2C, 0xA8, 0xB0))

# (png, x, y, altura, hover) em unidades do FTB Quests; a largura sai da proporção do PNG
INICIO = [
    ('inicio_logo', 2.0, -2.3, 1.7, ['&a&lLilyvale', 'Um modpack aconchegante para jogar com amigos']),
    ('inicio_subtitulo', 2.0, -1.0, 0.5, ['Comece por aqui']),
    ('inicio_casa', 2.0, 2.0, 2.5, ['Um lar no vale']),
    ('inicio_placa', 6.6, 0.4, 2.4, ['Fazenda, casa, companheiros, engenharia, exploração...', 'Todas as trilhas são opcionais']),
    ('inicio_lago', 2.0, 6.3, 1.4, ['Lírios no lago de Lilyvale']),
]
MOCHILA = [
    ('mochila_titulo', 1.2, -2.1, 1.1, ['&b&lMochila e Organização', 'Cada coisa no seu lugar']),
    ('mochila_rotulo_estrada', None, -0.85, 0.45, ['Para levar nas viagens']),
    ('mochila_rotulo_casa', None, 1.15, 0.45, ['Para guardar na base']),
    ('mochila_rotulo_rede', None, 5.15, 0.45, ['Para achar tudo num lugar só']),
    ('mochila_desenho', -2.6, 0.9, 2.4, ['Mochila de aventureiro']),
    ('mochila_barris', 4.8, 4.2, 2.6, ['Um depósito bem arrumado']),
]
ROTULOS = [('mochila_rotulo_estrada', 'Na estrada'), ('mochila_rotulo_casa', 'Em casa'),
           ('mochila_rotulo_rede', 'Rede de depósito')]


def up(img, k):
    return img.resize((img.width * k, img.height * k), Image.NEAREST)


def contorno(img, cor=ESCURO, raio=3, alpha=230):
    """Contorno escuro em volta da arte, para ela não sumir no fundo do livro."""
    base = Image.new('RGBA', img.size, cor + (0,))
    base.putalpha(img.getchannel('A').filter(ImageFilter.MaxFilter(raio)).point(lambda v: alpha if v else 0))
    return Image.alpha_composite(base, img)


def pad(img, n):
    out = Image.new('RGBA', (img.width + 2 * n, img.height + 2 * n), (0, 0, 0, 0))
    out.alpha_composite(img, (n, n))
    return out


def jar(pat):
    return zipfile.ZipFile(MC_JAR if pat == 'minecraft' else glob.glob(os.path.join(ROOT, 'mods', pat))[0])


def textura(pat, path):
    return Image.open(io.BytesIO(jar(pat).read(path))).convert('RGBA')


# ---------------------------------------------------------------- Início
def casinha():
    """Chalé com telhado vermelho, chaminé fumegando, janela acesa e canteiro de flores."""
    w, h = 44, 40
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # fumaça
    for i, (x, y) in enumerate(((33, 1), (31, 3), (34, 5), (32, 7))):
        d.rectangle((x, y, x + 1 + i % 2, y + 1), fill=(0xD8, 0xD8, 0xE0, 200 - i * 20))
    d.rectangle((30, 9, 33, 16), fill=(0x8A, 0x4A, 0x3A, 255))           # chaminé
    d.rectangle((30, 9, 33, 9), fill=(0x5A, 0x30, 0x24, 255))
    # paredes de madeira
    for y in range(20, 36):
        d.line((7, y, 36, y), fill=MADEIRA[(y // 2) % 2] + (255,))
    d.rectangle((7, 20, 7, 35), fill=MADEIRA[2] + (255,))
    d.rectangle((36, 20, 36, 35), fill=MADEIRA[2] + (255,))
    # telhado
    for i in range(12):
        d.line((4 + i, 21 - i, 39 - i, 21 - i), fill=((0xC8, 0x3C, 0x32) if i % 3 else (0x9A, 0x28, 0x22)) + (255,))
    d.line((3, 21, 40, 21), fill=(0x6A, 0x1C, 0x18, 255))
    # porta e janela acesa
    d.rectangle((12, 26, 17, 35), fill=(0x5A, 0x38, 0x1C, 255))
    d.point((16, 31), fill=(0xE8, 0xC0, 0x6A, 255))
    d.rectangle((23, 24, 31, 30), fill=(0x4A, 0x30, 0x18, 255))
    d.rectangle((24, 25, 30, 29), fill=(0xFF, 0xD8, 0x6A, 255))
    d.line((27, 25, 27, 29), fill=(0x4A, 0x30, 0x18, 255))
    d.line((24, 27, 30, 27), fill=(0x4A, 0x30, 0x18, 255))
    # grama e flores
    d.rectangle((0, 36, w - 1, 39), fill=(0x5C, 0xA8, 0x3C, 255))
    d.line((0, 36, w - 1, 36), fill=(0x8C, 0xD0, 0x5C, 255))
    for x, cor in ((2, (0xF0, 0x5A, 0x8C)), (20, (0xFF, 0xE0, 0x5A)), (39, (0xF0, 0x5A, 0x8C)), (41, (0xFF, 0xFF, 0xFF))):
        d.point((x, 34), fill=cor + (255,))
        d.point((x, 35), fill=(0x3C, 0x80, 0x2C, 255))
    return up(contorno(pad(img, 2)), 6)


def placa(font):
    """Poste com três tábuas em seta, apontando para trilhas diferentes."""
    tabuas = [('Fazenda', 1), ('Casa', -1), ('Aventura', 1)]
    w, h = 100, 62
    cx = w // 2
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((cx - 2, 4, cx + 1, h - 3), fill=MADEIRA[1] + (255,))
    d.line((cx + 1, 4, cx + 1, h - 3), fill=MADEIRA[2] + (255,))
    d.rectangle((cx - 6, h - 3, cx + 5, h - 1), fill=(0x5C, 0xA8, 0x3C, 255))
    for n, (txt, lado) in enumerate(tabuas):
        y = 6 + n * 16
        m = font.mask(txt)
        tw = sum(font.glyphs[c][1] + 1 for c in txt)
        bw = tw + 8
        x0 = cx - 4 if lado > 0 else cx - bw + 4
        x1 = x0 + bw
        d.rectangle((x0, y, x1, y + 11), fill=MADEIRA[0] + (255,))
        d.line((x0, y + 11, x1, y + 11), fill=MADEIRA[2] + (255,))
        ponta = [(x1, y), (x1 + 5, y + 5), (x1, y + 11)] if lado > 0 else [(x0, y), (x0 - 5, y + 5), (x0, y + 11)]
        d.polygon(ponta, fill=MADEIRA[0] + (255,))
        tx = x0 + 4
        for yy in range(m.height):
            for xx in range(tw):
                if m.getpixel((xx, yy)):
                    d.point((tx + xx, y - 1 + yy), fill=(0x3A, 0x24, 0x10, 255))
    bbox = img.getbbox()
    return up(contorno(pad(img.crop(bbox), 2)), 4)


def lago():
    """Faixa de lago com vitórias-régias, lírios rosados e taboas nas pontas."""
    w, h = 120, 22
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((2, 6, w - 3, h - 2), radius=6, fill=(0x2E, 0x74, 0xB8, 255))
    d.rounded_rectangle((4, 8, w - 5, h - 4), radius=5, fill=(0x3C, 0x8C, 0xD0, 255))
    for x in range(8, w - 8, 9):
        d.line((x, 11 + (x // 9) % 3, x + 3, 11 + (x // 9) % 3), fill=(0x8C, 0xD0, 0xF0, 255))
    for cx, cy, flor in ((22, 13, True), (40, 16, False), (58, 12, True), (77, 15, False), (95, 13, True)):
        d.ellipse((cx - 5, cy - 3, cx + 5, cy + 3), fill=(0x4C, 0xA8, 0x3C, 255))
        d.line((cx, cy, cx + 5, cy - 2), fill=(0x3C, 0x8C, 0xD0, 255))
        if flor:
            d.rectangle((cx - 2, cy - 4, cx + 1, cy - 2), fill=(0xF8, 0xA8, 0xC8, 255))
            d.point((cx - 1, cy - 5), fill=(0xFF, 0xD8, 0xE8, 255))
            d.point((cx - 1, cy - 3), fill=(0xFF, 0xE0, 0x5A, 255))
    for x in (5, 8, w - 9, w - 6):
        d.line((x, 0 + (x % 3), x, 10), fill=(0x4C, 0x8C, 0x2C, 255))
        d.rectangle((x - 1, 1 + (x % 3), x, 4 + (x % 3)), fill=(0x7A, 0x4A, 0x24, 255))
    return up(contorno(pad(img, 2)), 6)


# ---------------------------------------------------------------- Mochila
def mochila():
    """Mochila de lona com bolso, fivelas de latão e um rolo de cobertor em cima."""
    w, h = 30, 34
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    lona = [(0xB0, 0x6C, 0x3C), (0x8C, 0x50, 0x2C), (0x5E, 0x34, 0x1C)]
    d.rounded_rectangle((5, 7, 24, 32), radius=4, fill=lona[0] + (255,))
    d.rounded_rectangle((19, 9, 24, 31), radius=3, fill=lona[1] + (255,))
    d.rounded_rectangle((7, 18, 20, 29), radius=2, fill=lona[1] + (255,))     # bolso
    d.line((8, 18, 19, 18), fill=lona[2] + (255,))
    d.rectangle((12, 19, 14, 22), fill=(0xE8, 0xC0, 0x6A, 255))             # fivela
    d.rounded_rectangle((7, 6, 22, 12), radius=2, fill=lona[1] + (255,))     # aba
    for x in (10, 18):
        d.line((x, 11, x, 15), fill=lona[2] + (255,))
        d.point((x, 15), fill=(0xE8, 0xC0, 0x6A, 255))
    d.rounded_rectangle((4, 1, 25, 6), radius=3, fill=(0x3C, 0x8C, 0x7C, 255))   # cobertor enrolado
    d.line((5, 3, 24, 3), fill=(0x5C, 0xB8, 0xA0, 255))
    for x in (9, 20):
        d.line((x, 1, x, 6), fill=lona[2] + (255,))
    d.arc((11, -2, 18, 5), 180, 360, fill=lona[2] + (255,))
    return up(contorno(pad(img, 2)), 6)


def barris():
    """Pilha de barris deitados (textura de barril do jogo) com um baú na base."""
    tampa = textura('minecraft', 'assets/minecraft/textures/block/barrel_top.png')
    lado = textura('minecraft', 'assets/minecraft/textures/block/barrel_side.png')
    w, h = 16 * 3 + 4, 16 * 3 + 4
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for linha, qtd in enumerate((1, 2, 3)):
        for i in range(qtd):
            x = (w - qtd * 16) // 2 + i * 16
            y = 2 + linha * 16
            img.alpha_composite(tampa if (linha + i) % 2 == 0 else lado.rotate(90), (x, y))
    d = ImageDraw.Draw(img)
    for linha, qtd in enumerate((1, 2, 3)):
        x0 = (w - qtd * 16) // 2
        d.line((x0, 2 + linha * 16 + 15, x0 + qtd * 16 - 1, 2 + linha * 16 + 15), fill=(0x2A, 0x1C, 0x10, 255))
    return up(contorno(pad(img, 2)), 6)


# ---------------------------------------------------------------- Tips & Tricks
def bilhete(font):
    """Papel preso com alfinete e o título escrito em tinta azul, grande e sem contorno para ler bem."""
    m = font.mask('Tips & Tricks')
    tw = sum(font.glyphs[c][1] + 1 for c in 'Tips & Tricks')
    k = 2                                  # texto em 2x dentro do papel
    w, h = tw * k + 24, m.height * k + 18
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((2, 4, w - 1, h - 1), fill=(0x00, 0x00, 0x00, 90))                # sombra
    d.rectangle((0, 2, w - 3, h - 3), fill=(0xF4, 0xEC, 0xD4, 255))
    for y in range(9, h - 4, 5):
        d.line((3, y, w - 6, y), fill=(0xD4, 0xE0, 0xEE, 255))
    d.line((8, 4, 8, h - 5), fill=(0xE8, 0x9C, 0x9C, 255))
    texto = m.crop((0, 0, tw, m.height)).resize((tw * k, m.height * k), Image.NEAREST)
    tinta = Image.new('RGBA', texto.size, (0x1C, 0x2C, 0x6C, 255))
    tinta.putalpha(texto)
    img.alpha_composite(tinta, (14, 6))
    d.ellipse((w // 2 - 3, 0, w // 2 + 2, 5), fill=(0xD8, 0x3A, 0x32, 255))       # alfinete
    d.point((w // 2 - 2, 1), fill=(0xFF, 0xB8, 0xA8, 255))
    return up(img, 5)


def polaroide(font, sprite, legenda, angulo):
    """Foto instantânea: moldura branca, céu de fundo, item em 2x e legenda embaixo."""
    if sprite.width > 16:                  # texturas em alta resolução: reduz por média para 16 px
        sprite = sprite.resize((16, 16), Image.BOX)
    w, h = 50, 50
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((1, 1, w - 1, h - 1), fill=(0, 0, 0, 90))
    d.rectangle((0, 0, w - 2, h - 2), fill=(0xF8, 0xF6, 0xF0, 255))
    for y in range(3, 37):
        k = (y - 3) / 33
        d.line((3, y, w - 5, y), fill=(int(0x8C + 0x40 * k), int(0xC8 + 0x20 * k), 0xF0, 255))
    d.rectangle((3, 31, w - 5, 36), fill=(0x6C, 0xB0, 0x4C, 255))
    img.alpha_composite(sprite.resize((32, 32), Image.NEAREST), ((w - 2 - 32) // 2, 3))
    m = font.mask(legenda)
    lw = sum(font.glyphs[c][1] + 1 for c in legenda)
    sx = (w - 2 - lw) // 2
    for yy in range(m.height):
        for xx in range(lw):
            if m.getpixel((xx, yy)):
                d.point((sx + xx, 35 + yy), fill=(0x3A, 0x3A, 0x48, 255))
    return up(img, 5).rotate(angulo, resample=Image.NEAREST, expand=True)


def camera_sprite():
    """Câmera em 16 px desenhada à mão (a textura do Camerapture é o atlas do modelo 3D, não um ícone)."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((1, 5, 14, 13), fill=(0x3A, 0x3A, 0x44, 255))
    d.rectangle((1, 5, 14, 6), fill=(0x5A, 0x5A, 0x66, 255))
    d.rectangle((4, 3, 7, 4), fill=(0x3A, 0x3A, 0x44, 255))          # visor
    d.rectangle((11, 3, 13, 4), fill=(0xD8, 0x3A, 0x32, 255))        # botão
    d.rectangle((2, 7, 3, 8), fill=(0xF0, 0xF0, 0xE0, 255))          # flash
    d.ellipse((5, 6, 12, 13), fill=(0x1A, 0x1A, 0x22, 255))          # lente
    d.ellipse((6, 7, 11, 12), fill=(0x2E, 0x5C, 0x9C, 255))
    d.point((7, 8), fill=(0xC8, 0xE8, 0xFF, 255))
    d.line((1, 14, 14, 14), fill=(0x22, 0x22, 0x2A, 255))
    return img


def chipped_sprite():
    """Quatro variantes de tábua do Chipped num quadro 2x2, para a polaroide."""
    z = jar('chipped*.jar')
    nomes = sorted(n for n in z.namelist() if n.startswith('assets/chipped/textures/block/oak_planks/') and n.endswith('.png'))
    quadro = Image.new('RGBA', (16, 16))
    for i, n in enumerate(nomes[:4]):
        t = Image.open(io.BytesIO(z.read(n))).convert('RGBA').crop((0, 0, 16, 16)).resize((8, 8), Image.NEAREST)
        quadro.alpha_composite(t, ((i % 2) * 8, (i // 2) * 8))
    return quadro


# ---------------------------------------------------------------- montagem
def titulo_texto(font, texto, cores, escala):
    return gradient_text(font, texto, cores[0], cores[1], escala, outline=(0x10, 0x24, 0x2C))


def gerar():
    os.makedirs(OUT, exist_ok=True)
    font = McFont()
    s = lambda img, nome: img.save(os.path.join(OUT, nome + '.png'))  # noqa: E731
    s(Image.open(LOGO).convert('RGBA'), 'inicio_logo')
    s(gradient_text(font, 'Seu cantinho no vale começa aqui', (0xF4, 0xF8, 0xD8), (0xA8, 0xD8, 0x6C), 3,
                    outline=(0x18, 0x24, 0x10)), 'inicio_subtitulo')
    s(casinha(), 'inicio_casa')
    s(placa(font), 'inicio_placa')
    s(lago(), 'inicio_lago')
    s(titulo_texto(font, 'Mochila e Organização', TEAL, 5), 'mochila_titulo')
    for nome, texto in ROTULOS:
        s(titulo_texto(font, texto, ((0xF0, 0xF8, 0xFF), (0x9C, 0xD8, 0xE8)), 4), nome)
    s(mochila(), 'mochila_desenho')
    s(barris(), 'mochila_barris')
    s(bilhete(font), 'mural_titulo')
    planador = textura('gliders-forge*.jar', 'assets/vc_gliders/textures/item/paraglider_wood.png')
    camera = camera_sprite()
    bussola = textura('NaturesCompass*.jar', 'assets/naturescompass/textures/item/naturescompass_00.png')
    s(polaroide(font, planador, 'Voe', 4), 'polaroide_planador')
    s(polaroide(font, camera, 'Fotos', -3), 'polaroide_camera')
    s(polaroide(font, bussola, 'Explore', 3), 'polaroide_bussola')
    s(polaroide(font, chipped_sprite(), 'Decore', -4), 'polaroide_chipped')


def aplicar(layout, arquivo):
    imgs = []
    for nome, x, y, h, hover in layout:
        pw, ph = Image.open(os.path.join(OUT, nome + '.png')).size
        w = h * pw / ph
        if x is None:      # rótulos alinhados pela esquerda das quests (borda em x = -0.5)
            x = -0.5 + w / 2
        imgs.append(dict(path=TEX + nome + '.png', x=x, y=y, w=w, h=h, hover=hover))
    core.apply_images(os.path.join(CH, arquivo), imgs)


if __name__ == '__main__':
    gerar()
    aplicar(INICIO, 'inicio.snbt')
    aplicar(MOCHILA, 'mochila_e_organizacao.snbt')
    for f in sorted(os.listdir(OUT)):
        print('%-28s %s' % (f, Image.open(os.path.join(OUT, f)).size))
