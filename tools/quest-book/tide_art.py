# -*- coding: utf-8 -*-
"""Decoração do capítulo À Beira d'Água (VC06): título, faixas das seções e peixes em 3D.

Rode da raiz: python tools/quest-book/tide_art.py
Gera PNGs em kubejs/assets/lilyvale/textures/quests/pesca/.

Os peixes são os sprites grandes do Tide (textures/item/*_full.png) extrudados em voxels:
a espessura de cada coluna cresce com a distância até a borda do sprite, o que dá corpo
arredondado ao peixe e deixa as nadadeiras finas. O texto usa a fonte bitmap do próprio
Minecraft (ascii.png + accented.png do client jar).
"""
import glob
import io
import json
import math
import os
import zipfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'pesca')
MC_JAR = os.path.join(ROOT, '..', '..', '..', 'libraries', 'com', 'mojang', 'minecraft', '1.20.1',
                      'minecraft-1.20.1-client.jar')

# peixe -> (yaw, pitch, roll) em graus; o sprite olha para a esquerda
RENDERS = {
    'coelacanth': (-32, 18, -6),
    'great_white_shark': (30, 16, 5),
    'manta_ray': (-20, 42, 0),
    'blazing_swordfish': (28, 14, 8),
    'dragon_fish': (-30, 16, -8),
    'sailfish': (26, 14, 4),
    'shadow_shark': (-28, 16, -4),
}

# (arquivo, texto, cor de cima, cor de baixo)
SECTIONS = [
    ('secao_agua_doce', 'Água Doce', (0x9C, 0xF5, 0x8C), (0x3F, 0xB0, 0x5A)),
    ('secao_mar', 'Mar Aberto', (0x8C, 0xE8, 0xFF), (0x2E, 0x86, 0xD8)),
    ('secao_cavernas', 'Cavernas', (0xD8, 0xD2, 0xF0), (0x7E, 0x74, 0xA8)),
    ('secao_lava', 'Lava', (0xFF, 0xD8, 0x5A), (0xE0, 0x4A, 0x1A)),
    ('secao_vazio', 'Vazio do Overworld', (0xC8, 0x9C, 0xFF), (0x6A, 0x3A, 0xB8)),
    ('secao_end', 'Vazio do End', (0xF4, 0xF0, 0xB4), (0xA8, 0x7C, 0xD8)),
]


def tide_jar():
    return zipfile.ZipFile(glob.glob(os.path.join(ROOT, 'mods', 'tide-*.jar'))[0])


# ---------------------------------------------------------------- fonte do Minecraft
class McFont:
    def __init__(self):
        z = zipfile.ZipFile(MC_JAR)
        provs = json.loads(z.read('assets/minecraft/font/include/default.json'))['providers']
        self.glyphs = {}
        # ascii primeiro: é a fonte que o jogo usa para o latim básico
        for p in sorted(provs, key=lambda p: {'minecraft:font/ascii.png': 0, 'minecraft:font/accented.png': 1}.get(p['file'], 2)):
            img = Image.open(io.BytesIO(z.read('assets/minecraft/textures/' + p['file'].split(':')[1]))).convert('RGBA')
            rows = p['chars']
            cw, ch = img.width // len(rows[0]), img.height // len(rows)
            height = p.get('height', 8)
            scale = height / ch
            for r, row in enumerate(rows):
                for c, char in enumerate(row):
                    if char in self.glyphs or char == '\u0000':
                        continue
                    g = img.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch))
                    a = np.array(g)[:, :, 3]
                    cols = np.nonzero(a.max(axis=0))[0]
                    width = int(cols.max() + 1) if len(cols) else (3 if char == ' ' else 0)
                    if scale != 1:
                        g = g.resize((max(1, round(cw * scale)), height), Image.NEAREST)
                        width = round(width * scale)
                    self.glyphs[char] = (g, width, p['ascent'])

    def mask(self, text):
        """Máscara 1 bit do texto, com 3 px de folga acima para acentos altos."""
        top = 3
        w = sum(self.glyphs[ch][1] + 1 for ch in text)
        m = Image.new('L', (w, 8 + top + 2), 0)
        x = 0
        for ch in text:
            g, width, ascent = self.glyphs[ch]
            y = top + 7 - ascent
            m.paste(g.getchannel('A').crop((0, 0, width, g.height)), (x, y))
            x += width + 1
        return m.point(lambda v: 255 if v > 0 else 0)


