# -*- coding: utf-8 -*-
"""Menu principal do Lilyvale no FancyMenu 3.11 (Forge 1.20.1).

Rode da raiz: python tools/fancymenu/menu.py
Gera a arte em config/fancymenu/assets/lilyvale/ e o layout em
config/fancymenu/customization/lilyvale_titulo.txt. O layout é reescrito a cada execução: edite
este script, não o arquivo (edições feitas no editor do FancyMenu se perdem na próxima geração).

Desenho: o logo oficial no topo; os botões do próprio jogo (que continuam funcionando, inclusive
o de Mods do Forge) ganham textura de madeira e ficam sobre um painel com cantos de latão; à
esquerda, uma moldura de espelho com o personagem do jogador; à direita, os botões de idioma,
acessibilidade e óculos do Visor numa coluna, e o botão de VR do Visor embaixo do painel. O fundo continua sendo o panorama original do jogo, com paralaxe.

Posições: tudo o que fica em volta dos botões é ancorado no botão "Um jogador"
(mc_titlescreen_singleplayer_button), que o jogo posiciona em (largura/2 - 100, altura/4 + 48).
Assim o conjunto acompanha qualquer tamanho de janela e escala de interface.
O texto da versão sai da entrada mais recente do CHANGELOG.md; no build, o workflow troca pela versão exata.

Depende de tools/quest-book/tide_art.py (fonte do jogo para a plaquinha), que lê o client jar do
Minecraft 1.20.1 na pasta libraries do Prism: rode na instância de desenvolvimento, não no CI.
"""
import os
import shutil
import uuid

from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ASSETS = os.path.join(ROOT, 'config', 'fancymenu', 'assets', 'lilyvale')
LAYOUT = os.path.join(ROOT, 'config', 'fancymenu', 'customization', 'lilyvale_titulo.txt')
LOGO = os.path.join(ROOT, '.github', 'assets', 'Lilyvale.png')
SRC = '[source:local]/config/fancymenu/assets/lilyvale/'


def versao_atual():
    """Versão da entrada mais recente do CHANGELOG.md (a mesma fonte que o workflow de build usa)."""
    import re
    with open(os.path.join(ROOT, 'CHANGELOG.md'), encoding='utf-8') as f:
        m = re.search(r'^## \[([^\]]+)\]', f.read(), re.M)
    return m.group(1) if m else 'dev'
ANCORA = 'mc_titlescreen_singleplayer_button'

MADEIRA = [(0xD8, 0xA8, 0x70), (0xB8, 0x86, 0x52), (0x96, 0x68, 0x3C), (0x6E, 0x48, 0x28), (0x48, 0x2E, 0x18)]
LATAO = [(0xFF, 0xE4, 0x8C), (0xE8, 0xC0, 0x5A), (0xB0, 0x86, 0x30), (0x6E, 0x50, 0x18)]
NOITE = (0x10, 0x16, 0x2C)


def uid(nome):
    """IDs estáveis entre execuções, no formato que o FancyMenu usa (uuid-timestamp)."""
    return '%s-1764000000000' % uuid.uuid5(uuid.NAMESPACE_URL, 'lilyvale/menu/' + nome)


# ---------------------------------------------------------------- arte
def painel(fundo_cor=MADEIRA):
    """Painel nine-slice de 48x48: moldura de madeira escura, miolo de tábuas, cantos de latão."""
    s = 48
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, s - 1, s - 1), fill=MADEIRA[4] + (255,))
    d.rectangle((1, 1, s - 2, s - 2), fill=MADEIRA[3] + (255,))
    d.rectangle((3, 3, s - 4, s - 4), fill=MADEIRA[4] + (255,))
    for y in range(4, s - 4):                                                   # tábuas
        cor = fundo_cor[1] if (y - 4) // 6 % 2 == 0 else fundo_cor[2]
        d.line((4, y, s - 5, y), fill=cor + (255,))
        if (y - 4) % 6 == 5:
            d.line((4, y, s - 5, y), fill=fundo_cor[3] + (255,))
    for x, y in ((0, 0), (s - 9, 0), (0, s - 9), (s - 9, s - 9)):               # cantoneiras
        d.rectangle((x, y, x + 8, y + 8), fill=LATAO[2] + (255,))
        d.rectangle((x + 1, y + 1, x + 7, y + 7), fill=LATAO[1] + (255,))
        d.rectangle((x + 3, y + 3, x + 5, y + 5), fill=LATAO[3] + (255,))
        d.point((x + 2, y + 2), fill=LATAO[0] + (255,))
    return img


