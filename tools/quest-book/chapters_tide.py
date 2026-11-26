# -*- coding: utf-8 -*-
"""Grade de peixes do Tide no capítulo À Beira d'Água (VC06).

Uma quest por espécie, agrupadas por habitat e ordenadas por raridade. A descrição de cada uma
é montada a partir das condições de pesca do próprio jar do Tide (data/*/fishing/fish/*.json),
então muda junto com o mod. A ordem das listas abaixo define os IDs (contador único para todas as
seções): espécies novas vão no fim da lista da ÚLTIMA seção, nunca no meio.

Condições de estação são ignoradas: sem Serene Seasons, Ecliptic Seasons ou Fabric Seasons
instalados, o Tide considera todas as estações válidas (SeasonsCondition.test).
"""
import glob
import json
import os
import zipfile

from core import ROOT

ARTE = 'lilyvale:textures/quests/pesca/'
COLS = 6

# (chave, imagem do cabeçalho, origem x, origem y, dica do cabeçalho, peixes)
SECOES = [
    ('doce', 'secao_agua_doce', 0, 6, 'Rios e lagos acima de Y 40, longe do mar', [
        'minecraft:salmon', 'black_crappie', 'bluegill', 'brook_trout', 'carp', 'largemouth_bass', 'pike',
        'rainbow_trout', 'smallmouth_bass', 'white_crappie', 'yellow_perch', 'catfish', 'guppy', 'walleye',
        'arapaima', 'blossom_bass', 'frostbite_flounder', 'mirage_catfish', 'sand_tiger_shark', 'slimy_salmon',
        'sturgeon', 'bull_shark', 'mooneye']),
    ('mar', 'secao_mar', 7, 6, 'Oceanos, praias e costas acima de Y 40', [
        'minecraft:cod', 'minecraft:tropical_fish', 'anchovy', 'flounder', 'mackerel', 'ocean_perch',
        'red_snapper', 'snook', 'tuna', 'minecraft:pufferfish', 'angelfish', 'mahi_mahi', 'manta_ray',
        'sailfish', 'spore_stalker', 'swordfish', 'aquathorn', 'great_white_shark', 'marstilus', 'neptune_koi',
        'pluto_snail', 'saturn_cuttlefish', 'sun_emblem', 'uranias_pisces', 'coelacanth', 'shooting_starfish']),
    ('cavernas', 'secao_cavernas', 14, 6, 'Água abaixo de Y 40 no Overworld', [
        'cave_crawler', 'cave_eel', 'deep_grouper', 'shadow_snapper', 'abyss_angler', 'anglerfish',
        'crystal_shrimp', 'dripstone_darter', 'glowfish', 'iron_tetra', 'lapis_lanternfish', 'bedrock_tetra',
        'crystalline_carp', 'gilded_minnow', 'luminescent_jellyfish', 'chasm_eel', 'echo_snapper',
        'devils_hole_pupfish', 'midas_fish']),
    ('lava', 'secao_lava', 0, 13, 'Anzol à prova de lava ou vara de netherita', [
        'ash_perch', 'ember_koi', 'magma_mackerel', 'obsidian_pike', 'volcano_tuna', 'crimson_fangjaw',
        'inferno_guppy', 'soulscale', 'warped_guppy', 'witherfin', 'blazing_swordfish']),
    ('vazio', 'secao_vazio', 7, 13, 'Abaixo da bedrock, com o anzol do vazio', [
        'bedrock_bug', 'incandescent_larva', 'sleepy_carp', 'blue_neonfish', 'deep_blue', 'judgment_fish',
        'nephrosilu', 'pentapus', 'vengeance', 'darkness_eater', 'shadow_shark', 'alpha_fish']),
    ('end', 'secao_end', 14, 13, 'Da borda das ilhas, com o anzol do vazio', [
        'amber_rockfish', 'enderfin', 'pale_clubfish', 'chorus_cod', 'ender_glider', 'endergazer',
        'violet_carp', 'dutchman_sock', 'elytrout', 'red_40', 'mantyvern', 'snatcher_squid', 'dragon_fish',
        'voidseeker']),
]

RARIDADE = {
    'common': ('&f', 'Comum', 10), 'uncommon': ('&a', 'Incomum', 15), 'rare': ('&9', 'Raro', 25),
    'very_rare': ('&5', 'Muito raro', 40), 'legendary': ('&6&l', 'Lendário', 100),
}
HABITAT = {'doce': 'Água doce', 'mar': 'Mar', 'cavernas': 'Cavernas', 'lava': 'Lava',
           'vazio': 'Vazio do Overworld', 'end': 'Vazio do End'}

