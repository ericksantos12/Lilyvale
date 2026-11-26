# -*- coding: utf-8 -*-
"""Primeiros Dias (PD04) e Vida no Campo (VC01, VC06). VC02–VC05 e VC07 ficam em chapters_farm.py."""
from core import Chapter
import chapters_tide

POSSE = 'A tarefa registra posse, sem consumir: troca e presente também valem.'


def build():
    out = []

    # ------------------------------------------------------------ PD04
    c = Chapter(0x01, 'PD04', 'tips_and_tricks', 'PD', 3, '&6&lTips & Tricks', 'vc_gliders:paraglider_wood')
    c.q('glider', 'A', '&6Asas de pano', 'vc_gliders:paraglider_wood', 0, 0, ['vc_gliders:paraglider_wood'], [
        'Um planador de madeira transforma qualquer morro em atalho. Equipe-o, salte e segure o pulo para abrir as asas.',
        'Ele plana, não sobe: escolha um ponto alto e poupe a durabilidade. A receita está no EMI. ' + POSSE,
    ])
    c.q('glider2', 'C', '&dVento mais firme', 'vc_gliders:paraglider_iron', 0, 2, ['vc_gliders:paraglider_iron'], [
        'O planador de ferro aguenta voos mais longos. Há melhorias de cobre e do Nether para quem quiser brincar com correntes de ar e calor.',
        'Sugestão de passeio: saltar do ponto mais alto da sua base e pousar na horta sem amassar nada. Só o planador é detectado.',
    ], deps=['glider'])
    c.q('camera', 'A', '&6Diga xis', 'camerapture:camera', 1, 0, ['camerapture:camera'], [
        'A câmera do Camerapture tira fotos de verdade do seu mundo. Leve papel no inventário: cada clique gasta uma folha.',
        'As fotos podem ir para molduras ou para um álbum. ' + POSSE,
    ])
    c.q('photo', 'C', '&dPrimeira revelação', 'camerapture:picture', 1, 2, ['camerapture:picture', 'camerapture:album'], [
        'Uma foto revelada e um álbum para guardá-la. Fotografe a casa, a colheita, o trem ou aquele pôr do sol que ninguém acreditou.',
        'Qualquer foto serve; o livro não avalia enquadramento. Ainda bem.',
    ], deps=['camera'])
    c.q('bag', 'A', '&6Dormir sem voltar pra casa', 'comforts:sleeping_bag_white', 2, 0,
        ['tag:comforts:sleeping_bags|Obtenha um saco de dormir de qualquer cor'], [
        'O saco de dormir pula a noite sem mudar seu ponto de renascimento. Perfeito para expedições longas.',
        'Qualquer cor vale. Ele se desgasta com o uso; confira a receita no EMI.',
    ])
    c.q('hammock', 'C', '&dSoneca da tarde', 'comforts:hammock_white', 2, 2,
        ['tag:comforts:hammocks|Obtenha uma rede de qualquer cor', 'comforts:rope_and_nail*2'], [
        'A rede serve para dormir de dia e acordar à noite. Prenda duas cordas com prego em blocos frente a frente e pendure a rede entre elas.',
        'A tarefa pede a rede e as duas cordas; montar e cochilar ficam por sua conta.',
    ], deps=['bag'])
    c.q('compass', 'A', '&6Para que lado fica?', 'naturescompass:naturescompass', 3, 0, ['naturescompass:naturescompass'], [
        'A Bússola da Natureza procura biomas pelo nome. Clique com o botão direito, escolha o destino e siga a agulha.',
        'Combina bem com o Atlas de Descobertas, mas nenhum bioma é obrigatório. ' + POSSE,
    ])
    c.q('carry', 'A', '&6Mãos à obra', 'minecraft:chest', 4, 0, ['check:|Li a dica do Carry On'], [
        'Com as duas mãos vazias, agache e clique com o botão direito em um baú, barril ou animal pequeno para carregá-lo no colo, com todo o conteúdo.',
        'Você anda mais devagar enquanto carrega e alguns blocos e criaturas são bloqueados pela configuração do pack. Solte com o botão direito no chão.',
        'Este cartão é só leitura: não há item para detectar, então o check é uma confirmação manual, sem recompensa.',
    ], sub='&7Dica de leitura', xp=0, optional=True)
    c.q('chipped', 'A', '&6Mil caras para cada bloco', 'chipped:carpenters_table', 5, 0, ['chipped:carpenters_table'], [
        'O Chipped traz sete bancadas que trocam um bloco por variantes decorativas do mesmo material: tábuas entalhadas, '
        'pedras lavradas, vidros desenhados. Coloque os blocos na bancada, escolha o visual e retire; a troca é de um para um '
        'e dá para voltar ao original na mesma bancada.',
        'A Mesa de Carpinteiro (Carpenters Table) cuida da madeira: tábuas, troncos e afins. Comece por ela; as receitas de todas '
        'estão no EMI. ' + POSSE,
    ])
    c.q('chipped2', 'C', '&dAteliê completo', 'chipped:mason_table', 5, 2, [
        'chipped:carpenters_table', 'chipped:mason_table', 'chipped:glassblower', 'chipped:loom_table',
        'chipped:botanist_workbench', 'chipped:alchemy_bench', 'chipped:tinkering_table'], [
        'Cada bancada cuida de uma família de blocos:',
        '&6Mesa de Pedreiro&r (Mason Table): pedras, tijolos e rochas.',
        '&6Soprador de Vidro&r (Glassblower): vidros e painéis, de todas as cores.',
        '&6Mesa de Tear&r (Loom Table): lãs e tapetes.',
        '&6Bancada do Botânico&r (Botanist Workbench): terra, areia, gelo, folhas, cogumelos, abóboras e outros blocos naturais.',
        '&6Bancada de Alquimia&r (Alchemy Bench): blocos de minério, ametista, pedra luminosa, cobre encerado e outros especiais.',
        '&6Mesa de Funileiro&r (Tinkering Table): lanternas, grades de ferro e blocos de redstone.',
        'Uma oficina com as sete transforma qualquer obra. ' + POSSE,
    ], deps=['chipped'])
    # Mural (primeiros_dias_art.py): bilhete com o título preso por alfinete e polaroides das dicas.
    for img, x, y, h, dica in (('mural_titulo', 2.5, -1.6, 1.5, ['&6&lTips & Tricks', 'Pequenos truques para o dia a dia']),
                               ('polaroide_planador', 0.4, 3.8, 1.5, ['Voe de morro em morro']),
                               ('polaroide_camera', 1.85, 3.85, 1.5, ['Fotografe o vale e revele as fotos']),
                               ('polaroide_bussola', 3.3, 3.8, 1.5, ['Ache o bioma certo']),
                               ('polaroide_chipped', 4.75, 3.85, 1.5, ['Dê outra cara ao bloco'])):
        c.image('lilyvale:textures/quests/primeiros_dias/%s.png' % img, x, y, None, h, dica)
    out.append(c)

    # ------------------------------------------------------------ VC01
    c = Chapter(0x02, 'VC01', 'caderno_de_receitas', 'VC', 0, '&a&lCaderno de Receitas', 'farmersdelight:cooking_pot')
    c.q('knife', 'A', '&aFaca na mão', 'farmersdelight:flint_knife', 0, 0,
        ['adv:farmersdelight:main/craft_knife|Obtenha uma faca de qualquer material'], [
        'A faca do Farmer\'s Delight colhe palha do capim, corta bolos e é a ferramenta da tábua de corte. A de pederneira já resolve.',
        'Qualquer faca conta. O livro registra a posse, não quem a afiou.',
    ])
    c.q('board', 'A', '&aTábua de corte', 'farmersdelight:cutting_board', 1, 0,
        ['adv:farmersdelight:main/use_cutting_board|Corte algo na tábua de corte'], [
        'Coloque um ingrediente na tábua e clique com a faca. Carnes viram cortes, repolhos viram folhas e troncos podem ser descascados com machado.',
        'Aqui a tarefa detecta o corte de verdade. O EMI mostra o que cada ferramenta faz na tábua.',
    ], deps=['knife'])
    c.q('pot', 'A', '&aPanela no fogo', 'farmersdelight:cooking_pot', 2, 0,
        ['adv:farmersdelight:main/place_cooking_pot|Coloque uma panela de cozinha'], [
        'A panela precisa de calor por baixo: fogão, fogueira ou magma. Junte os ingredientes, o recipiente pedido pela receita (tigela, garrafa...) e espere.',
        'A tarefa detecta a panela colocada no mundo. O fogão do Farmer\'s Delight também assa direto na chapa.',
    ])
    c.q('skillet', 'A', '&aFrigideira de respeito', 'farmersdelight:skillet', 3, 0, ['farmersdelight:skillet'], [
        'A frigideira frita no chão sobre uma fonte de calor ou na mão, perto do fogo. Também é uma arma surpreendentemente convincente.',
        POSSE,
    ])
    c.q('nourish', 'M', '&6&lBarriga cheia, dia ganho', 'farmersdelight:beef_stew', 2, 1,
        ['adv:farmersdelight:main/eat_nourishing_food|Receba o efeito Nutrição de uma refeição'], [
        'Refeições completas dão Nutrição: a fome para de cair por um tempo. É o jeito do campo de dizer que você comeu direito.',
        'O marco detecta o efeito, então alguém precisa mesmo sentar e comer. Quem cozinhou é assunto da mesa.',
    ], deps=['pot'])
    c.q('feast', 'C', '&dMesa posta', 'farmersdelight:roast_chicken_block', 2, 2,
        ['adv:farmersdelight:main/place_feast|Sirva um banquete na mesa'], [
        'Banquetes são pratos grandes colocados como bloco e servidos em porções: frango assado, presunto glaceado, abóbora recheada, torta do pastor...',
        'A tarefa detecta qualquer banquete colocado. Convidar os vizinhos é opcional, mas recomendado.',
    ], deps=['nourish'])
    c.q('soil', 'C', '&dTerra que devolve', 'farmersdelight:rich_soil', 0, 2,
        ['adv:farmersdelight:main/place_organic_compost|Coloque composto orgânico', 'farmersdelight:rich_soil'], [
        'O composto orgânico amadurece sozinho até virar solo rico, mais rápido com água e cogumelos por perto. Plantas crescem melhor nele.',
        'São duas tarefas: colocar o composto e ter um bloco de solo rico.',
    ])
    c.q('veggies', 'C', '&dHorta sortida', 'veggiesdelight:bellpepper', 4, 2,
        ['adv:veggiesdelight:main/r_all_veggies|Tenha todos os vegetais do Veggies Delight'], [
        'Pimentão, brócolis, couve-flor, alho, batata-doce, nabo, abobrinha e companhia nascem selvagens pelo mundo. Colha, replante e varie o cardápio.',
        'Este desafio usa o avanço do próprio mod, que pede um exemplar de cada vegetal no inventário ao longo do tempo.',
    ])
    c.q('kettle', 'A', '&aChaleira no fogo', 'farmersrespite:kettle', 5, 0, ['farmersrespite:kettle'], [
        'A chaleira do Farmer\'s Respite prepara chás e café. Como a panela, precisa de calor por baixo e de água dentro.',
        POSSE,
    ])
    c.q('leaves', 'A', '&aFolhas no ponto', 'farmersrespite:green_tea_leaves', 5, 1,
        ['farmersrespite:green_tea_leaves', 'farmersrespite:coffee_beans'], [
        'Arbustos de chá e de café crescem selvagens. As folhas verdes podem secar e escurecer; os grãos de café pedem torra.',
        'A tarefa registra folhas de chá verde e grãos de café. As infusões em si ficam no álbum abaixo.',
    ], deps=['kettle'])
    c.q('jar', 'A', '&aPote de fermentar', 'vintagedelight:fermenting_jar', 7, 0,
        ['adv:vintagedelight:main/place_fermenting_jar|Coloque um pote de fermentação'], [
        'O Vintage Delight guarda a colheita em conserva. O pote de fermentação transforma ingredientes com tempo e paciência, sem fogo.',
        'A tarefa detecta o pote colocado. As receitas e os tempos estão no EMI.',
    ])
    c.q('pickle', 'M', '&6&lDespensa viva', 'vintagedelight:pickled_onion', 7, 1,
        ['adv:vintagedelight:main/pickled_item|Obtenha uma conserva em picles'], [
        'Uma despensa com conservas atravessa qualquer inverno. Beterraba, cebola, ovo, pimenta: escolha a sua.',
        'Qualquer conserva em picles conta; o avanço do mod aceita alternativas.',
    ], deps=['jar'])
    c.q('evap', 'A', '&aSal da casa', 'vintagedelight:evaporator', 8, 0,
        ['adv:vintagedelight:main/evaporator|Coloque um evaporador', 'vintagedelight:salt_dust'], [
        'O evaporador tira sal da água; o minério de sal também aparece em cavernas. Sal é a base de queijos curados e conservas.',
        'São duas tarefas: o evaporador colocado e um punhado de sal.',
    ])
    fd = ('Uma página do caderno. Registrar exige apenas ter o prato uma vez; nada é consumido, e receber de alguém também vale. '
          'A receita está no EMI.')
    c.gallery('fd', [
        'farmersdelight:bacon_and_eggs', 'farmersdelight:bacon_sandwich', 'farmersdelight:baked_cod_stew',
        'farmersdelight:barbecue_stick', 'farmersdelight:beef_stew', 'farmersdelight:bone_broth',
        'farmersdelight:cabbage_rolls', 'farmersdelight:chicken_sandwich', 'farmersdelight:chicken_soup',
        'farmersdelight:cod_roll', 'farmersdelight:dumplings', 'farmersdelight:egg_sandwich',
        'farmersdelight:fish_stew', 'farmersdelight:fried_rice', 'farmersdelight:fruit_salad',
        'farmersdelight:grilled_salmon', 'farmersdelight:hamburger', 'farmersdelight:honey_glazed_ham',
        'farmersdelight:kelp_roll', 'farmersdelight:mixed_salad', 'farmersdelight:mushroom_rice',
        'farmersdelight:mutton_wrap', 'farmersdelight:nether_salad', 'farmersdelight:noodle_soup',
        'farmersdelight:onion_soup', 'farmersdelight:pasta_with_meatballs', 'farmersdelight:pasta_with_mutton_chop',
        'farmersdelight:pumpkin_soup', 'farmersdelight:ratatouille', 'farmersdelight:roast_chicken',
        'farmersdelight:roasted_mutton_chops', 'farmersdelight:salmon_roll', 'farmersdelight:shepherds_pie',
        'farmersdelight:squid_ink_pasta', 'farmersdelight:steak_and_potatoes', 'farmersdelight:stuffed_potato',
    ], 0, 4, fd)
    c.gallery('ex', [
        'farmersdelight:apple_pie', 'farmersdelight:chocolate_pie', 'farmersdelight:sweet_berry_cheesecake',
        'farmersdelight:glow_berry_custard', 'farmersdelight:hot_cocoa', 'farmersdelight:apple_cider',
        'farmersrespite:green_tea', 'farmersrespite:black_tea', 'farmersrespite:coffee',
        'farmersrespite:rose_hip_tea', 'farmersrespite:coffee_cake', 'farmersrespite:rose_hip_pie',
        'farmersrespite:tea_curry', 'farmersrespite:blazing_chili',
        'oceansdelight:seagrass_salad', 'oceansdelight:squid_rings', 'oceansdelight:honey_fried_kelp',
        'oceansdelight:braised_sea_pickle', 'oceansdelight:fugu_roll', 'oceansdelight:bowl_of_guardian_soup',
        'veggiesdelight:cacciatore', 'veggiesdelight:broccoli_soup', 'veggiesdelight:cauliflower_kuku',
        'veggiesdelight:garlic_bread', 'veggiesdelight:sweet_potato_pancakes', 'veggiesdelight:turnip_beef_stew',
        'veggiesdelight:stuffed_zucchini_boat', 'veggiesdelight:vegetarian_burger',
        'vintagedelight:kimchi', 'vintagedelight:pickle', 'vintagedelight:century_egg',
        'vintagedelight:pad_thai', 'vintagedelight:stuffed_burrito', 'vintagedelight:overnight_oats',
        'vintagedelight:cheese_pasta', 'vintagedelight:surstromming',
    ], 8, 4, 'Doces, infusões, pratos do mar, da horta e da despensa. Registrar exige apenas ter o item uma vez; nada é consumido. '
             'Consulte a receita e a estação de preparo no EMI.')
    out.append(c)

    # ------------------------------------------------------------ VC06
    c = Chapter(0x07, 'VC06', 'a_beira_dagua', 'VC', 5, '&a&lÀ Beira d\'Água', 'tide:fishing_journal')
    c.q('rod', 'A', '&aLinha na água', 'minecraft:fishing_rod', 0, 0, ['adv:tide:root|Obtenha uma vara de pesca'], [
        'Com o Tide, cada rio, lago, caverna e oceano tem seus próprios peixes, e clima, hora e profundidade mudam o que morde.',
        'Qualquer vara de pesca serve para começar.',
    ])
    c.q('fish', 'M', '&6&lFisgou!', 'minecraft:cod', 0, 1,
        ['adv:minecraft:husbandry/fishy_business|Pesque um peixe'], [
        'O primeiro peixe do dia. Daqui em diante é paciência, isca e conversa fiada na beira d\'água.',
        'O marco detecta a fisgada de verdade.',
    ], deps=['rod'])
    c.q('bait', 'A', '&aIsca boa', 'tide:bait', 1, 0, ['adv:tide:get_bait|Obtenha uma isca'], [
        'Iscas aceleram a fisgada e algumas atraem peixes específicos. Elas vão no compartimento da vara, pela mesa de pesca.',
        'Qualquer isca do Tide conta.',
    ], deps=['rod'])
    c.q('journal', 'A', '&aDiário de pesca', 'tide:fishing_journal', 2, 0, ['tide:fishing_journal'], [
        'O diário do Tide registra cada espécie, onde vive e do que gosta. A grade abaixo resume o que cada peixe pede; o diário guarda os recordes.',
        POSSE,
    ])
    c.q('half', 'M', '&6&lMeio diário', 'tide:fishing_journal', 2, 1,
        ['adv:tide:journal_halfway_completed|Complete metade do diário de pesca'], [
        'Metade das espécies registradas. Você já sabe ler a água melhor que muita gaivota.',
        'O marco usa o avanço do próprio Tide.',
    ], deps=['journal'])
    c.q('full', 'C', '&dDiário completo', 'tide:fishing_journal', 2, 2,
        ['adv:tide:journal_completed|Complete o diário de pesca'], [
        'Todas as espécies, de todos os lugares. Um projeto para muitas estações, sem pressa nenhuma.',
        'Usa o avanço do próprio Tide. Nada no livro depende disso.',
    ], deps=['half'], xp=150)
    c.q('table', 'A', '&aMesa de pesca', 'tide:angling_table', 3, 0, ['tide:angling_table'], [
        'Na mesa de pesca você troca linha, anzol e boia da vara e guarda iscas nela.',
        POSSE,
    ])
    c.q('tackle', 'A', '&aLinha e anzol', 'tide:fishing_hook', 4, 0, ['tide:fishing_line', 'tide:fishing_hook'], [
        'Linhas e anzóis mudam o comportamento da vara: mais sorte, mais alcance, resistência a lava. Boias são só charme, e charme conta.',
        'A tarefa pede uma linha e um anzol básicos.',
    ], deps=['table'])
    c.q('crate', 'C', '&dTesouro encharcado', 'tide:wooden_crate', 0, 3, ['adv:tide:pull_crate|Pesque um caixote'], [
        'Às vezes o que vem na linha não é peixe. Caixotes trazem materiais e surpresas do fundo.',
        'A tarefa detecta o caixote fisgado.',
    ])
    c.q('legend', 'C', '&dHistória de pescador', 'tide:coelacanth', 1, 3,
        ['adv:tide:catch_legendary|Pesque um peixe lendário'], [
        'Peixes lendários existem, por mais que ninguém acredite na sua história. O diário dá pistas de onde e quando.',
        'A tarefa detecta a fisgada de qualquer lendário.',
    ])
    c.q('displayf', 'C', '&dTroféu na parede', 'tide:fish_display', 2, 3, ['tide:fish_display'], [
        'Um expositor para pendurar a melhor pescaria na parede da sala. Tamanho do peixe a critério do narrador.',
        POSSE,
    ])
    c.q('lava', 'C', '&dPescaria quente', 'tide:lavaproof_hook', 4, 3, ['adv:tide:fish_in_lava|Pesque na lava'], [
        'Com o equipamento certo dá para pescar em lava. Os peixes de lá são exatamente tão esquisitos quanto você imagina.',
        'Especialização opcional: envolve o Nether e anzol à prova de lava.',
    ])
    c.q('void', 'C', '&dLinha no nada', 'tide:void_hook', 5, 3, ['adv:tide:fish_in_void|Pesque no vazio'], [
        'Pescar no vazio do End é para quem já pescou em todo o resto. Segure-se bem na borda.',
        'Especialização opcional: exige chegar ao End.',
    ])
    # A progressão fica no centro, entre os peixes em 3D; a grade de espécies vem abaixo.
    for q in c.quests:
        q['x'] += 14.0
    P = chapters_tide.ARTE
    c.image(P + 'titulo.png', 9.5, -2.6, None, 3.2, ['&b&lÀ Beira d\'Água', 'Uma quest para cada peixe do Tide'])
    for img, x, y, h, nome in (('coelacanth', 3.0, 1.5, 3.6, 'Coelacanth'), ('great_white_shark', 16.0, 1.5, 3.6, 'Great White Shark'),
                               ('sailfish', -2.6, 8.0, 4.0, 'Sailfish'), ('manta_ray', 21.6, 8.0, 3.6, 'Manta Ray'),
                               ('blazing_swordfish', 2.5, 17.6, 3.4, 'Blazing Swordfish'),
                               ('shadow_shark', 9.5, 17.6, 3.4, 'Shadow Shark'), ('dragon_fish', 16.5, 17.6, 3.4, 'Dragon Fish')):
        c.image(P + 'peixe_%s.png' % img, x, y, None, h, [nome])
    falta = chapters_tide.build(c)
    assert not falta, 'peixes do Tide fora da grade: %s' % ', '.join(falta)
    out.append(c)
    return out