def botao(hover=False):
    """Botão de 200x20 (tamanho do vanilla), nine-slice com borda de 4 px.

    Madeira escura e lisa no miolo, sem veios atravessando o texto branco do botão; o relevo fica só
    nas bordas. No hover a madeira clareia um pouco e o contorno vira latão."""
    w, h = 200, 20
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if hover:
        claro, meio, escuro, contorno = MADEIRA[1], (0x84, 0x5A, 0x34), MADEIRA[3], LATAO[1]
    else:
        claro, meio, escuro, contorno = MADEIRA[2], (0x62, 0x40, 0x24), MADEIRA[4], (0x24, 0x16, 0x0C)
    d.rectangle((0, 0, w - 1, h - 1), fill=contorno + (255,))
    d.rectangle((1, 1, w - 2, h - 2), fill=meio + (255,))
    d.line((1, 1, w - 2, 1), fill=claro + (255,))
    d.line((1, 1, 1, h - 2), fill=claro + (255,))
    d.line((1, h - 2, w - 2, h - 2), fill=escuro + (255,))
    d.line((2, h - 3, w - 3, h - 3), fill=escuro + (120,))
    d.line((w - 2, 1, w - 2, h - 2), fill=escuro + (255,))
    return img


def placa(texto):
    """Plaquinha de pergaminho para o topo da moldura, com o texto na fonte do jogo."""
    import sys
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'quest-book'))
    from tide_art import McFont
    font = McFont()
    m = font.mask(texto)
    tw = sum(font.glyphs[c][1] + 1 for c in texto)
    w, h = tw + 10, m.height + 2
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, w - 1, h - 1), fill=MADEIRA[4] + (255,))
    d.rectangle((1, 1, w - 2, h - 2), fill=(0xF0, 0xE0, 0xB8, 255))
    d.line((1, h - 2, w - 2, h - 2), fill=(0xC8, 0xB0, 0x80, 255))
    for yy in range(m.height):
        for xx in range(tw):
            if m.getpixel((xx, yy)):
                d.point((5 + xx, yy - 1), fill=(0x4A, 0x30, 0x1A, 255))
    return img


def gerar_arte():
    os.makedirs(ASSETS, exist_ok=True)
    painel().save(os.path.join(ASSETS, 'painel.png'))
    painel(fundo_cor=[(0, 0, 0), (0x2A, 0x2E, 0x3A), (0x24, 0x28, 0x34), (0x1C, 0x1E, 0x28)]).save(
        os.path.join(ASSETS, 'moldura.png'))
    botao().save(os.path.join(ASSETS, 'botao.png'))
    botao(True).save(os.path.join(ASSETS, 'botao_hover.png'))
    placa('Seu reflexo').save(os.path.join(ASSETS, 'placa_espelho.png'))
    shutil.copyfile(LOGO, os.path.join(ASSETS, 'logo.png'))


# ---------------------------------------------------------------- layout
def bloco(tipo, campos):
    return tipo + ' {\n' + ''.join('  %s = %s\n' % kv for kv in campos) + '}\n'


def comuns(nome, tipo, x, y, w, h, ancora='element', extra=()):
    lr = uid(nome + '/req')
    campos = [('element_type', tipo), ('instance_identifier', nome if tipo == 'vanilla_button' else uid(nome)),
              ('appearance_delay', 'no_delay'), ('appearance_delay_seconds', '1.0'), ('fade_in_v2', 'no_fading'),
              ('fade_in_speed', '1.0'), ('fade_out', 'no_fading'), ('fade_out_speed', '1.0'), ('base_opacity', '1.0'),
              ('auto_sizing', 'false'), ('auto_sizing_base_screen_width', '0'), ('auto_sizing_base_screen_height', '0'),
              ('sticky_anchor', 'false'), ('anchor_point', ancora)]
    if ancora == 'element':
        campos.append(('anchor_point_element', ANCORA))
    campos += [('x', str(x)), ('y', str(y)), ('width', str(w)), ('height', str(h)), ('stretch_x', 'false'),
               ('stretch_y', 'false'), ('stay_on_screen', 'false' if ancora == 'element' else 'true'),
               ('element_loading_requirement_container_identifier', lr),
               ('[loading_requirement_container_meta:%s]' % lr, '[groups:][instances:]'),
               ('enable_parallax', 'false'), ('parallax_intensity_v2', '0.5'), ('invert_parallax', 'false'),
               ('animated_offset_x', '0'), ('animated_offset_y', '0'), ('load_once_per_session', 'false'),
               ('in_editor_color', '#FFC800FF'), ('layer_hidden_in_editor', 'false')]
    return list(extra) + campos