BIOMAS = {
    '#tide:has_jungle_fish': 'selvas', '#tide:has_swamp_fish': 'pântanos',
    '#tide:has_cherry_grove_fish': 'bosques de cerejeiras', '#minecraft:is_river': 'rios',
    '#tide:has_frozen_fish': 'biomas gelados ou nevados', '#tide:has_desert_fish': 'desertos e badlands',
    '#minecraft:is_deep_ocean': 'oceanos profundos', '#tide:has_coastal_fish': 'praias e costas pedregosas',
    '#tide:has_mushroom_fish': 'ilhas de cogumelos', '#tide:has_dripstone_fish': 'cavernas de espeleotemas',
    '#tide:has_deep_dark_fish': 'da Escuridão Profunda',
}
ESTRUTURAS = {'minecraft:monument': 'monumentos oceânicos', 'minecraft:ancient_city': 'de cidades ancestrais'}
LUAS = ['na lua cheia', 'na lua minguante gibosa', 'no quarto minguante', 'na lua minguante', 'na lua nova',
        'na lua crescente', 'no quarto crescente', 'na lua crescente gibosa']
CLIMA = {'rain': 'chuva', 'storm': 'tempestade', 'clear': 'céu limpo'}

# Dicas escritas à mão, somadas às geradas.
EXTRA = {
    'chasm_eel': 'Guarde uma: clicar com ela na bedrock faz a enguia comer o bloco. É assim que se abre caminho '
                 'até o vazio do Overworld.',
    'midas_fish': 'Sorte 5 sai, por exemplo, de Sorte do Mar III na vara mais a isca da sorte (+2). A linha dourada '
                  'e a vara de ouro somam +1 cada.',
    'devils_hole_pupfish': 'A faixa é estreita: de Y 20 a Y 30. O medidor de profundidade conta a partir do nível do mar (Y 63), então procure de 33 a 43 nele.',
    'aquathorn': 'Pesque na água de dentro do monumento, não no mar em volta. Cuidado com os guardiões.',
    'coelacanth': 'Noite, chuva e oceano profundo ao mesmo tempo: o rádio meteorológico avisa quando o tempo vira.',
    'shooting_starfish': 'Uma noite de lua cheia sobre oceano profundo. O calendário lunar mostra a fase.',
    'sun_emblem': 'Pesca de dia, mas conta a fase da lua daquele dia: confira no calendário lunar.',
    'blazing_swordfish': 'Com a vara flamejante (Blazing Fishing Rod), os peixes do Nether mordem em qualquer lava.',
}

POSSE = 'A tarefa registra a posse do peixe, sem consumir: pode soltá-lo ou cozinhá-lo depois.'


def carregar():
    z = zipfile.ZipFile(glob.glob(os.path.join(ROOT, 'mods', 'tide-*.jar'))[0])
    dados = {}
    for n in z.namelist():
        if n.endswith('.json') and (n.startswith('data/tide/fishing/fish/') or n.startswith('data/minecraft/fishing/fish/')):
            d = json.loads(z.read(n))
            dados[d['fish']] = d
    return dados