def gradient_text(font, text, top, bottom, scale, outline=(0x10, 0x1C, 0x2C)):
    """Texto em pixel art: gradiente vertical, sombra do Minecraft e contorno escuro."""
    m = font.mask(text)
    w, h = m.size
    pad = 2
    img = Image.new('RGBA', (w + 2 * pad + 1, h + 2 * pad + 1), (0, 0, 0, 0))
    a = np.array(m) > 0
    # contorno (vizinhança 8) e sombra deslocada 1 px
    big = np.zeros((h + 2 * pad + 1, w + 2 * pad + 1), bool)
    big[pad:pad + h, pad:pad + w] = a
    shadow = np.zeros_like(big)
    shadow[pad + 1:pad + 1 + h, pad + 1:pad + 1 + w] = a
    ring = np.zeros_like(big)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            ring |= np.roll(np.roll(big | shadow, dy, 0), dx, 1)
    px = np.zeros((big.shape[0], big.shape[1], 4), np.uint8)
    px[ring] = outline + (255,)
    sh = tuple(int(c * 0.35) for c in bottom)
    px[shadow & ~big] = sh + (255,)
    rows = np.nonzero(big.any(axis=1))[0]
    y0, y1 = rows.min(), rows.max()
    for y in range(big.shape[0]):
        t = 0 if y1 == y0 else min(1, max(0, (y - y0) / (y1 - y0)))
        col = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        px[y][big[y]] = col + (255,)
    img = Image.fromarray(px, 'RGBA')
    return img.resize((img.width * scale, img.height * scale), Image.NEAREST)


# ---------------------------------------------------------------- voxels
def thickness(alpha):
    """Meia espessura de cada coluna: cresce com a distância (Chebyshev) até a borda."""
    h, w = alpha.shape
    d = np.where(alpha, 10 ** 6, 0)
    for _ in range(max(h, w)):
        p = np.pad(d, 1, constant_values=0)
        n = np.minimum.reduce([p[1:-1, :-2], p[1:-1, 2:], p[:-2, 1:-1], p[2:, 1:-1]]) + 1
        nd = np.where(alpha, np.minimum(d, n), 0)
        if (nd == d).all():
            break
        d = nd
    return np.where(alpha, np.clip(np.round(np.sqrt(d) * 1.25), 1, 5), 0).astype(int)


def rot(yaw, pitch, roll):
    y, p, r = (math.radians(v) for v in (yaw, pitch, roll))
    ry = np.array([[math.cos(y), 0, math.sin(y)], [0, 1, 0], [-math.sin(y), 0, math.cos(y)]])
    rx = np.array([[1, 0, 0], [0, math.cos(p), -math.sin(p)], [0, math.sin(p), math.cos(p)]])
    rz = np.array([[math.cos(r), -math.sin(r), 0], [math.sin(r), math.cos(r), 0], [0, 0, 1]])
    return rz @ rx @ ry