def imagem(nome, arquivo, x, y, w, h, ancora='element', nine=None):
    extra = [('source', SRC + arquivo), ('repeat_texture', 'false'),
             ('nine_slice_texture', 'true' if nine else 'false'),
             ('nine_slice_texture_border_x', str(nine or 5)), ('nine_slice_texture_border_y', str(nine or 5)),
             ('image_tint', '#FFFFFF'), ('restart_animated_on_menu_load', 'false')]
    return bloco('element', comuns(nome, 'image', x, y, w, h, ancora, extra))


def botao_extra(nome, textura=True, label=None):
    eb = uid(nome + '/exec')
    wr = uid(nome + '/ativo')
    campos = [('button_element_executable_block_identifier', eb),
              ('[executable_block:%s][type:generic]' % eb, '[executables:]')]
    if textura:
        campos += [('backgroundnormal', SRC + 'botao.png'), ('backgroundhovered', SRC + 'botao_hover.png')]
    campos += [('restartbackgroundanimations', 'true'), ('nine_slice_custom_background', 'true' if textura else 'false'),
               ('nine_slice_border_x', '4'), ('nine_slice_border_y', '4')]
    if label is not None:
        campos.append(('label', label))
    campos += [('navigatable', 'true'), ('widget_active_state_requirement_container_identifier', wr),
               ('[loading_requirement_container_meta:%s]' % wr, '[groups:][instances:]'), ('is_template', 'false')]
    return campos


def vanilla(nome, x=0, y=0, w=200, h=20, ancora='element', oculto=False, textura=True):
    """Botão do próprio jogo, com nova posição/textura. Ocultos mantêm a posição original."""
    if oculto:
        ancora, textura = 'vanilla', False
    campos = comuns(nome, 'vanilla_button', x, y, w, h, ancora, botao_extra(nome, textura))
    campos += [('is_hidden', 'true' if oculto else 'false'), ('automated_button_clicks', '0')]
    if nome == ANCORA:
        # o próprio botão âncora fica onde o jogo o coloca
        campos = [kv for kv in campos if kv[0] != 'anchor_point_element']
        campos = [(k, 'vanilla') if k == 'anchor_point' else (k, v) for k, v in campos]
    return bloco('vanilla_button', campos)


def texto(nome, conteudo, x, y, w, h, ancora, escala='1.0', cor='#FFFFFF'):
    extra = [('interactable', 'false'), ('source', conteudo), ('source_mode', 'direct'), ('shadow', 'true'),
             ('scale', escala), ('base_color', cor), ('text_border', '2'), ('line_spacing', '2'),
             ('enable_scrolling', 'false'), ('auto_line_wrapping', 'false'), ('remove_html_breaks', 'true'),
             ('parse_markdown', 'true')]
    return bloco('element', comuns(nome, 'text_v2', x, y, w, h, ancora, extra))


def jogador(nome, x, y, escala):
    extra = [('copy_client_player', 'true'), ('auto_skin', 'true'), ('auto_cape', 'true'), ('slim', 'false'),
             ('scale', str(escala)), ('is_baby', 'false'), ('crouching', 'false'), ('showname', 'false'),
             ('head_follows_mouse', 'true'), ('body_follows_mouse', 'true')]
    w, h = int(escala * 0.6), int(escala * 1.8)
    return bloco('element', comuns(nome, 'fancymenu_customization_player_entity', x, y, w, h, 'element', extra))


