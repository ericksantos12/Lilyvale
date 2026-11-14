# -*- coding: utf-8 -*-
"""Companheiros e Coleções, Criando seu Lar, A Jornada até o End."""
from core import Chapter

POSSE = 'A tarefa registra posse, sem consumir: troca e presente também valem.'
PERTO = 'Chegue perto e mire no animal até a tarefa registrar. Observar basta: nada de capturar, domar ou machucar.'

EYES = ['old_eye', 'rogue_eye', 'black_eye', 'cold_eye', 'lost_eye', 'corrupted_eye', 'nether_eye', 'cursed_eye',
        'magical_eye', 'guardian_eye', 'wither_eye', 'evil_eye', 'cryptic_eye', 'witch_eye', 'undead_eye', 'exotic_eye']


def build(village_plushies, treasure_plushies, rare_plushies):
    out = []

    # ------------------------------------------------------------ CC01
    c = Chapter(0x11, 'CC01', 'pequenos_e_grandes_companheiros', 'CC', 0,
                '&d&lPequenos e Grandes Companheiros', 'crittersandcompanions:pearl_necklace_1')
    c.q('net', 'A', '&dRede de captura', 'naturalist:capture_net', 0, 0, ['naturalist:capture_net'], [
        'A rede do Naturalist recolhe criaturas pequenas, como borboletas, vaga-lumes e caracóis, sem machucar. Solte-as no jardim de casa.',
        'A fauna de Lilyvale é para conviver: nenhuma página deste capítulo pede caça. ' + POSSE,
    ])
    c.q('hamster', 'A', '&dBolinha de pelo', 'minecraft:wheat_seeds', 2, 0,
        ['ent:hamsters:hamster|Observe um hamster de perto'], [
        'Hamsters aparecem em campos e florestas. Sementes de trigo, beterraba ou abóbora conquistam a confiança deles.',
        PERTO,
    ])
    c.q('wheel', 'A', '&dCantinho do hamster', 'hamsters:hamster_wheel', 3, 0, ['hamsters:hamster_wheel'], [
        'Uma roda de exercícios e um cercadinho seguro fazem um lar de hamster. Eles sobem em escadas e túneis.',
        'A tarefa pede a roda; o resto do habitat é projeto seu.',
    ], deps=['hamster'])
    c.q('bear', 'C', '&dDoce para o urso', 'minecraft:honeycomb', 5, 0,
        ['adv:naturalist:husbandry/feed_bear_honeycomb|Dê um favo de mel a um urso'], [
        'Ursos adoram favo de mel. Jogue um favo perto e espere o urso pegar. De longe: urso com fome não é bom vizinho.',
        'A tarefa detecta o urso pegando o favo.',
    ])
    c.q('hippo', 'C', '&dMelancia inteira', 'minecraft:melon', 6, 0,
        ['adv:naturalist:husbandry/feed_hippo_melon|Dê uma melancia a um hipopótamo'], [
        'Hipopótamos comem melancias inteiras de uma bocada só. Ofereça uma e veja com os próprios olhos.',
        'A tarefa detecta a interação.',
    ])
    c.q('giraffe', 'C', '&dVista do alto', 'minecraft:map', 7, 0,
        ['adv:naturalist:husbandry/ride_giraffe_with_map|Monte uma girafa segurando um mapa'], [
        'Lá de cima da girafa se enxerga longe. Leve um mapa na mão, como todo bom explorador.',
        'A tarefa detecta a montaria com o mapa.',
    ])
    cr = [('otter', 'Lontra'), ('ferret', 'Furão'), ('red_panda', 'Panda-vermelho'), ('shima_enaga', 'Shima enaga'),
          ('dumbo_octopus', 'Polvo-dumbo'), ('sea_bunny', 'Coelho-do-mar'), ('koi_fish', 'Carpa koi'), ('dragonfly', 'Libélula'),
          ('snail', 'Caracol'), ('leaf_insect', 'Bicho-folha'), ('jumping_spider', 'Aranha-saltadora'), ('ladybug', 'Joaninha')]
    c.gallery('cr', [('ent:crittersandcompanions:%s|Observe: %s' % (e, n), 'crittersandcompanions:%s_spawn_egg' % e) for e, n in cr],
              0, 2, ['Um encontro com os pequenos do Critters and Companions. Cada um vive em seu canto: rios, florestas, recifes, jardins.', PERTO])
    na = [('deer', 'Cervo'), ('bear', 'Urso'), ('boar', 'Javali'), ('elephant', 'Elefante'), ('giraffe', 'Girafa'), ('zebra', 'Zebra'),
          ('lion', 'Leão'), ('hippo', 'Hipopótamo'), ('rhino', 'Rinoceronte'), ('capybara', 'Capivara'), ('tortoise', 'Jabuti'), ('duck', 'Pato'),
          ('butterfly', 'Borboleta'), ('firefly', 'Vaga-lume'), ('hedgehog', 'Ouriço'), ('alligator', 'Jacaré'), ('ostrich', 'Avestruz'), ('snake', 'Cobra')]
    c.gallery('na', [('ent:naturalist:%s|Observe: %s' % (e, n), 'naturalist:%s_spawn_egg' % e) for e, n in na],
              0, 5, ['Vida selvagem do Naturalist. Savanas, florestas e pântanos têm moradores próprios; alguns são mansos, outros pedem distância.', PERTO])
    out.append(c)

    # ------------------------------------------------------------ CC02
    c = Chapter(0x12, 'CC02', 'vida_no_estabulo', 'CC', 1, '&d&lVida no Estábulo', 'minecraft:saddle')
    c.q('own', 'A', '&dUm cavalo para chamar de seu', 'minecraft:lead', 0, 0,
        ['adv:icys-better-horses:hold_your_horses|Torne-se dono de um cavalo'], [
        'No Icy\'s Better Horses, cavalos têm raça, temperamento e vínculo com o dono. Dome um, dê um nome e cuide: ele retribui.',
        'A tarefa usa o avanço do mod, concedido quando o cavalo passa a ser seu.',
    ])
    c.q('saddle', 'A', '&dSela reforçada', 'icys-better-horses:upgraded_saddle', 1, 0,
        ['adv:icys-better-horses:all_tacked_up|Obtenha uma sela reforçada'], [
        'A sela reforçada abre espaços de equipamento no cavalo: ferraduras, kit médico, estabilizador, engate de carroça.',
        POSSE,
    ], deps=['own'])
    c.q('gear', 'A', '&dFerraduras', 'icys-better-horses:horse_hooves_gear', 2, 0,
        ['icys-better-horses:horse_hooves_gear', 'icys-better-horses:horse_medkit_gear'], [
        'Ferraduras protegem os cascos em viagens longas e o kit médico cuida do cavalo quando o passeio dá errado.',
        'A tarefa pede as duas peças; instalá-las é com você e com a sela reforçada.',
    ], deps=['saddle'])
    c.q('home', 'A', '&dOnde mora o feno', 'minecraft:hay_block', 0, 1,
        ['adv:icys-better-horses:home_is_where_the_hay_is|Defina a casa do seu cavalo'], [
        'Todo cavalo precisa de uma baia para chamar de casa. Com a casa definida, ele sabe para onde voltar.',
        'A tarefa detecta a casa definida.',
    ], deps=['own'])
    c.q('bond', 'M', '&6&lAmigo para a vida toda', 'minecraft:golden_carrot', 0, 2,
        ['adv:icys-better-horses:ride_or_die|Alcance o vínculo máximo com um cavalo'], [
        'Passeios, cuidado e petiscos constroem o vínculo. No máximo, vocês dois se entendem sem rédea.',
        'O marco usa o avanço do mod. Não há atalho: é convivência.',
    ], deps=['home'])
    c.q('book', 'A', '&dManual do estábulo', 'icys-better-horses:stable_handbook_book', 3, 0,
        ['icys-better-horses:stable_handbook_book'], [
        'O manual do próprio mod explica raças, equipamento, vínculo e criação com mais detalhe do que cabe aqui.',
        POSSE,
    ])
    c.q('foal', 'C', '&dPatas compridas', 'minecraft:wheat', 0, 4, ['adv:icys-better-horses:foal_play|Tenha um potro nascido no seu estábulo'], [
        'Dois cavalos bem cuidados, um pouco de privacidade e logo há um potro desengonçado no pasto.',
        'A tarefa detecta o nascimento.',
    ])
    c.q('mixed', 'C', '&dO melhor dos dois', 'minecraft:golden_apple', 1, 4,
        ['adv:icys-better-horses:best_of_both_worlds|Tenha um potro de raças diferentes'], [
        'Cruzar raças combina características dos pais. Criadores pacientes chegam a cavalos sob medida.',
        'A tarefa detecta o potro mestiço.',
    ], deps=['foal'])
    c.q('ten', 'C', '&dEstábulo cheio', 'minecraft:oak_fence_gate', 2, 4,
        ['adv:icys-better-horses:stable_genius|Seja dono de dez cavalos'], [
        'Dez cavalos pedem pasto, baias e muito feno. Um haras de verdade.',
        'Usa a contagem do próprio mod.',
    ])
    c.q('cart', 'C', '&dCarroça atrelada', 'icys-better-horses:horse_cart_gear', 3, 4,
        ['icys-better-horses:horse_cart_gear', 'icys-better-horses:wheel*2'], [
        'O engate de carroça transforma o cavalo em transporte de carga e de passageiros. Ótimo com as estradas do Via Romana.',
        POSSE,
    ])
    c.q('fast', 'C', '&dVento na crina', 'minecraft:sugar', 4, 4,
        ['adv:icys-better-horses:built_different|Alcance alta velocidade a cavalo'], [
        'Raça, treino e estrada boa: descubra quão rápido seu melhor cavalo consegue ir.',
        'Usa o avanço do mod, que mede a velocidade máxima.',
    ])
    br = [('icelandic', 'Islandês'), ('haflinger', 'Haflinger'), ('morgan', 'Morgan'), ('quarter', 'Quarto de Milha'),
          ('arabian', 'Árabe'), ('mustang', 'Mustangue'), ('appaloosa', 'Appaloosa'), ('american_paint', 'Paint Horse'),
          ('andalusian', 'Andaluz'), ('thoroughbred', 'Puro-sangue Inglês'), ('friesian', 'Frísio'), ('percheron', 'Percheron'),
          ('belgian', 'Belga de tração'), ('clydesdale', 'Clydesdale'), ('shire', 'Shire')]
    c.gallery('br', [('ent:icys-better-horses:%s_horse|Observe: %s' % (e, n), 'icys-better-horses:%s_horse_spawn_egg' % e) for e, n in br],
              0, 6, ['Uma raça para o caderno do criador. Cada uma prefere certas paisagens e tem porte e temperamento próprios.',
                     'Chegue perto e mire no cavalo até a tarefa registrar. Observar basta; domar é opcional.'])
    out.append(c)

    # ------------------------------------------------------------ CC03 (novo cartão)
    c = Chapter(0x13, 'CC03', 'immersive_melodies', 'CC', 2, '&d&lMúsica para Lilyvale', 'immersive_melodies:lute')
    c.q('first', 'A', '&dPrimeira nota', 'minecraft:note_block', 1.5, 0,
        ['tag:immersive_melodies:instruments|Obtenha um instrumento qualquer'], [
        'Com um instrumento na mão, clique com o botão direito para abrir a lista de melodias. Você pode tocar as que vêm com o mod ou importar arquivos MIDI.',
        'Quem estiver por perto ouve: dá para montar banda, serenata e festa de colheita. Qualquer instrumento conta; a coleção abaixo é toda opcional.',
    ])
    out.append(c)

    # ------------------------------------------------------------ LR01
    c = Chapter(0x14, 'LR01', 'da_planta_a_fachada', 'LR', 0, '&e&lDa Planta à Fachada', 'chipped:mason_table')
    c.q('chipped', 'A', '&eMil jeitos de ser pedra', 'chipped:mason_table', 0, 0,
        ['chipped:mason_table', 'chipped:carpenters_table'], [
        'As bancadas do Chipped transformam um bloco comum em dezenas de variações, sem custo extra. A do pedreiro cuida de pedras e tijolos; a do carpinteiro, de madeiras.',
        'Escolha uma paleta de três ou quatro variações e repita pela construção. O livro não cataloga texturas: a coleção é a sua casa.',
    ])
    c.q('benches', 'C', '&dOficina de acabamentos', 'chipped:loom_table', 0, 1,
        ['chipped:loom_table', 'chipped:botanist_workbench', 'chipped:tinkering_table', 'chipped:alchemy_bench'], [
        'Tear para lãs e tapetes, bancada de botânica para plantas, mesa de engenhocas para redstone e lanternas, e bancada de alquimia para vidros e brilhos.',
        POSSE,
    ], deps=['chipped'])
    c.q('stick', 'A', '&eVareta de construção', 'constructionstick:wooden_stick', 2, 0, ['constructionstick:wooden_stick'], [
        'A vareta estende a face para a qual você olha, usando blocos do inventário. Paredes, pisos e telhados sobem em poucos cliques.',
        'A de madeira já ajuda; materiais melhores alcançam mais blocos por vez. ' + POSSE,
    ])
    c.q('stick2', 'C', '&dVareta de ferro', 'constructionstick:iron_stick', 2, 1, ['constructionstick:iron_stick'], [
        'Mais alcance, mais durabilidade e espaço para melhorias.',
        POSSE,
    ], deps=['stick'])
    c.q('templ', 'C', '&dKit de reforma', 'constructionstick:template_replacement', 2, 2,
        ['constructionstick:template_angel', 'constructionstick:template_replacement'], [
        'O molde angelical coloca blocos no ar, sem apoio. O de substituição troca o material de uma parede inteira sem derrubá-la: perfeito para mudar de paleta.',
        'Moldes se aplicam à vareta de ferro ou melhor. ' + POSSE,
    ], deps=['stick2'])
    c.q('amend', 'A', '&eDetalhes que mudam tudo', 'minecraft:lantern', 4, 0,
        ['minecraft:lantern', 'minecraft:flower_pot'], [
        'O Amendments melhora blocos que você já conhece. Lanternas podem ser presas na parede, vasos podem ser pendurados no teto e tapetes cobrem escadas e lajes.',
        'Também dá para misturar corantes no caldeirão e empilhar bolos. A tarefa pede só uma lanterna e um vaso para experimentar.',
    ])
    c.q('cake', 'C', '&dBolo de dois andares', 'minecraft:cake', 4, 1, ['minecraft:cake*2'], [
        'Coloque um bolo sobre outro para montar um bolo de dois andares. Uma vela em cima e está pronta a festa.',
        'A tarefa confere dois bolos no inventário; empilhar é a parte divertida.',
    ], deps=['amend'])
    out.append(c)

    # ------------------------------------------------------------ LR02
    c = Chapter(0x15, 'LR02', 'um_lar_com_vida', 'LR', 1, '&e&lUm Lar com Vida', 'another_furniture:oak_chair')
    c.q('night', 'M', '&6&lPrimeira noite em casa', 'minecraft:red_bed', 4, 0,
        ['adv:minecraft:adventure/sleep_in_bed|Durma em uma cama'], [
        'Quatro paredes, um teto e uma cama. Tudo o que vem depois é capricho, e capricho é o assunto deste capítulo.',
        'O marco detecta uma noite dormida. Os cômodos abaixo são independentes: monte só os que quiser.',
    ])
    c.q('hammer', 'A', '&eMartelo de móveis', 'another_furniture:furniture_hammer', 0, 0, ['another_furniture:furniture_hammer'], [
        'O martelo do Another Furniture muda o formato dos móveis: encostos, braços de sofá, pernas de mesa. Clique no móvel colocado para alternar.',
        POSSE,
    ])
    c.q('plate', 'A', '&ePrato na mesa', 'displaydelight:food_plate', 1, 0,
        ['displaydelight:food_plate', 'displaydelight:small_food_plate'], [
        'Com o Display Delight a comida aparece servida. Coloque o prato na mesa e clique com a refeição na mão; sobremesas vão no prato pequeno.',
        'Funciona com muitas receitas do Caderno de Receitas. ' + POSSE,
    ])
    rooms = [
        ('kitchen', '&dCozinha', 'another_furniture:oak_shelf', 0,
         ['tag:another_furniture:shelves|Uma prateleira de qualquer madeira', 'tag:another_furniture:drawers|Um gaveteiro de qualquer madeira',
          'dustydecorations:ceramic_pot'],
         'Prateleiras para os potes, gaveteiro para os talheres e um vaso de cerâmica no canto. A cozinha é onde a casa conversa.'),
        ('living', '&dSala de estar', 'another_furniture:white_sofa', 2,
         ['tag:another_furniture:sofas|Um sofá de qualquer cor', 'tag:another_furniture:tables|Uma mesa de qualquer madeira',
          'tag:another_furniture:lamps|Um abajur de qualquer cor'],
         'Sofá, mesa de centro e um abajur aceso. Lugar de visita, de livro e de não fazer nada.'),
        ('bedroom', '&dQuarto', 'another_furniture:white_curtain', 4,
         ['tag:another_furniture:curtains|Uma cortina de qualquer cor', 'cluttered:antique_standing_lamp', 'dustydecorations:bookstack'],
         'Cortina para a manhã chegar devagar, uma luminária antiga e a pilha de livros que você jura que vai ler.'),
        ('garden', '&dJardim e varanda', 'chimes:bamboo_chimes', 6,
         ['tag:another_furniture:flower_boxes|Uma floreira de qualquer madeira', 'tag:another_furniture:benches|Um banco de qualquer madeira',
          'chimes:bamboo_chimes'],
         'Floreira na janela, banco na sombra e um sino de vento de bambu. Os sinos do Chimes tocam com a brisa e mais forte na chuva.'),
        ('common', '&dPonto de encontro', 'another_furniture:white_stool', 8,
         ['tag:another_furniture:chairs|Uma cadeira de qualquer madeira', 'tag:another_furniture:tall_stools|Uma banqueta alta de qualquer cor',
          'cluttered:bulletin_board'],
         'Cadeiras, banquetas altas e um quadro de avisos: café, taverna, praça ou salão comunitário. Casa cheia é casa viva.'),
    ]
    for key, title, icon, x, tasks, text in rooms:
        c.q(key, 'C', title, icon, x, 2, tasks, [
            text,
            'As peças são um ponto de partida e contam por posse, em qualquer cor ou madeira. O cômodo de verdade é o que você constrói; o livro não mede beleza.',
        ])
    c.q('shutter', 'C', '&dJanela com venezianas', 'another_furniture:oak_shutter', 6, 3,
        ['tag:another_furniture:shutters|Uma veneziana de qualquer madeira'], [
        'Venezianas abrem e fecham com um clique e mudam a cara de qualquer fachada.',
        POSSE,
    ], deps=['garden'])
    c.q('chimes', 'C', '&dCoro de vento', 'chimes:amethyst_chimes', 7, 3,
        ['chimes:iron_chimes', 'chimes:copper_chimes', 'chimes:amethyst_chimes', 'chimes:glass_bells'], [
        'Cada material tem sua voz: ferro, cobre, ametista e os sininhos de vidro. Juntos, fazem a trilha sonora do jardim.',
        POSSE,
    ])
    out.append(c)

    # ------------------------------------------------------------ LR03
    c = Chapter(0x16, 'LR03', 'prateleira_de_abracos', 'LR', 2, '&e&lPrateleira de Abraços', 'perfectplushies:red_panda_plushie')
    c.q('first', 'A', '&ePrimeiro abraço', 'perfectplushies:dog_plushie', 0, 0,
        ['tag:perfectplushieapi:village_plushies|Obtenha uma pelúcia de animal'], [
        'Pelúcias do Perfect Plushies não têm receita: aparecem em baús de vilas e nas mãos de comerciantes. Colocadas no mundo, fazem um barulhinho ao serem apertadas.',
        'Qualquer pelúcia de animal conta. A coleção é para passear e trocar, não para repetir a mesma vila até cansar.',
    ])
    c.gallery('pl', sorted(village_plushies), 0, 2,
              'Uma pelúcia para a prateleira. Procure em baús de vilas e com comerciantes; trocar com outros jogadores também vale. '
              'Registrar exige apenas tê-la uma vez, sem consumo.')
    c.gallery('tr', sorted(treasure_plushies) + sorted(rare_plushies), 8, 2,
              'Raridade: pelúcias de tesouro e versões especiais aparecem em baús de estruturas e com o comerciante errante, quando aparecem. '
              'Página só para quem gosta de procurar; nada depende dela.', cols=4)
    out.append(c)

    # ------------------------------------------------------------ JE01
    c = Chapter(0x17, 'JE01', 'olhos_do_mundo', 'JE', 0, '&e&lOlhos do Mundo', 'endrem:old_eye')
    c.q('first', 'A', '&eUm olho diferente', 'endrem:old_eye', 0, 0,
        ['tag:lilyvale:endrem_eyes|Obtenha qualquer olho do End Remastered'], [
        'Em Lilyvale, olhos do End comuns não abrem o portal nem apontam fortalezas. O caminho passa pelos olhos espalhados pelo mundo: em estruturas, chefes, trocas e receitas.',
        'Cada olho encontrado é uma pista de viagem. Qualquer um deles conclui esta tarefa.',
    ])
    c.q('end', 'M', '&6&lO portal desperta', 'minecraft:end_portal_frame', 1, 0, ['dim:minecraft:the_end|Entre no End'], [
        'O portal antigo pede olhos diferentes entre si, um por moldura. Você não precisa dos dezesseis: confira no próprio portal quantos faltam.',
        'O marco detecta a chegada ao End, não a coleção. Viajar com o grupo de quem abriu o portal também vale.',
    ], deps=['first'])
    c.gallery('ey', ['endrem:' + e for e in EYES], 0, 2,
              'Um olho para a coleção. O avanço do End Remastered com o nome deste olho dá a pista de onde procurar; alguns vêm de estruturas, '
              'outros de criaturas, trocas ou receitas. Registrar exige apenas tê-lo uma vez. Completar os dezesseis é opcional.', cols=8)
    out.append(c)

    # ------------------------------------------------------------ JE02
    c = Chapter(0x18, 'JE02', 'o_ultimo_voo', 'JE', 1, '&e&lO Último Voo', 'minecraft:dragon_head')
    c.q('prep', 'A', '&eAntes de pular', 'minecraft:water_bucket', 0, 0,
        ['minecraft:water_bucket', 'minecraft:arrow*64', 'minecraft:golden_apple*2'], [
        'Com o True Ending, a dragoa tem novos ataques, fases e uma trilha sonora à altura. Não é a luta que você lembra.',
        'Kit sugerido: balde de água para as quedas, flechas para os cristais e maçãs douradas para os sustos. A tarefa só confere a mochila; ir ou não ir é decisão sua.',
    ])
    c.q('dragon', 'M', '&6&lO último voo', 'minecraft:dragon_egg', 1, 0,
        ['adv:true_ending:kill_dragon|Derrote a Ender Dragon'], [
        'O céu do End fica em silêncio. Seja qual for o seu jeito de jogar, isto é uma história para contar na volta.',
        'O marco usa o avanço do True Ending: quem já venceu não precisa repetir. O resto do livro continua aberto antes e depois deste combate.',
    ], deps=['prep'])
    c.q('breath', 'C', '&dFôlego engarrafado', 'minecraft:dragon_breath', 1, 1, ['minecraft:dragon_breath'], [
        'Recolha o sopro da dragoa em garrafas de vidro durante o combate. Serve para poções persistentes e para contar vantagem.',
        POSSE,
    ], deps=['dragon'])
    c.q('egg', 'C', '&dLembrança de viagem', 'minecraft:dragon_egg', 2, 0, ['minecraft:dragon_egg'], [
        'O ovo teleporta quando tocado. Um pistão ou uma tocha embaixo resolvem. Fica lindo sobre a lareira.',
        POSSE,
    ], deps=['dragon'])
    c.q('again', 'C', '&dDe novo?', 'minecraft:end_crystal', 2, 1,
        ['adv:true_ending:place_end_crystal_on_bedrock|Coloque um cristal do End no portal de saída'], [
        'Quatro cristais em volta do portal de saída chamam a dragoa de volta. Para quem achou pouco.',
        'A tarefa detecta um cristal colocado sobre a rocha-mãe.',
    ], deps=['egg'])
    out.append(c)

    # ------------------------------------------------------------ JE03
    c = Chapter(0x19, 'JE03', 'ilhas_do_vazio', 'JE', 2, '&e&lIlhas do Vazio', 'minecraft:chorus_flower')
    c.q('gate', 'A', '&ePortal de passagem', 'minecraft:ender_pearl', 0, 0,
        ['adv:minecraft:end/enter_end_gateway|Atravesse um portal de passagem do End'], [
        'Os portais de passagem levam às ilhas externas. Jogue uma pérola do Ender dentro dele para atravessar.',
        'O Endercon redesenha o End: ilhas maiores, cavernas, pilares e ruínas. A tarefa detecta a travessia.',
    ])
    c.q('hallows', 'C', '&dCampos pálidos', 'minecraft:end_stone', 1, 0,
        ['biome:endercon:end_hallows|Visite os End Hallows'], [
        'Os Hallows são as terras altas do novo End: pilares, lâmpadas pendentes e um silêncio comprido.',
        'A tarefa detecta a visita ao bioma.',
    ])
    c.q('border', 'C', '&dA borda do mapa', 'minecraft:purpur_block', 2, 0,
        ['biome:endercon:end_border|Visite a fronteira do End'], [
        'Na fronteira, as ilhas se desfazem em pedaços sobre o nada. Leve blocos, pérolas e cuidado.',
        'A tarefa detecta a visita ao bioma.',
    ])
    c.q('ruins', 'C', '&dRuínas de quem veio antes', 'minecraft:end_stone_bricks', 3, 0,
        ['struct:endercon:end_ruins|Encontre ruínas do End'], [
        'Ruínas espalhadas pelas ilhas guardam barris com suprimentos de outros viajantes.',
        'A tarefa detecta a chegada à estrutura.',
    ])
    c.q('city', 'C', '&dCidade nas alturas', 'minecraft:purpur_pillar', 4, 0,
        ['struct:minecraft:end_city|Encontre uma cidade do End'], [
        'Torres roxas, shulkers nas paredes e, com sorte, um navio ancorado no ar.',
        'A tarefa detecta a chegada à estrutura.',
    ])
    c.q('elytra', 'C', '&dAsas próprias', 'minecraft:elytra', 4, 1, ['minecraft:elytra'], [
        'A élitra espera no navio do End. Depois dela, o mundo inteiro fica a um salto de distância.',
        POSSE,
    ], deps=['city'])
    c.q('shulker', 'C', '&dCaixa que viaja', 'minecraft:shulker_box', 3, 1, ['minecraft:shulker_shell*2'], [
        'Duas cascas e um baú fazem uma caixa de shulker, que guarda o conteúdo ao ser quebrada.',
        'A tarefa pede as duas cascas.',
    ])
    c.q('chorus', 'C', '&dPomar do vazio', 'minecraft:chorus_flower', 1, 1,
        ['minecraft:chorus_flower', 'minecraft:end_stone*16'], [
        'Flores de coro crescem em pedra do End em qualquer dimensão. Leve as duas para casa e plante um pomar esquisito.',
        'Projeto sugerido: uma ponte entre ilhas ou um observatório sobre o vazio. O livro não mede a obra; a vista é a recompensa.',
    ])
    out.append(c)
    return out