def render_fish(sprite, angles, px=10, ss=3):
    """Renderiza o sprite extrudado; px = pixels por voxel na saída, ss = superamostragem."""
    a = np.array(sprite.convert('RGBA'))
    alpha = a[:, :, 3] > 0
    ys, xs = np.nonzero(alpha)
    a, alpha = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1], alpha[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    t = thickness(alpha)
    H, W = alpha.shape
    R = rot(*angles)
    light = np.array([-0.45, 0.75, 0.55])
    light /= np.linalg.norm(light)
    cx, cy = W / 2, H / 2

    def T(i, j):
        return t[i, j] if 0 <= i < H and 0 <= j < W else 0

    faces = []
    for i in range(H):
        for j in range(W):
            k = t[i, j]
            if not k:
                continue
            col = a[i, j, :3].astype(float)
            x0, x1 = j - cx, j + 1 - cx
            y0, y1 = cy - i - 1, cy - i
            # frente e trás
            faces.append(([(x0, y0, k), (x1, y0, k), (x1, y1, k), (x0, y1, k)], (0, 0, 1), col))
            faces.append(([(x0, y0, -k), (x0, y1, -k), (x1, y1, -k), (x1, y0, -k)], (0, 0, -1), col))
            # laterais: só o trecho que fica exposto acima da coluna vizinha
            for di, dj, n in ((-1, 0, (0, 1, 0)), (1, 0, (0, -1, 0)), (0, -1, (-1, 0, 0)), (0, 1, (1, 0, 0))):
                nk = T(i + di, j + dj)
                if nk >= k:
                    continue
                side = col * 0.92
                for z0, z1 in ((nk, k), (-k, -nk)):
                    if n == (0, 1, 0):
                        q = [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)]
                    elif n == (0, -1, 0):
                        q = [(x0, y0, z0), (x0, y0, z1), (x1, y0, z1), (x1, y0, z0)]
                    elif n == (-1, 0, 0):
                        q = [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)]
                    else:
                        q = [(x1, y0, z0), (x1, y0, z1), (x1, y1, z1), (x1, y1, z0)]
                    faces.append((q, n, side))

    s = px * ss
    proj = []
    for q, n, col in faces:
        nv = R @ np.array(n, float)
        if nv[2] <= 0:
            continue
        pts = (R @ np.array(q, float).T).T
        shade = 0.5 + 0.55 * max(0.0, float(nv @ light))
        c = tuple(int(min(255, v * shade)) for v in col)
        proj.append((pts[:, 2].mean(), [(p[0] * s, -p[1] * s) for p in pts], c))
    proj.sort(key=lambda f: f[0])
    xs = [p[0] for f in proj for p in f[1]]
    ys = [p[1] for f in proj for p in f[1]]
    pad = 4 * ss
    ox, oy = -min(xs) + pad, -min(ys) + pad
    img = Image.new('RGBA', (int(max(xs) - min(xs) + 2 * pad), int(max(ys) - min(ys) + 2 * pad)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for _, pts, c in proj:
        poly = [(x + ox, y + oy) for x, y in pts]
        d.polygon(poly, fill=c + (255,), outline=c + (255,))
    img = img.resize((img.width // ss, img.height // ss), Image.LANCZOS)
    # contorno escuro suave para destacar do fundo do livro
    al = img.getchannel('A')
    ring = al.filter(ImageFilter.MaxFilter(5))
    base = Image.new('RGBA', img.size, (0x0B, 0x16, 0x22, 0))
    base.putalpha(ring.point(lambda v: int(v * 0.8)))
    return Image.alpha_composite(base, img)


# ---------------------------------------------------------------- composições
def title(font):
    text = gradient_text(font, 'À Beira d\'Água', (0xB8, 0xFF, 0xF4), (0x1F, 0x9C, 0xD6), 6)
    sub = gradient_text(font, 'Guia de Pesca do Vale', (0xFF, 0xF1, 0xB8), (0xE0, 0xA8, 0x40), 3)
    w = max(text.width, sub.width) + 40
    img = Image.new('RGBA', (w, text.height + sub.height + 40), (0, 0, 0, 0))
    img.alpha_composite(text, ((w - text.width) // 2, 0))
    # onda em pixel art separando título e subtítulo
    d = ImageDraw.Draw(img)
    wy = text.height + 10
    for x in range(20, w - 20, 3):
        y = wy + round(3 * math.sin(x / 14))
        d.rectangle((x, y, x + 2, y + 2), fill=(0x6F, 0xD8, 0xF0, 255))
        d.rectangle((x, y + 3, x + 2, y + 5), fill=(0x1F, 0x6C, 0x9C, 255))
    img.alpha_composite(sub, ((w - sub.width) // 2, wy + 14))
    return img


def section(font, text, top, bottom):
    t = gradient_text(font, text, top, bottom, 4)
    w = t.width + 32
    img = Image.new('RGBA', (w, t.height + 14), (0, 0, 0, 0))
    img.alpha_composite(t, (16, 0))
    d = ImageDraw.Draw(img)
    y = t.height + 4
    # filete com pontas, na cor de baixo do texto
    d.rectangle((16, y, w - 17, y + 3), fill=bottom + (255,))
    d.rectangle((16, y + 4, w - 17, y + 5), fill=tuple(int(c * 0.45) for c in bottom) + (255,))
    for x in (4, w - 12):
        d.rectangle((x, y - 2, x + 7, y + 5), fill=top + (255,))
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    font = McFont()
    sizes = {}
    title(font).save(os.path.join(OUT, 'titulo.png'))
    for fn, text, top, bottom in SECTIONS:
        section(font, text, top, bottom).save(os.path.join(OUT, fn + '.png'))
    z = tide_jar()
    for fish, ang in RENDERS.items():
        sprite = Image.open(io.BytesIO(z.read('assets/tide/textures/item/%s_full.png' % fish)))
        render_fish(sprite, ang).save(os.path.join(OUT, 'peixe_%s.png' % fish))
    for f in sorted(os.listdir(OUT)):
        im = Image.open(os.path.join(OUT, f))
        sizes[f] = im.size
        print('%-32s %4d x %d' % (f, im.width, im.height))
    return sizes


if __name__ == '__main__':
    main()
