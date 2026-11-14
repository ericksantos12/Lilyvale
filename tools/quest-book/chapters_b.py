# -*- coding: utf-8 -*-
"""Engenhos e Ferrovias (acréscimos EF02/EF03), O Mundo Lá Fora, Além do Horizonte, FL02."""
from core import Chapter

POSSE = 'A tarefa registra posse, sem consumir: troca e presente também valem.'

# Famílias de paisagem do Regions Unexplored -> tags de bioma em kubejs/data/lilyvale
RU_FAMILIES = {
    'ru_bosques': ['autumnal_maple_forest', 'maple_forest', 'deciduous_forest', 'silver_birch_forest',
                   'magnolia_woodland', 'orchard', 'willow_forest', 'temperate_grove', 'cold_deciduous_forest'],
    'ru_coniferas_e_gelo': ['boreal_taiga', 'golden_boreal_taiga', 'cold_boreal_taiga', 'pine_taiga', 'blackwood_taiga',
                            'redwoods', 'sparse_redwoods', 'frozen_pine_taiga', 'frozen_tundra', 'icy_heights',
                            'spires', 'pine_slopes'],
    'ru_campos_e_flores': ['flower_fields', 'poppy_fields', 'clover_plains', 'barley_fields', 'pumpkin_fields',
                           'prairie', 'grassland', 'highland_fields', 'rocky_meadow', 'shrubland', 'steppe',
                           'mauve_hills'],
    'ru_terras_aridas': ['joshua_desert', 'saguaro_desert', 'outback', 'baobab_savanna', 'dry_bushland',
                         'arid_mountains', 'chalk_cliffs', 'towering_cliffs', 'mountains'],
    'ru_aguas_e_tropicos': ['bayou', 'old_growth_bayou', 'fen', 'fungal_fen', 'marsh', 'tropical_river', 'muddy_river',
                            'cold_river', 'rocky_reef', 'hyacinth_deeps', 'grassy_beach', 'gravel_beach', 'tropics',
                            'rainforest', 'sparse_rainforest', 'eucalyptus_forest', 'bamboo_forest'],
    'ru_cavernas': ['bioshroom_caves', 'prismachasm', 'redstone_caves', 'scorching_caves', 'ancient_delta'],
}
AN_TIERS = ['iron', 'gold', 'emerald', 'diamond']
AN_GEAR = ['axe', 'boots', 'chestplate', 'helmet', 'hoe', 'leggings', 'pickaxe', 'shovel', 'sword']