def gerar_layout():
    meta_req = uid('meta/req')
    out = ['type = fancymenu_layout\n\n']
    out.append(bloco('layout-meta', [
        ('identifier', 'title_screen'), ('render_custom_elements_behind_vanilla', 'true'),
        ('last_edited_time', '1764000000000'), ('is_enabled', 'true'), ('randommode', 'false'),
        ('randomgroup', '1'), ('randomonlyfirsttime', 'false'), ('layout_index', '0'),
        ('widget_identifier_revision', '2'),
        ('[loading_requirement_container_meta:%s]' % meta_req, '[groups:][instances:]')]))
    out.append('\n' + bloco('layout_action_executable_blocks', []))

    elementos = [
        # logo oficial no topo, centralizado (x = -largura/2)
        imagem('logo', 'logo.png', -128, 10, 256, 56, ancora='top-centered'),
        # painel atrás dos botões: os botões ocupam 200x104 a partir do botão "Um jogador"
        imagem('painel', 'painel.png', -12, -12, 224, 128, nine=12),
        # moldura do espelho à esquerda, plaquinha e o jogador
        imagem('moldura', 'moldura.png', -104, -12, 84, 128, nine=12),
        imagem('placa_espelho', 'placa_espelho.png', -97, -20, 70, 15),
        jogador('jogador', -77, 12, 50),
        # coluna dos botões pequenos à direita: idioma, acessibilidade e o ícone de óculos do Visor
        imagem('coluna', 'painel.png', 216, 6, 32, 82, nine=12),
        # versão do pack no canto superior esquerdo
        texto('versao', 'Lilyvale ' + versao_atual(), 4, 4, 160, 12, 'top-left', escala='1.0', cor='#E8F0C8'),
    ]
    vanillas = [
        vanilla(ANCORA),
        vanilla('mc_titlescreen_multiplayer_button', 0, 24),
        vanilla('titlescreen_mods_button', 0, 48),
        vanilla('mc_titlescreen_options_button', 0, 84, 98),
        vanilla('mc_titlescreen_quit_button', 102, 84, 98),
        vanilla('mc_titlescreen_language_button', 222, 10, 20, 20, textura=False),
        vanilla('mc_titlescreen_accessibility_button', 222, 36, 20, 20, textura=False),
        # Botões do Visor. O mod não dá nome a eles, então o FancyMenu os identifica pela posição
        # original (x e y concatenados); os ids são os que o editor do FancyMenu mostra.
        # 376322: ícone de óculos, no terceiro lugar da coluna da direita.
        vanilla('376322', 222, 62, 20, 20, textura=False),
        # 604322: botão "VR: ...", largo e embaixo do painel para o texto caber inteiro.
        vanilla('604322', 0, 122, 200, 20),
        vanilla('mc_titlescreen_realms_button', oculto=True),
        vanilla('minecraft_realms_notification_icons_widget', oculto=True),
        vanilla('minecraft_logo_widget', oculto=True),
    ]
    # splash do jogo, preso no canto inferior direito do logo
    splash = comuns('minecraft_splash_widget', 'vanilla_button', 100, 40, 80, 30, 'top-centered',
                    botao_extra('minecraft_splash_widget', textura=False))
    splash += [('is_hidden', 'false'), ('automated_button_clicks', '0')]
    vanillas.append(bloco('vanilla_button', splash))
    texto_final = ''.join(out) + '\n' + '\n'.join(elementos) + '\n' + '\n'.join(vanillas)
    os.makedirs(os.path.dirname(LAYOUT), exist_ok=True)
    with open(LAYOUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto_final)


def habilitar_titulo():
    """O FancyMenu só aplica layouts às telas listadas em customizablemenus.txt, pelo nome da classe
    (ScreenCustomization.isCustomizationEnabledForScreen). Acrescenta a tela de título sem mexer nas outras."""
    arq = os.path.join(ROOT, 'config', 'fancymenu', 'customizablemenus.txt')
    classe = 'net.minecraft.client.gui.screens.TitleScreen'
    texto = open(arq, encoding='utf-8').read() if os.path.isfile(arq) else 'type = customizablemenus\n'
    if (classe + ' {') not in texto:
        texto = texto.rstrip('\n') + '\n\n' + classe + ' {\n}\n'
        with open(arq, 'w', encoding='utf-8', newline='\n') as f:
            f.write(texto)


if __name__ == '__main__':
    gerar_arte()
    gerar_layout()
    habilitar_titulo()
    for f in sorted(os.listdir(ASSETS)):
        print('%-22s %s' % (f, Image.open(os.path.join(ASSETS, f)).size))
    print('layout:', os.path.relpath(LAYOUT, ROOT))