def horas(ranges):
    """Faixas de ticks -> 'das 19h às 5h' (tick 0 = 6h), unindo faixas que se encostam."""
    slots = set()
    for r in ranges:
        slots |= set(range(r['min'] // 1000, -(-r['max'] // 1000)))
    slots = {s % 24 for s in slots}
    if len(slots) >= 24:
        return None
    inicio = [s for s in sorted(slots) if (s - 1) % 24 not in slots]
    partes = []
    for s in inicio:
        e = s
        while (e + 1) % 24 in slots:
            e = (e + 1) % 24
        partes.append('das %dh às %dh' % ((s + 6) % 24, (e + 7) % 24))
    return ' e '.join(partes)


def descrever(fid, d, secao):
    conds = {c['type'].split(':')[1]: c for c in d.get('conditions', [])}
    onde = []
    fluido = conds.get('fluid', {}).get('fluid', 'water')
    dims = conds.get('dimension', {}).get('dimensions', [])
    if fluido == 'lava':
        onde.append('Lava do Nether.' if dims == ['minecraft:the_nether'] else 'Lava de qualquer dimensão, Overworld ou Nether.')
    elif fluido == 'void':
        if dims == ['minecraft:the_end']:
            onde.append('Vazio do End: lance a linha da borda de uma ilha, com o anzol do vazio (Hook of the Depths) na vara.')
        else:
            onde.append('Vazio do Overworld, abaixo da bedrock: abra caminho com uma Chasm Eel e pesque com o anzol do vazio (Hook of the Depths).')
    else:
        lugares = []
        if 'found_in' in conds:
            lugares += [BIOMAS[b] for b in conds['found_in']['biomes']]
        if 'either' in conds:
            for k in ('a', 'b'):
                c = conds['either'][k]
                lugares += [BIOMAS[b] for b in c.get('biomes', [])] + [ESTRUTURAS[s] for s in c.get('structures', [])]
        if 'found_in_structures' in conds:
            lugares.append('dentro de ' + ESTRUTURAS[conds['found_in_structures']['structures'][0]])
        agua = 'água doce' if 'freshwater' in conds else 'água salgada' if 'saltwater' in conds else 'qualquer água'
        prof = ''
        if 'above' in conds:
            prof = ', acima de Y %d' % conds['above']['y']
        elif 'below' in conds:
            prof = ', abaixo de Y %d' % conds['below']['y']
        elif 'depth_range' in conds:
            prof = ', entre Y %d e Y %d' % (conds['depth_range']['min_y'], conds['depth_range']['max_y'])
        txt = 'Em %s' % agua
        if lugares:
            if lugares[0].startswith('dentro'):
                txt += ', ' + lugares[0]
            else:
                txt += ' ' + ' ou '.join(l if l.startswith(('da ', 'de ')) else 'de ' + l for l in lugares)
        onde.append(txt + prof + '.')
    linhas = ['&3Onde:&r ' + ' '.join(onde)]
    quando = []
    if 'time_of_day' in conds:
        h = horas(conds['time_of_day']['ranges'])
        if h:
            quando.append(h)
    if 'weather' in conds:
        quando.append('com ' + ' ou '.join(CLIMA[w] for w in conds['weather']['types']))
    if 'moon_phase' in conds:
        quando.append(' ou '.join(LUAS[p] for p in conds['moon_phase']['any_of']))
    if quando:
        linhas.append('&3Quando:&r ' + ', '.join(quando) + '.')
    if 'luck' in conds:
        linhas.append('&3Sorte:&r pelo menos %d de sorte de pesca.' % conds['luck']['min'])
    for m in d.get('modifiers', []):
        if m['type'] == 'tide:temperature':
            t, tol = m['preferred_temperature'], m['temperature_tolerance']
            clima = 'frias' if t <= -0.3 else 'quentes' if t >= 0.3 else 'amenas'
            txt = '&3Clima:&r prefere águas %s' % clima
            txt += ' e quase não aparece fora delas.' if tol <= 0.25 else '; aparece mais em biomas assim.'
            linhas.append(txt)
    if fid.split(':')[1] in EXTRA:
        linhas.append(EXTRA[fid.split(':')[1]])
    if fluido == 'lava' and secao == 'lava':
        linhas.append('Precisa do anzol à prova de lava (Lavaproof Hook) ou de uma vara de netherita.')
    linhas.append(POSSE)
    return linhas


def build(c, reg_items=None):
    """Acrescenta a decoração e a grade ao capítulo VC06 (depois das quests de progressão)."""
    dados = carregar()
    vistos = set()
    for chave, img, ox, oy, dica, peixes in SECOES:
        c.image(ARTE + img + '.png', ox + 2.5, oy - 1.2, None, 1.0, [HABITAT[chave], dica])
        for n, p in enumerate(peixes):
            fid = p if ':' in p else 'tide:' + p
            assert fid in dados, 'peixe sem dados no jar do Tide: ' + fid
            assert fid not in vistos, fid
            vistos.add(fid)
            d = dados[fid]
            rar = d.get('journal_profile', {}).get('rarity', 'common')
            cor, nome, xp = RARIDADE[rar]
            lend = rar == 'legendary'
            c.q('%s%02d' % (chave, n + 1), 'C', None, fid, ox + n % COLS, oy + n // COLS, [fid],
                descrever(fid, d, chave), sub='%s%s &7· %s' % (cor, nome, HABITAT[chave]), xp=xp,
                shape='gear' if lend else None, size='1.25d' if lend else None)
    faltando = sorted(set(dados) - vistos)
    return faltando