def build():
    out = []

    # ------------------------------------------------------------ EF02 (novos)
    c = Chapter(0x08, 'EF02', 'logistica_em_movimento', 'EF', 1, '&b&lLogística em Movimento', 'create:packager')
    c.q('terminal', 'A', '&bTerminal a bordo', 'toms_storage:ts.storage_terminal', 2, 0,
        ['toms_storage:ts.storage_terminal', 'create:item_vault'], [
        'Com o Create Contraption Terminals, o terminal do Tom\'s enxerga cofres do Create e continua funcionando depois que a estrutura vira uma contraption: trem, elevador ou perfuratriz com depósito pesquisável.',
        'Encoste o terminal no cofre antes de montar. A tarefa pede apenas ter um terminal e um cofre de itens; a montagem não é detectada. O Ponder do terminal mostra o encaixe.',
    ], deps=['6C1100000000001A'])
    out.append(c)

    # ------------------------------------------------------------ EF03 (novos)
    c = Chapter(0x09, 'EF03', 'estacoes_e_ferrovias', 'EF', 2, '&b&lEstações e Ferrovias', 'create:track_station')
    c.q('cap', 'A', '&eQuepe de maquinista', 'railways:white_conductor_cap', 0, 1,
        ['tag:railways:conductor_caps|Obtenha um quepe de maquinista de qualquer cor'], [
        'O Steam \'n\' Rails acrescenta o quepe de maquinista. Vista você mesmo ou coloque em um Blaze Burner para ele conduzir o trem.',
        'Qualquer cor conta. ' + POSSE,
    ])
    c.q('switch', 'A', '&eAgulha de desvio', 'railways:track_switch_andesite', 1, 1, ['railways:track_switch_andesite'], [
        'A agulha escolhe para qual ramo o trem segue em uma bifurcação, à mão ou por redstone. Pátios e desvios ficam muito mais simples.',
        POSSE + ' O Ponder mostra o posicionamento.',
    ], deps=['6C1100000000001D'])
    c.q('coupler', 'A', '&eEngate e desengate', 'railways:track_coupler', 2, 1, ['railways:track_coupler'], [
        'O acoplador de trilho engata e solta vagões na estação. Dá para deixar vagões carregando enquanto a locomotiva segue viagem.',
        POSSE,
    ], deps=['6C1100000000001E'])
    c.q('semaphore', 'A', '&eBraço levantado', 'railways:semaphore', 3, 1, ['railways:semaphore'], [
        'O semáforo de braço mostra o estado do sinal ferroviário mais próximo de um jeito que se vê de longe. Monte-o em um poste ao lado do sinal.',
        POSSE,
    ], deps=['6C1100000000001F'])
    c.q('handcar', 'C', '&dNo muque', 'railways:handcar', 0, 2, ['railways:handcar'], [
        'A draisina anda no braço, sem combustível nem horário. Ótima para inspecionar a linha ou para uma ferrovia bem pequena.',
        POSSE,
    ])
    c.q('stack', 'C', '&dFumaça com estilo', 'railways:smokestack_coalburner', 1, 2, ['railways:smokestack_coalburner'], [
        'Chaminés dão cara de locomotiva à locomotiva. Há vários modelos e acabamentos; esta página pede a de carvão como exemplo.',
        POSSE,
    ])
    c.q('fuel', 'C', '&dTanque cheio', 'railways:fuel_tank', 2, 2,
        ['railways:fuel_tank', 'railways:portable_fuel_interface'], [
        'O tanque de combustível alimenta os queimadores do trem com líquidos, e a interface portátil reabastece na estação sem desmontar nada.',
        POSSE,
    ])
    c.q('whistle', 'C', '&dApito na curva', 'railways:conductor_whistle', 3, 2,
        ['railways:conductor_whistle', 'railways:remote_lens'], [
        'O apito chama o trem conduzido por um maquinista até você, e a lente remota mostra o que ele vê.',
        POSSE,
    ])
    c.q('nav', 'A', '&eItinerário na mão', 'createrailwaysnavigator:navigator', 0, 3,
        ['adv:createrailwaysnavigator:navigator|Obtenha um navegador'], [
        'O navegador do Create Railways Navigator calcula rotas pela rede: de qual estação sair, onde baldear e quanto falta.',
        'Ele precisa de trens com horários configurados para ter o que consultar. ' + POSSE,
    ])
    c.q('adisplay', 'C', '&dPainel de plataforma', 'createrailwaysnavigator:advanced_display', 1, 3,
        ['adv:createrailwaysnavigator:advanced_display|Obtenha um painel avançado de qualquer formato'], [
        'Painéis avançados mostram partidas, destinos e avisos nas plataformas e dentro dos vagões.',
        'Qualquer formato de painel conta.',
    ], deps=['nav'])
    c.q('clock', 'C', '&dHora certa', 'createrailwaysnavigator:train_station_clock', 2, 3,
        ['createrailwaysnavigator:train_station_clock'], [
        'Nenhuma estação está pronta sem um relógio. Atrasos continuam sendo responsabilidade do maquinista.',
        POSSE,
    ])
    out.append(c)

    # ------------------------------------------------------------ MF01
    c = Chapter(0x0A, 'MF01', 'atlas_de_descobertas', 'MF', 0, '&3&lAtlas de Descobertas', 'minecraft:filled_map')
    c.q('chest', 'A', '&3Tesouro para cada um', 'lootr:lootr_chest', 0, 0, ['adv:lootr:1chest|Abra um baú do Lootr'], [
        'Com o Lootr, baús de estruturas guardam um saque separado para cada jogador. Quem chega depois ainda encontra a sua parte.',
        'Por isso, não quebre esses baús: deixe-os para o próximo viajante. A tarefa detecta a abertura.',
    ])
    c.q('ten', 'M', '&6&lViajante de carteirinha', 'lootr:trophy', 1, 0, ['adv:lootr:10loot|Abra dez recipientes do Lootr'], [
        'Dez tesouros abertos pelo mundo. Você já conhece o cheiro de ruína, de mina abandonada e de navio afundado.',
        'O marco usa a contagem do próprio Lootr.',
    ], deps=['chest'])
    c.q('fifty', 'C', '&dCinquenta fechaduras', 'lootr:trophy', 2, 0, ['adv:lootr:50loot|Abra cinquenta recipientes do Lootr'], [
        'Para quem não consegue ver uma estrutura no horizonte sem ir conferir.',
        'Usa a contagem do próprio Lootr.',
    ], deps=['ten'])
    c.q('barrel', 'C', '&dAté os barris', 'lootr:lootr_barrel', 0, 1, ['adv:lootr:1barrel|Abra um barril do Lootr'], [
        'Barris de vilas e estruturas também têm saque individual.',
        'A tarefa detecta a abertura.',
    ], deps=['chest'])
    c.q('cart', 'C', '&dCarrinho esquecido', 'minecraft:chest_minecart', 1, 1, ['adv:lootr:1cart|Abra um carrinho com baú do Lootr'], [
        'Minas abandonadas escondem carrinhos com baú. Leve tochas e cuidado com as aranhas.',
        'A tarefa detecta a abertura.',
    ])
    fam = [
        ('bosques', '&dBosques de muitas cores', 'regions_unexplored:maple_sapling', 'ru_bosques',
         'Bordos de outono, pomares, bétulas prateadas, magnólias e salgueiros: florestas temperadas para passear sem pressa.'),
        ('gelo', '&dPinheiros e geada', 'regions_unexplored:pine_sapling', 'ru_coniferas_e_gelo',
         'Taigas boreais, sequoias gigantes, tundras e picos gelados. Leve agasalho e uma boa sopa.'),
        ('campos', '&dCampos e flores', 'minecraft:poppy', 'ru_campos_e_flores',
         'Campos de papoulas, trevos, cevada e abóboras, pradarias e colinas lilases: paisagens abertas, boas para fazenda e cavalo.'),
        ('aridas', '&dTerras de sol forte', 'minecraft:dead_bush', 'ru_terras_aridas',
         'Desertos de cactos e iúcas, savanas de baobás, o outback e paredões de pedra. Água na mochila, sempre.'),
        ('aguas', '&dÁguas e trópicos', 'minecraft:lily_pad', 'ru_aguas_e_tropicos',
         'Pântanos, brejos, rios, recifes, praias e florestas tropicais. Onde há água, há vida e geralmente um bom ponto de pesca.'),
        ('cavernas', '&dMundos sob a terra', 'minecraft:glow_lichen', 'ru_cavernas',
         'Cavernas de cogumelos luminosos, abismos de prismarinho, galerias de redstone e fornalhas naturais.'),
    ]
    for n, (key, title, icon, tag, text) in enumerate(fam):
        c.q(key, 'C', title, icon, n, 3, ['biome:#lilyvale:%s|Visite uma paisagem desta família' % tag], [
            text,
            'Qualquer bioma da família conta: ninguém precisa visitar todos. A Bússola da Natureza ajuda a encontrar um deles.',
        ])
    out.append(c)

    # ------------------------------------------------------------ MF02
    c = Chapter(0x0B, 'MF02', 'memorias_sob_a_terra', 'MF', 1, '&3&lMemórias Sob a Terra', 'minecraft:brush')
    c.q('brush', 'A', '&3Pincel e paciência', 'minecraft:brush', 0, 0, ['minecraft:brush'], [
        'Areia, cascalho e terra suspeitos escondem achados. Escove sem quebrar o bloco: quem tem pressa perde a relíquia.',
        'O Better Archeology espalha acampamentos, ruínas, tumbas e fósseis pelo mundo. ' + POSSE,
    ])
    c.q('shards', 'A', '&3Cacos com história', 'betterarcheology:artifact_shards', 0, 1,
        ['adv:betterarcheology:artifact_shards|Obtenha fragmentos de artefato'], [
        'Fragmentos de artefato saem das escavações e são material para pincéis melhores e para a mesa de arqueologia.',
        POSSE,
    ], deps=['brush'])
    c.q('ibrush', 'C', '&dPincel de ferro', 'betterarcheology:iron_brush', 0, 2, ['betterarcheology:iron_brush'], [
        'Pincéis melhores escovam mais rápido e duram mais. Há versões de ferro, diamante e netherita.',
        POSSE,
    ], deps=['shards'])
    c.q('unid', 'A', '&3O que será isso?', 'betterarcheology:unidentified_artifact', 1, 0,
        ['adv:betterarcheology:unidentified_artifact|Obtenha um artefato não identificado'], [
        'Fragmentos reunidos formam um artefato que ninguém sabe o que é. Guarde: a mesa de arqueologia revela o segredo.',
        POSSE,
    ], deps=['brush'])
    c.q('table', 'M', '&6&lGabinete de arqueologia', 'betterarcheology:archeology_table', 2, 0,
        ['betterarcheology:archeology_table', 'betterarcheology:unidentified_artifact'], [
        'Na mesa, o artefato é limpo e estudado até revelar um encantamento antigo que não existe em mesa de encantar nenhuma.',
        'O marco registra a mesa e um artefato esperando por ela. A identificação em si não tem detector: qual segredo sair é sorte de arqueólogo.',
    ], deps=['unid'])
    c.q('vase', 'C', '&dVaso de saque', 'betterarcheology:loot_vase', 4, 0,
        ['adv:betterarcheology:loot_vase_broken|Quebre um vaso de saque'], [
        'Vasos antigos em ruínas guardam moedas, cacos e surpresas. Estes pode quebrar sem culpa.',
        'A tarefa detecta o vaso quebrado.',
    ])
    c.q('totem', 'C', '&dTotem do crescimento', 'betterarcheology:growth_totem', 4, 1, ['betterarcheology:growth_totem'], [
        'Totens são relíquias de templos e tumbas. O do crescimento acelera as plantas ao redor: um presente e tanto para a horta.',
        POSSE,
    ])
    c.q('fossil', 'M', '&6&lOsso de verdade', 'betterarcheology:fossiliferous_dirt', 5, 0,
        ['adv:betterarcheology:fossil_found|Obtenha uma parte de fóssil'], [
        'Terra fossilífera escovada revela cabeças e corpos de fósseis. Junte as duas partes para montar o esqueleto completo.',
        'Qualquer parte de fóssil conta.',
    ])
    c.gallery('fo', [
        'betterarcheology:chicken_fossil', 'betterarcheology:sheep_fossil', 'betterarcheology:wolf_fossil',
        'betterarcheology:ocelot_fossil', 'betterarcheology:villager_fossil', 'betterarcheology:creeper_fossil',
        'betterarcheology:guardian_fossil',
    ], 0, 4, 'Um esqueleto montado para o museu. Cabeça e corpo se combinam no fóssil completo; cada espécie aparece em um tipo de sítio. '
             'Registrar exige ter o fóssil completo uma vez, sem consumo.', cols=7)
    out.append(c)

    # ------------------------------------------------------------ MF03
    c = Chapter(0x0C, 'MF03', 'caminhos_que_conectam', 'MF', 2, '&3&lCaminhos que Conectam', 'via_romana:charting_map')
    c.q('map', 'A', '&3Mapa de traçado', 'via_romana:charting_map', 0, 0, ['via_romana:charting_map'], [
        'No Via Romana, estradas de verdade viram rotas de viagem. Com o mapa de traçado na mão, caminhe pela estrada para registrá-la.',
        'Só vale chão trabalhado: trilha de terra, tijolos, madeira e outros blocos de infraestrutura. Grama solta não é estrada.',
    ])
    c.q('signs', 'A', '&3Placa no entroncamento', 'minecraft:oak_sign', 1, 0,
        ['tag:minecraft:signs|Obtenha uma placa de qualquer madeira'], [
        'Placas perto de um ponto do caminho viram destinos. Clique nela para ligar ao traçado e dar nome ao lugar.',
        'Com dois destinos ligados pela mesma estrada, dá para viajar de um ao outro. A tarefa pede apenas a placa.',
    ], deps=['map'])
    c.q('link', 'M', '&6&lO mundo ficou menor', 'minecraft:lodestone', 1, 1,
        ['adv:via_romana:story/a_strand_type_game|Conecte lugares com um caminho traçado'], [
        'Casa e vila, fazenda e porto, estação e mina: a primeira ligação muda o jeito de morar no mundo.',
        'O marco usa o avanço do próprio Via Romana, concedido ao conectar caminhos.',
    ], deps=['signs'])
    c.q('chart', 'C', '&dCinco quilômetros de estrada', 'minecraft:dirt_path', 0, 2,
        ['adv:via_romana:story/straight_up_pathing_it|Trace 5 km de caminhos'], [
        'Uma malha de estradas de respeito. Pontes, calçadas e postes de luz são por conta do seu bom gosto.',
        'Usa o avanço do próprio mod. Não depende de ferrovia nem de nenhum outro capítulo.',
    ])
    c.q('travel', 'C', '&dPé na estrada', 'minecraft:leather_boots', 1, 2,
        ['adv:via_romana:story/i_just_felt_like_running|Viaje 5 km por caminhos traçados'], [
        'Estrada boa é estrada usada. Viaje pelos seus caminhos até somar cinco quilômetros.',
        'Usa o avanço do próprio mod.',
    ])
    out.append(c)

    # ------------------------------------------------------------ AH01
    c = Chapter(0x0D, 'AH01', 'entre_as_nuvens', 'AH', 0, '&5&lEntre as Nuvens', 'aether:aether_portal_frame')
    c.q('prep', 'A', '&5Uma porta para o céu', 'minecraft:glowstone', 0, 0,
        ['minecraft:glowstone*10', 'minecraft:water_bucket'], [
        'O portal do Aether é uma moldura de pedra luminosa, do formato do portal do Nether, acesa com um balde de água.',
        'Dez blocos bastam para a moldura sem os cantos. Antes de atravessar, leve comida e blocos: cair das ilhas devolve você ao mundo de baixo.',
    ])
    c.q('enter', 'M', '&6&lAcima das nuvens', 'aether:aether_grass_block', 1, 0,
        ['dim:aether:the_aether|Entre no Aether'], [
        'Ilhas flutuantes, baleias no céu e uma luz que não existe lá embaixo. Bem-vindo ao Aether.',
        'O marco detecta a chegada à dimensão. Nada da fazenda, da casa ou de outras trilhas depende desta viagem.',
    ], deps=['prep'])
    c.q('skyroot', 'A', '&5Madeira das alturas', 'aether:skyroot_pickaxe', 2, 0, ['aether:skyroot_pickaxe'], [
        'No Aether as ferramentas do mundo de baixo rendem pouco. Comece de novo com Skyroot e suba para Holystone.',
        'Ferramentas de Skyroot às vezes dobram o que você coleta. ' + POSSE,
    ], deps=['enter'])
    c.q('ambro', 'A', '&5Luz de ambrósia', 'aether:ambrosium_shard', 3, 0, ['aether:ambrosium_shard*8'], [
        'A ambrósia é o carvão do Aether: faz tochas, alimenta o altar e ainda mata a fome num aperto.',
        POSSE,
    ], deps=['skyroot'])
    c.q('altar', 'A', '&5Altar', 'aether:altar', 4, 0, ['adv:aether:craft_altar|Obtenha um altar'], [
        'O altar encanta e repara itens usando ambrósia. É nele que a gravitita ganha seu poder e que a comida do Aether fica melhor.',
        POSSE,
    ], deps=['ambro'])
    c.q('zanite', 'A', '&5Zanita', 'aether:zanite_gemstone', 2, 1, ['adv:aether:zanite|Obtenha uma gema de zanita'], [
        'A zanita faz ferramentas que ficam mais rápidas quanto mais gastas. Uma lógica só do céu.',
        POSSE,
    ], deps=['skyroot'])
    c.q('incub', 'A', '&5Incubadora', 'aether:incubator', 3, 1, ['aether:incubator'], [
        'A incubadora choca ovos de Moa com o calor de tochas de ambrósia. Uma Moa domada salta entre ilhas com você nas costas.',
        POSSE,
    ], deps=['ambro'])
    c.q('freezer', 'A', '&5Congelador', 'aether:freezer', 4, 1, ['aether:freezer'], [
        'O congelador usa pedra de gelo para transformar itens: nuvens azuis, acessórios de gelo e outras curiosidades.',
        POSSE,
    ], deps=['altar'])
    c.q('bronze', 'M', '&6&lCalabouço de bronze', 'aether:bronze_dungeon_key', 6, 0,
        ['adv:aether:bronze_dungeon|Derrote o Slider'], [
        'Os calabouços de bronze ficam dentro das ilhas, em salas de pedra talhada. O Slider só sente picareta.',
        'O marco usa o avanço do Aether: quem já venceu não precisa repetir.',
    ])
    c.q('silver', 'M', '&6&lCalabouço de prata', 'aether:silver_dungeon_key', 7, 0,
        ['adv:aether:silver_dungeon|Derrote a Rainha Valquíria'], [
        'Templos de prata flutuam sobre nuvens. As valquírias exigem medalhas de vitória antes de aceitar o seu desafio.',
        'O marco usa o avanço do Aether.',
    ])
    c.q('gold', 'M', '&6&lCalabouço de ouro', 'aether:gold_dungeon_key', 8, 0,
        ['adv:aether:gold_dungeon|Derrote o Espírito do Sol'], [
        'A ilha de ouro guarda o Espírito do Sol. Devolva as bolas de gelo que ele lança: fogo não o incomoda.',
        'O marco usa o avanço do Aether. É o maior desafio do céu e continua sendo opcional para o resto do livro.',
    ])
    c.q('egg', 'C', '&dOvo de Moa', 'aether:blue_moa_egg', 0, 3, ['adv:aether:obtain_egg|Obtenha um ovo de Moa'], [
        'Moas botam ovos azuis, brancos e pretos. Cada cor dá uma ave com fôlego diferente para saltos no ar.',
        'Qualquer cor conta.',
    ])
    c.q('hatch', 'C', '&dChocadeira ligada', 'aether:incubator', 1, 3, ['adv:aether:incubate_moa|Choque um ovo de Moa na incubadora'], [
        'Mantenha a incubadora abastecida de tochas de ambrósia até o ovo abrir. O filhote precisa de pétalas de Aechor para crescer.',
        'A tarefa detecta a incubação.',
    ], deps=['egg'])
    c.q('phyg', 'C', '&dPorco com asas', 'minecraft:saddle', 2, 3, ['adv:aether:mount_phyg|Monte um Phyg'], [
        'No Aether, porcos voam. Leve uma sela e veja as ilhas de cima.',
        'A tarefa detecta a montaria.',
    ])
    c.q('cloud', 'C', '&dPula-pula de nuvem', 'aether:blue_aercloud', 3, 3, ['adv:aether:blue_aercloud|Pule em uma nuvem azul'], [
        'Nuvens azuis lançam você para o alto. Nuvens frias amortecem a queda. As douradas... descubra.',
        'A tarefa detecta o salto.',
    ])
    c.q('grav', 'C', '&dGravitita encantada', 'aether:enchanted_gravitite', 4, 3,
        ['adv:aether:enchanted_gravitite|Obtenha gravitita encantada'], [
        'O minério de gravitita cai para cima. Encantado no altar, vira o melhor material de ferramentas do Aether.',
        POSSE,
    ])
    c.q('sleep', 'C', '&dCochilo nas alturas', 'minecraft:white_bed', 5, 3, ['adv:aether:aether_sleep|Durma no Aether'], [
        'Monte um cantinho seguro numa ilha e passe a noite. O céu daqui não tem a pressa do de lá.',
        'A tarefa detecta o sono na dimensão.',
    ])
    c.q('lore', 'C', '&dLivro de saberes', 'aether:book_of_lore', 6, 3, ['adv:aether:read_lore|Consulte o Livro de Saberes'], [
        'O Livro de Saberes descreve cada item do Aether. Coloque um item nele para ler a história.',
        'A tarefa detecta a leitura de uma entrada.',
    ])
    out.append(c)

    # ------------------------------------------------------------ AH02
    c = Chapter(0x0E, 'AH02', 'ecos_das_profundezas', 'AH', 1, '&5&lEcos das Profundezas', 'minecraft:sculk_shrieker')
    c.q('city', 'A', '&5Cidade sem voz', 'minecraft:sculk', 0, 0,
        ['adv:deeperdarker:main/find_ancient_city|Encontre uma cidade antiga'], [
        'As cidades antigas dormem no fundo do Deep Dark. Ande agachado, leve lã para abafar os passos e não acorde quem está dormindo.',
        'A tarefa detecta a chegada à estrutura.',
    ])
    c.q('warden', 'M', '&6&lO guardião cai', 'deeperdarker:warden_carapace', 1, 0,
        ['adv:deeperdarker:main/kill_warden|Derrote um Warden'], [
        'No Deeper and Darker, o Warden guarda a chave do Otherside. É um combate para preparar com calma, de longe e, se possível, em grupo.',
        'O marco usa o avanço do mod: quem já venceu não precisa repetir.',
    ], deps=['city'])
    c.q('heart', 'A', '&5Coração das profundezas', 'deeperdarker:heart_of_the_deep', 2, 0, ['deeperdarker:heart_of_the_deep'], [
        'O Warden derrotado deixa o Coração das Profundezas. Use-o na grande moldura da cidade antiga para abrir o portal.',
        POSSE,
    ], deps=['warden'])
    c.q('other', 'M', '&6&lDo outro lado', 'deeperdarker:echo_log', 3, 0,
        ['dim:deeperdarker:otherside|Entre no Otherside'], [
        'O Otherside é um mundo inteiro de sculk: florestas de eco, cavernas floridas e criaturas que ouvem tudo.',
        'O marco detecta a chegada à dimensão. Nenhuma outra trilha do livro passa por aqui.',
    ], deps=['heart'])
    c.q('shard', 'C', '&dEco reforçado', 'deeperdarker:reinforced_echo_shard', 0, 2,
        ['adv:deeperdarker:main/obtain_reinforced_echo_shard|Obtenha um fragmento de eco reforçado'], [
        'Fragmentos de eco e carapaça de Warden formam o fragmento reforçado, base do equipamento das profundezas.',
        POSSE,
    ])
    c.q('trans', 'C', '&dTransmissor de sculk', 'deeperdarker:sculk_transmitter', 1, 2,
        ['adv:deeperdarker:main/obtain_sculk_transmitter|Obtenha um transmissor de sculk'], [
        'O transmissor abre um recipiente ligado a ele de qualquer distância. Um baú de casa sempre ao alcance.',
        POSSE,
    ], deps=['shard'])
    c.q('explore', 'C', '&dQuatro paisagens de eco', 'deeperdarker:bloom_berries', 2, 2,
        ['adv:deeperdarker:main/explore_otherside|Visite os biomas do Otherside'], [
        'Floresta de eco, terras profundas, cavernas floridas e colunas nubladas. Cada bioma tem seus recursos e seus sustos.',
        'Usa o avanço do mod, que registra cada bioma visitado.',
    ])
    c.q('temple', 'C', '&dTemplo antigo', 'deeperdarker:sculk_stone', 3, 2,
        ['adv:deeperdarker:main/find_ancient_temple|Encontre um templo antigo'], [
        'Templos antigos do Otherside guardam o melhor saque da dimensão e bastante companhia indesejada.',
        'A tarefa detecta a chegada à estrutura; saqueá-la é escolha sua.',
    ])
    c.q('staff', 'C', '&dCajado sonoro', 'deeperdarker:sonorous_staff', 4, 2,
        ['adv:deeperdarker:main/obtain_sonorous_staff|Obtenha um cajado sonoro'], [
        'O cajado sonoro devolve ao mundo o grito do Warden. Use com respeito.',
        POSSE,
    ])
    c.q('armor', 'C', '&dCarapaça vestida', 'deeperdarker:warden_chestplate', 5, 2,
        ['adv:deeperdarker:main/warden_armor|Tenha a armadura de Warden completa'], [
        'A armadura de Warden é uma melhoria da netherita feita com fragmentos reforçados.',
        'O avanço pede o conjunto completo no inventário.',
    ])
    c.q('elytra', 'C', '&dAsas de alma', 'deeperdarker:soul_elytra', 6, 2, ['deeperdarker:soul_elytra'], [
        'A élitra de alma ganha impulso sozinha em pleno voo. Para quem já voa e quer voar melhor.',
        POSSE,
    ])
    out.append(c)

    # ------------------------------------------------------------ AH03
    c = Chapter(0x0F, 'AH03', 'diario_de_bordo', 'AH', 2, '&5&lDiário de Bordo', 'ad_astra:tier_1_rocket')
    c.q('steel', 'A', '&5Aço de foguete', 'ad_astra:steel_ingot', 0, 0, ['ad_astra:steel_ingot*8'], [
        'O Ad Astra constrói tudo em aço. Confira no EMI como ele é feito neste pack: a forja de Fogo, Martelo e Aço também trabalha com aço.',
        POSSE,
    ])
    c.q('comp', 'A', '&5Sob pressão', 'ad_astra:compressor', 1, 0, ['adv:ad_astra:under_pressure|Obtenha um compressor'], [
        'O compressor transforma lingotes em placas, a pele de qualquer foguete. Ele precisa de energia.',
        POSSE,
    ], deps=['steel'])
    c.q('bench', 'A', '&5Bancada da NASA', 'ad_astra:nasa_workbench', 2, 0, ['adv:ad_astra:rocket_science|Obtenha uma bancada da NASA'], [
        'A bancada monta o foguete peça por peça: cone, tanques, aletas e motor. O EMI mostra o gabarito de cada nível.',
        POSSE,
    ], deps=['comp'])
    c.q('gen', 'A', '&5Primeira energia', 'ad_astra:coal_generator', 0, 1, ['adv:ad_astra:ad_astra|Obtenha um gerador a carvão'], [
        'O gerador a carvão alimenta as primeiras máquinas. Cabos levam a energia; painéis solares vêm depois.',
        POSSE,
    ])
    c.q('fuel', 'A', '&5Combustível', 'ad_astra:fuel_bucket', 1, 1, ['ad_astra:fuel_refinery', 'ad_astra:fuel_bucket'], [
        'O petróleo vem do fundo de oceanos e poços. A refinaria o transforma em combustível, e o foguete só decola de tanque cheio.',
        'A tarefa pede a refinaria e um balde de combustível.',
    ], deps=['gen'])
    c.q('oxy', 'A', '&5Ar para a viagem', 'ad_astra:oxygen_loader', 0, 2, ['ad_astra:oxygen_loader', 'ad_astra:gas_tank'], [
        'O carregador de oxigênio produz ar a partir de água e enche tanques e o próprio traje. Sem oxigênio no espaço, o passeio é curto.',
        'A tarefa detecta apenas os itens: ter o tanque não prova que ele está cheio. Confira o medidor antes de embarcar.',
    ])
    c.q('suit', 'A', '&5Traje espacial', 'ad_astra:space_helmet', 1, 2, ['adv:ad_astra:astronaut|Tenha o traje espacial completo'], [
        'Capacete, traje, calça e botas. O traje guarda o oxigênio e protege do frio do vácuo; carregue-o no carregador antes de sair.',
        'O avanço pede as quatro peças no inventário.',
    ], deps=['oxy'])
    c.q('rocket', 'M', '&6&lFoguete na rampa', 'ad_astra:tier_1_rocket', 3, 0,
        ['adv:ad_astra:tier_1_rocket|Obtenha um foguete de nível 1', 'ad_astra:launch_pad'], [
        'Foguete montado e plataforma de lançamento pronta. Abasteça, vista o traje, confira o oxigênio e segure o pulo para a contagem regressiva.',
        'O marco registra o foguete e a plataforma no inventário. A decolagem é o próximo passo.',
    ], deps=['bench'])
    c.q('moon', 'M', '&6&lUm pequeno passo', 'ad_astra:moon_sand', 5, 0, ['dim:ad_astra:moon|Pouse na Lua'], [
        'Silêncio, poeira cinza e a Terra no horizonte. Você chegou à Lua.',
        'O marco detecta a chegada. Guarde o foguete por perto: ele é a passagem de volta.',
    ], deps=['rocket'])
    c.q('cheese', 'C', '&dÉ mesmo de queijo', 'ad_astra:cheese', 5, 1, ['adv:ad_astra:moon_cheese|Obtenha queijo lunar'], [
        'A velha história tinha um fundo de verdade. O queijo lunar combina com qualquer tábua de frios de Lilyvale.',
        POSSE,
    ], deps=['moon'])
    c.q('dist', 'C', '&dAr dentro de casa', 'ad_astra:oxygen_distributor', 5, 3,
        ['adv:ad_astra:oxygen_distributor|Obtenha um distribuidor de oxigênio'], [
        'O distribuidor enche um ambiente fechado de ar respirável. É o coração de qualquer base fora da Terra.',
        'A tarefa pede o item; uma base selada e funcionando não é detectada automaticamente.',
    ])
    c.q('solar', 'C', '&dSol sem nuvens', 'ad_astra:solar_panel', 6, 3, ['adv:ad_astra:solar_panel|Obtenha um painel solar'], [
        'Painéis solares rendem mais onde não há atmosfera no caminho. Energia limpa para a base lunar.',
        POSSE,
    ])
    c.q('grav', 'C', '&dPés no chão', 'ad_astra:gravity_normalizer', 7, 3,
        ['adv:ad_astra:gravity_normalizer|Obtenha um normalizador de gravidade'], [
        'O normalizador devolve a gravidade de casa a um ambiente. Útil para quem cansou de quicar pela sala.',
        POSSE,
    ])
    c.q('rover', 'C', '&dPasseio de rover', 'ad_astra:tier_1_rover', 8, 3, ['adv:ad_astra:rover|Obtenha um rover'], [
        'O rover leva dois astronautas e carga pelas planícies lunares. Tem até rádio.',
        POSSE,
    ])
    c.q('t2', 'A', '&5Mais longe', 'ad_astra:tier_2_rocket', 7, 0, ['adv:ad_astra:tier_2_rocket|Obtenha um foguete de nível 2'], [
        'O desh minerado na Lua constrói o foguete de nível 2, capaz de alcançar Marte.',
        POSSE,
    ], deps=['moon'])
    c.q('mars', 'M', '&6&lPoeira vermelha', 'ad_astra:mars_sand', 8, 0, ['dim:ad_astra:mars|Pouse em Marte'], [
        'Cânions, tempestades e ruínas de quem chegou antes. Marte guarda o ostrum para o próximo foguete.',
        'O marco detecta a chegada à dimensão.',
    ], deps=['t2'])
    c.q('t3', 'C', '&dTerceiro estágio', 'ad_astra:tier_3_rocket', 9, 0, ['adv:ad_astra:tier_3_rocket|Obtenha um foguete de nível 3'], [
        'O foguete de nível 3 alcança Vênus e Mercúrio. O calor de lá pede traje reforçado.',
        POSSE,
    ], deps=['mars'])
    c.q('venus', 'C', '&dChuva ácida', 'ad_astra:venus_sandstone', 10, 0, ['dim:ad_astra:venus|Pouse em Vênus'], [
        'Vênus é quente, corrosivo e rico em calorita. Uma visita curta costuma ser suficiente.',
        'A tarefa detecta a chegada à dimensão.',
    ], deps=['t3'])
    c.q('mercury', 'C', '&dPerto demais do Sol', 'ad_astra:mercury_stone', 9, 1, ['dim:ad_astra:mercury|Pouse em Mercúrio'], [
        'Mercúrio ferve de um lado e congela do outro. Bom lugar para testar a confiança no traje.',
        'A tarefa detecta a chegada à dimensão.',
    ], deps=['t3'])
    c.q('t4', 'C', '&dÚltimo modelo', 'ad_astra:tier_4_rocket', 11, 0, ['adv:ad_astra:tier_4_rocket|Obtenha um foguete de nível 4'], [
        'Com calorita de Vênus nasce o foguete de nível 4, capaz de deixar o sistema solar.',
        POSSE,
    ], deps=['venus'])
    c.q('glacio', 'C', '&dOutro sol', 'ad_astra:glacian_log', 12, 0, ['dim:ad_astra:glacio|Pouse em Glacio'], [
        'Glacio orbita outra estrela: gelado, com árvores e ar respirável. Um novo começo, se você quiser um.',
        'A tarefa detecta a chegada à dimensão.',
    ], deps=['t4'])
    out.append(c)

    # ------------------------------------------------------------ FL02
    c = Chapter(0x10, 'FL02', 'alem_da_netherita', 'FL', 1, '&6&lAlém da Netherita', 'advancednetherite:netherite_diamond_ingot')
    c.q('base', 'A', '&6Ponto de partida', 'minecraft:netherite_ingot', 0, 0, ['minecraft:netherite_ingot'], [
        'O Advanced Netherite continua de onde a forja para: quatro ligas que somam ferro, ouro, esmeralda e diamante à netherita.',
        'Cada liga parte da anterior, na bancada comum. Equipamentos sobem de nível na mesa de ferraria, com molde de melhoria de netherita. Confira no EMI a receita válida neste pack antes de gastar um lingote.',
    ])
    tiers = [
        ('iron', 'Netherita com ferro', 'Quatro lingotes de ferro reforçam a netherita. É a liga mais barata e a porta de entrada das outras.'),
        ('gold', 'Netherita com ouro', 'A liga de ouro parte da de ferro. Piglins respeitam quem a veste, como respeitam o ouro.'),
        ('emerald', 'Netherita com esmeralda', 'A liga de esmeralda parte da de ouro. Dizem que aldeões olham com outros olhos para quem a carrega.'),
        ('diamond', 'Netherita com diamante', 'A liga de diamante é o topo: parte da de esmeralda e fecha a linha de melhorias.'),
    ]
    prev = 'base'
    for n, (t, title, text) in enumerate(tiers):
        c.q(t, 'M', '&6&l' + title, 'advancednetherite:netherite_%s_ingot' % t, n + 1, 0,
            ['advancednetherite:netherite_%s_ingot' % t], [
            text,
            'O marco registra um lingote da liga. Você não precisa refazer todo o equipamento a cada nível.',
        ], deps=[prev])
        c.q(t + '_gear', 'C', '&dUma peça à sua escolha', 'advancednetherite:netherite_%s_pickaxe' % t, n + 1, 1,
            ['tag:lilyvale:advanced_netherite_%s_gear|Obtenha uma ferramenta ou peça de armadura desta liga' % t], [
            'Escolha uma única peça para melhorar: a picareta de sempre, a espada preferida ou as botas de estimação.',
            'Qualquer ferramenta ou peça de armadura desta liga conta. O conjunto completo não é pedido em lugar nenhum.',
        ], deps=[t])
        prev = t
    out.append(c)
    return out
