# -*- coding: utf-8 -*-
"""Primeiros Dias (PD04) e Vida no Campo (VC01–VC06)."""
from core import Chapter

POSSE = 'A tarefa registra posse, sem consumir: troca e presente também valem.'


def build():
    out = []

    # ------------------------------------------------------------ PD04
    c = Chapter(0x01, 'PD04', 'tips_and_tricks', 'PD', 2, '&6&lTips & Tricks', 'vc_gliders:paraglider_wood')
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

    # ------------------------------------------------------------ VC02
    c = Chapter(0x03, 'VC02', 'rotina_da_fazenda', 'VC', 1, '&a&lRotina da Fazenda', 'farm_and_charm:pitchfork')
    c.q('fert', 'A', '&aNada se perde', 'farm_and_charm:fertilizer', 0, 0,
        ['adv:farm_and_charm:main/get_fertilizer|Obtenha fertilizante'], [
        'Restos de colheita viram composto, e o composto vira fertilizante. É o começo do ciclo do Farm & Charm.',
        'O EMI mostra o que pode ser compostado. ' + POSSE,
    ])
    c.q('fsoil', 'A', '&aTerra adubada', 'farm_and_charm:fertilized_soil', 1, 0,
        ['adv:farm_and_charm:main/place_fertilized_soil|Coloque um bloco de solo fertilizado'], [
        'O solo fertilizado é um canteiro de luxo. Coloque-o onde a horta vai ficar; o forcado espalha e recolhe o adubo.',
        'A tarefa detecta o bloco colocado no mundo.',
    ], deps=['fert'])
    c.q('hoe', 'A', '&aCanteiro pronto', 'minecraft:iron_hoe', 2, 0,
        ['adv:farm_and_charm:main/use_hoe_on_fertilized_soil|Are o solo fertilizado com uma enxada'], [
        'Passe a enxada no solo fertilizado para criar terra arada adubada: as plantas crescem mais rápido e a terra não seca com pisões.',
        'Dica do Harvest with Ease: clique com o botão direito em uma planta madura para colher e replantar de uma vez. Com enxada na mão, a colheita pode alcançar uma área maior.',
    ], deps=['fsoil'])
    c.q('sprinkler', 'A', '&aChuva particular', 'farm_and_charm:water_sprinkler', 1, 1,
        ['adv:farm_and_charm:main/place_water_sprinkler|Coloque um regador giratório'], [
        'O regador giratório mantém os canteiros úmidos ao redor sem precisar de valas de água no meio da horta.',
        'A tarefa detecta o regador colocado.',
    ], deps=['fsoil'])
    c.q('harvest', 'C', '&dCeleiro cheio', 'minecraft:wheat', 0, 1,
        ['minecraft:wheat*32', 'minecraft:carrot*16', 'minecraft:potato*16'], [
        'Uma colheita de respeito para estrear o clique direito do Harvest with Ease: trigo, cenoura e batata sem replantar à mão.',
        'A tarefa só confere os itens no inventário. Como eles chegaram lá é entre você e a horta.',
    ])
    c.q('bowl', 'A', '&aMassa na tigela', 'farm_and_charm:crafting_bowl', 4, 0,
        ['farm_and_charm:crafting_bowl', 'farm_and_charm:flour'], [
        'A tigela de preparo mistura farinha, água e fermento com algumas mexidas. A farinha vem de grãos moídos.',
        'Neste pack as massas dos mods de cozinha foram unificadas; confira no EMI qual massa cada receita aceita.',
    ])
    c.q('mincer', 'A', '&aGira a manivela', 'farm_and_charm:mincer', 5, 0,
        ['adv:farm_and_charm:main/introduction_mincing|Use o moedor'], [
        'O moedor transforma carne em carne moída e grãos em farinha. Coloque o ingrediente e gire a manivela com cliques.',
        'A tarefa detecta o uso do moedor, não só a posse.',
    ])
    c.q('silo', 'A', '&aSecar e guardar', 'farm_and_charm:silo_wood', 6, 0,
        ['adv:farm_and_charm:main/introduction_drying|Coloque algo para secar no silo'], [
        'O silo seca grãos e ervas. Empilhe blocos de silo para aumentar a capacidade e retire o produto seco por baixo.',
        'A tarefa detecta o uso do silo.',
    ])
    c.q('kitchen', 'M', '&6&lCozinha da fazenda', 'farm_and_charm:stove', 5, 1, [
        'adv:farm_and_charm:main/place_stove|Coloque um fogão de fazenda',
        'adv:farm_and_charm:main/place_cooking_pot|Coloque uma panela',
        'adv:farm_and_charm:main/place_roaster|Coloque uma assadeira',
    ], [
        'Fogão, panela e assadeira: com as três peças no lugar, a cozinha da fazenda dá conta de pães, sopas e assados.',
        'O marco detecta os três blocos colocados no mundo. Onde fica a mesa é decisão sua.',
    ])
    c.q('coop', 'A', '&aCasa das galinhas', 'farm_and_charm:chicken_coop', 8, 0,
        ['adv:farm_and_charm:main/place_chicken_coop|Coloque um galinheiro'], [
        'O galinheiro abriga as galinhas e junta os ovos num lugar só. Elas entram sozinhas ao anoitecer se estiverem por perto.',
        'A tarefa detecta o galinheiro colocado.',
    ])
    c.q('nest', 'A', '&aNinho arrumado', 'farm_and_charm:chicken_nest', 9, 0,
        ['adv:farm_and_charm:main/place_chicken_nest|Coloque um ninho'], [
        'Ninhos dão às galinhas um lugar para botar. Menos ovos perdidos pelo pasto, mais omeletes.',
        'A tarefa detecta o ninho colocado.',
    ], deps=['coop'])
    c.q('trough', 'A', '&aHora da ração', 'farm_and_charm:feeding_trough', 10, 0,
        ['adv:farm_and_charm:main/place_feeding_trough|Coloque um cocho'], [
        'O cocho alimenta os animais próximos com o que você deixar dentro. Bom para manter a criação sem correr atrás de cada bicho.',
        'A tarefa detecta o cocho colocado.',
    ])
    c.q('yard', 'M', '&6&lCriação em ordem', 'minecraft:egg', 8, 1,
        ['farm_and_charm:chicken_feed', 'minecraft:egg*16'], [
        'Galinheiro montado, ração no cocho e ovos chegando. A criação agora se cuida entre uma visita e outra.',
        'O marco pede ração de galinha e dezesseis ovos. Ele confere a posse, não conta cada ovo no ninho.',
    ], deps=['coop'])
    c.q('scare', 'C', '&dGuardião de palha', 'farm_and_charm:scarecrow', 0, 3, ['farm_and_charm:scarecrow'], [
        'Um espantalho dá personalidade à plantação. Os corvos de Lilyvale são imaginários, mas ele não sabe disso.',
        POSSE,
    ])
    c.q('rack', 'C', '&dCada ferramenta no lugar', 'farm_and_charm:tool_rack', 1, 3,
        ['farm_and_charm:tool_rack', 'farm_and_charm:window_sill'], [
        'Um suporte de ferramentas na parede do celeiro e um peitoril florido na janela. Fazenda também é capricho.',
        POSSE,
    ])
    c.gallery('fc', [
        'farm_and_charm:simple_tomato_soup', 'farm_and_charm:barley_soup', 'farm_and_charm:onion_soup',
        'farm_and_charm:potato_soup', 'farm_and_charm:goulash', 'farm_and_charm:corn_grits',
        'farm_and_charm:farmer_salad', 'farm_and_charm:pasta_with_onion_sauce', 'farm_and_charm:oatmeal_with_strawberries',
        'farm_and_charm:bacon_with_eggs', 'farm_and_charm:beef_patty_with_vegetables', 'farm_and_charm:barley_patties_with_potatoes',
        'farm_and_charm:sausage_with_oat_patty', 'farm_and_charm:lamb_with_corn', 'farm_and_charm:chicken_wrapped_in_bacon',
        'farm_and_charm:roasted_corn', 'farm_and_charm:potato_with_roast_meat', 'farm_and_charm:baked_lamb_ham',
        'farm_and_charm:stuffed_chicken', 'farm_and_charm:stuffed_rabbit', 'farm_and_charm:farmers_bread',
        'farm_and_charm:farmers_breakfast', 'farm_and_charm:oat_pancake', 'farm_and_charm:grandmothers_strawberry_cake',
    ], 0, 5, 'Um prato da roça. Panela, assadeira e fogão dividem as receitas; o EMI mostra qual estação usar. '
             'Registrar exige apenas ter o prato uma vez, sem consumo.')
    out.append(c)

    # ------------------------------------------------------------ VC03
    c = Chapter(0x04, 'VC03', 'sabores_do_prado', 'VC', 2, '&a&lSabores do Prado', 'meadow:cheese_block')
    c.q('bucket', 'A', '&aBalde de madeira', 'meadow:wooden_bucket', 0, 0, ['meadow:wooden_bucket'], [
        'No prado alpino até o balde é de madeira. Ele serve para água e, principalmente, para ordenhar.',
        POSSE,
    ])
    c.q('milk', 'A', '&aLeite fresco', 'meadow:wooden_milk_bucket', 1, 0, ['meadow:wooden_milk_bucket'], [
        'Ordenhe uma vaca com o balde de madeira. Ovelhas, cabras e búfalos-d\'água dão leites diferentes, e cada leite vira um queijo próprio.',
        'A tarefa pede leite de vaca no balde de madeira; os outros leites ficam para a coleção de queijos.',
    ], deps=['bucket'])
    c.q('rennet', 'A', '&aO segredo do coalho', 'meadow:rennet', 2, 0, ['adv:meadow:main/get_rennet|Obtenha coalho'], [
        'Sem coalho o leite não vira queijo. A receita está no EMI; guarde um pouco para as próximas levas.',
        POSSE,
    ], deps=['milk'])
    c.q('cauldron', 'A', '&aCaldeirão do queijeiro', 'meadow:cooking_cauldron', 3, 0, ['meadow:cooking_cauldron'], [
        'O caldeirão de cozinha aquece leite e coalho até formar a massa do queijo. Ele precisa de fogo por baixo.',
        'O mesmo caldeirão prepara outros pratos alpinos. ' + POSSE,
    ], deps=['rennet'])
    c.q('form', 'A', '&aNa forma', 'meadow:cheese_form', 4, 0,
        ['adv:meadow:main/place_cheese_form|Coloque uma forma de queijo'], [
        'A massa vai para a forma e descansa até virar uma roda de queijo. Uma prateleira de cura por perto deixa a queijaria com cara de queijaria.',
        'A tarefa detecta a forma colocada.',
    ], deps=['cauldron'])
    c.q('cheese', 'M', '&6&lPrimeira roda', 'meadow:cheese_block', 4, 1,
        ['adv:meadow:main/get_cheese|Obtenha uma roda de queijo de qualquer tipo'], [
        'Do pasto à forma: sua primeira roda de queijo. Corte em pedaços para comer ou sirva inteira na mesa.',
        'Qualquer queijo conta. O marco registra a roda nas suas mãos; a ordenha fica na memória.',
    ], deps=['form'])
    c.q('salt', 'C', '&dSal dos Alpes', 'meadow:alpine_salt', 0, 2, ['adv:meadow:main/get_salt|Obtenha sal alpino'], [
        'O minério de sal alpino aparece nas rochas das montanhas. Tempera pratos do prado e conserva carnes.',
        POSSE,
    ])
    c.q('wood', 'C', '&dLenha empilhada', 'meadow:woodcutter', 1, 2,
        ['adv:meadow:main/place_woodcutter|Coloque um cortador de lenha'], [
        'O cortador de lenha transforma troncos em vigas, bancos e peças de chalé com menos desperdício.',
        'A tarefa detecta o bloco colocado.',
    ])
    c.q('fondue', 'C', '&dNoite de fondue', 'meadow:fondue', 2, 2, ['adv:meadow:main/place_fondue|Coloque um fondue'], [
        'Queijo derretido, pão e gente em volta. O fondue vai na mesa como bloco e serve várias porções.',
        'A tarefa detecta o fondue colocado.',
    ], deps=[])
    c.q('bed', 'C', '&dCama de palha', 'meadow:straw_bed', 3, 2, ['adv:meadow:main/place_straw_bed|Coloque uma cama de palha'], [
        'Simples, quente e com cheiro de feno. A cama de palha combina com cabanas de pastor e sótãos de celeiro.',
        'A tarefa detecta a cama colocada.',
    ])
    c.q('fur', 'C', '&dAgasalho de montanha', 'meadow:fur_chestplate', 4, 2, ['adv:meadow:main/fur_armor|Tenha o conjunto de pele completo'], [
        'O conjunto de pele protege do frio das alturas. Quatro peças, um visual de pastor experiente.',
        'O avanço do mod pede as quatro peças no inventário.',
    ])
    c.q('buffalo', 'C', '&dDe longe, com respeito', 'minecraft:spyglass', 6, 0,
        ['adv:meadow:main/spyglass_at_buffalo|Observe um búfalo-d\'água pela luneta'], [
        'Búfalos-d\'água vivem perto de rios e pântanos. Aponte a luneta para um deles sem incomodar.',
        'A tarefa detecta a observação pela luneta. Ninguém precisa se machucar.',
    ])
    c.q('meadow', 'C', '&dAr de montanha', 'meadow:alpine_poppy', 6, 1, ['adv:meadow:main/find_meadow|Visite um prado'], [
        'Prados de montanha são a casa das flores alpinas, das vacas peludas e dos chalés. Um bom lugar para uma segunda casa.',
        'A tarefa detecta a visita ao bioma.',
    ])
    c.q('wool', 'C', '&dLãs do rebanho', 'meadow:highland_wool', 6, 2, ['adv:meadow:main/wool_collector|Reúna as lãs alpinas'], [
        'As ovelhas do Meadow têm pelagens próprias, e cada uma dá uma lã de padrão diferente para tapetes e camas.',
        'Usa o avanço do mod, que registra cada tipo de lã ao longo do tempo. Tosquiar basta.',
    ])
    c.gallery('ch', [
        'meadow:cheese_block', 'meadow:sheep_cheese_block', 'meadow:goat_cheese_block', 'meadow:buffalo_cheese_block',
        'meadow:grain_cheese_block', 'meadow:warped_cheese_block', 'meadow:amethyst_cheese_block',
    ], 0, 4, 'Uma roda para a prateleira de cura. Cada queijo nasce de um leite ou ingrediente diferente; alguns pedem viagens. '
             'Registrar exige ter a roda inteira uma vez, sem consumo.', cols=7)
    out.append(c)

    # ------------------------------------------------------------ VC04
    c = Chapter(0x05, 'VC04', 'vinhedos_e_adegas', 'VC', 3, '&a&lVinhedos e Adegas', 'vinery:red_wine')
    c.q('seeds', 'A', '&aSementes da safra', 'vinery:red_grape_seeds', 0, 0,
        ['adv:vinery:main/wild_harvest|Obtenha sementes de uva de qualquer variedade'], [
        'Arbustos de uva selvagem crescem em planícies, savanas, taigas e selvas, cada região com suas variedades tinta e branca.',
        'Qualquer semente serve para começar.',
    ])
    c.q('stem', 'A', '&aParreira de pé', 'vinery:grapevine_stem', 1, 0,
        ['adv:vinery:main/sowing_the_future|Plante sementes em uma estaca de parreira'], [
        'Finque estacas de parreira e plante as sementes nelas. Com o tempo a videira sobe e dá cachos; treliças deixam o vinhedo mais bonito.',
        'A tarefa detecta o plantio na estaca.',
    ], deps=['seeds'])
    c.q('pot', 'A', '&aPés na uva', 'vinery:grapevine_pot', 2, 0,
        ['adv:vinery:main/juice_it_up|Coloque um pote de pisar uvas'], [
        'Encha o pote com uvas e pule em cima até virar suco. Recolha com garrafas de vinho vazias.',
        'A tarefa detecta o pote colocado. Pular é com você.',
    ], deps=['stem'])
    c.q('juice', 'A', '&aSuco de uva', 'vinery:red_grapejuice', 3, 0,
        ['adv:vinery:main/juicy_success|Obtenha suco de uva de qualquer variedade'], [
        'O suco é a base de todo vinho. A variedade da uva decide quais rótulos você poderá fermentar.',
        'Qualquer suco de uva conta.',
    ], deps=['pot'])
    c.q('barrel', 'A', '&aA mágica do barril', 'vinery:fermentation_barrel', 4, 0,
        ['adv:vinery:main/the_magic_of_the_barrel|Coloque um barril de fermentação'], [
        'No barril de fermentação o suco encontra os outros ingredientes da receita e vira vinho. Tenha garrafas vazias por perto.',
        'A tarefa detecta o barril colocado. Cada rótulo tem sua receita no EMI.',
    ], deps=['juice'])
    c.q('wine', 'M', '&6&lPrimeira garrafa', 'vinery:red_wine', 4, 1,
        ['adv:vinery:main/the_noble_drop|Obtenha uma garrafa de vinho de qualquer rótulo'], [
        'Da semente à rolha. Vinhos dão efeitos ao serem bebidos e ficam ótimos em adegas e estantes.',
        'Qualquer rótulo conta. O marco registra a garrafa nas suas mãos.',
    ], deps=['barrel'])
    c.q('press', 'A', '&aPrensa de maçãs', 'vinery:apple_press', 0, 2,
        ['adv:vinery:main/the_first_press|Coloque uma prensa de maçãs'], [
        'Maçãs não se pisam: vão para a prensa. É um ramal à parte, que não depende das uvas.',
        'A tarefa detecta a prensa colocada.',
    ])
    c.q('mash', 'A', '&aPolpa de maçã', 'vinery:apple_mash', 1, 2, ['adv:vinery:main/mashy_success|Obtenha polpa de maçã'], [
        'A prensa esmaga as maçãs em polpa. Cerejeiras e macieiras do Vinery também dão frutas para a adega.',
        POSSE,
    ], deps=['press'])
    c.q('ajuice', 'A', '&aSuco de maçã', 'vinery:apple_juice', 2, 2, ['adv:vinery:main/purely_apple|Obtenha suco de maçã'], [
        'A polpa prensada vira suco de maçã, pronto para o barril.',
        POSSE,
    ], deps=['mash'])
    c.q('cider', 'M', '&6&lSidra da casa', 'vinery:apple_cider', 3, 2, ['vinery:apple_cider'], [
        'Suco de maçã fermentado vira sidra. Leve, dourada e perfeita para depois da colheita.',
        'O marco registra a garrafa de sidra no inventário.',
    ], deps=['ajuice'])
    c.q('lattice', 'C', '&dTreliça coberta', 'vinery:oak_lattice', 0, 4,
        ['adv:vinery:main/overgrown_lattices|Cubra uma treliça com videira'], [
        'Treliças recebem folhas de videira e viram cercas vivas, pérgolas e fachadas de adega.',
        'A tarefa detecta a videira aplicada na treliça.',
    ])
    c.q('rack', 'C', '&dAdega organizada', 'vinery:oak_wine_rack_big', 1, 4,
        ['vinery:oak_wine_rack_big', 'vinery:wine_box'], [
        'Estantes de vinho e caixas de garrafas guardam a safra à vista. Há versões em várias madeiras.',
        'A tarefa pede a estante grande de carvalho e uma caixa de vinho como exemplo.',
    ])
    c.q('cherry', 'C', '&dTempo das cerejas', 'vinery:cherry', 2, 4, ['adv:vinery:main/cherry_picker|Colha cerejas'], [
        'As cerejeiras escuras do Vinery dão frutas para vinhos próprios e uma madeira avermelhada muito bonita.',
        POSSE,
    ])
    c.q('jungle', 'C', '&dUvas da selva', 'vinery:jungle_grapes_red', 3, 4,
        ['adv:vinery:main/budding_grapes|Obtenha uvas da selva tintas e brancas'], [
        'As uvas da selva crescem como cipós, não em estacas. Alguns dos rótulos mais curiosos começam nelas.',
        'O avanço pede as duas cores.',
    ])
    c.q('hat', 'C', '&dTraje de vindima', 'vinery:straw_hat', 4, 4,
        ['vinery:straw_hat', 'vinery:winemaker_apron'], [
        'Chapéu de palha e avental de vinicultor: o uniforme oficial de quem passa o dia entre parreiras.',
        POSSE,
    ])
    c.gallery('w', [
        'vinery:red_wine', 'vinery:noir_wine', 'vinery:bolvar_wine', 'vinery:chenet_wine', 'vinery:cristel_wine', 'vinery:clark_wine',
        'vinery:strad_wine', 'vinery:stal_wine', 'vinery:solaris_wine', 'vinery:aegis_wine', 'vinery:jellie_wine', 'vinery:lilitu_wine',
        'vinery:mellohi_wine', 'vinery:magnetic_wine', 'vinery:glowing_wine', 'vinery:chorus_wine', 'vinery:eiswein', 'vinery:cherry_wine',
        'vinery:apple_wine', 'vinery:apple_cider', 'vinery:kelp_cider', 'vinery:mead', 'vinery:jo_special_mixture', 'vinery:creepers_crush',
        'vinery:villagers_fright', 'vinery:bottle_mojang_noir',
    ], 0, 6, 'Um rótulo para a adega. A receita de fermentação, com a variedade de suco necessária, está no EMI. '
             'Idade da safra não importa aqui: registrar exige apenas ter a garrafa uma vez, sem consumo.')
    out.append(c)

    # ------------------------------------------------------------ VC05
    c = Chapter(0x06, 'VC05', 'paes_e_confeitaria', 'VC', 4, '&a&lPães e Confeitaria', 'bakery:croissant')
    c.q('yeast', 'A', '&aFermento vivo', 'bakery:yeast', 0, 0, ['adv:bakery:main/get_yeast|Obtenha fermento'], [
        'Todo pão começa com fermento. A receita está no EMI; morangos e aveia selvagens também aparecem pelo mundo para a padaria.',
        POSSE,
    ])
    c.q('dough', 'A', '&aMão na massa', 'bakery:rolling_pin', 1, 0, ['bakery:crafting_bowl', 'bakery:rolling_pin'], [
        'A tigela mistura a massa e o rolo abre. Neste pack as massas foram unificadas entre os mods de cozinha; confira no EMI a massa aceita por cada receita.',
        'A tarefa pede a tigela e o rolo, sem consumo.',
    ], deps=['yeast'])
    c.q('station', 'A', '&aBancada do padeiro', 'bakery:baker_station', 2, 0,
        ['adv:bakery:main/place_baker_station|Coloque uma bancada de padeiro'], [
        'Na bancada a massa ganha forma: pão rústico, baguete, trança, croissant. Depois é só levar ao forno.',
        'A tarefa detecta a bancada colocada.',
    ], deps=['dough'])
    c.q('stove', 'A', '&aForno aceso', 'bakery:brick_stove', 3, 0,
        ['adv:bakery:main/place_stove|Coloque um forno de padaria de qualquer material'], [
        'O forno de padaria assa pães, tortas e bolos. Há versões em tijolo, pedra, arenito e outros materiais: escolha o que combina com a cozinha.',
        'Qualquer forno do Bakery conta.',
    ], deps=['station'])
    c.q('bread', 'M', '&6&lFornada do dia', 'bakery:bread', 3, 1, ['adv:bakery:main/eat_bread|Coma um pão da padaria'], [
        'Casca crocante, miolo quente. O primeiro pão saído do seu forno merece ser comido ainda morno.',
        'O marco detecta a mordida. Dividir com alguém continua sendo boa ideia.',
    ], deps=['stove'])
    c.q('pot', 'A', '&aTacho de geleia', 'bakery:small_cooking_pot', 5, 0,
        ['adv:bakery:main/place_cooking_pot|Coloque um tacho pequeno', 'bakery:jar'], [
        'O tacho pequeno cozinha geleias e cremes sobre o forno. Tenha potes vazios para envasar.',
        'São duas tarefas: o tacho colocado e um pote vazio.',
    ])
    c.q('cake', 'A', '&aMassa de bolo', 'bakery:blank_cake', 0, 2, ['bakery:cake_dough', 'bakery:blank_cake'], [
        'Bolos têm ramal próprio: a massa doce vai ao forno e sai um bolo liso, pronto para receber cobertura.',
        POSSE,
    ])
    c.q('cut', 'M', '&6&lA primeira fatia', 'bakery:strawberry_cake', 1, 2,
        ['adv:bakery:main/cut_strawberry_cake|Corte um bolo de morango com a faca de pão'], [
        'Cubra o bolo com geleia de morango, coloque-o na mesa e corte com a faca de pão. Fatias e bolo inteiro contam como a mesma receita no álbum.',
        'O marco detecta o corte do bolo de morango colocado.',
    ], deps=['cake'])
    c.q('crate', 'C', '&dCaixote de pães', 'bakery:bread_crate', 0, 4,
        ['adv:bakery:main/place_bread_crate|Coloque um caixote de pães'], [
        'Caixotes cheios de pão na porta: o jeito mais simples de avisar que a padaria abriu.',
        'A tarefa detecta o caixote colocado.',
    ])
    c.q('display', 'C', '&dVitrine cheirosa', 'bakery:wall_display', 1, 4,
        ['adv:bakery:main/use_bread_on_wall_display|Exponha um pão na vitrine de parede'], [
        'Vitrines de parede, suportes de bolo e expositores mostram a fornada. Clique com o produto na mão para expor.',
        'A tarefa detecta o pão colocado na vitrine.',
    ])
    c.q('sign', 'C', '&dPlaca na calçada', 'bakery:street_sign', 2, 4, ['adv:bakery:main/place_sign|Coloque uma placa de rua'], [
        'Toda padaria de bairro tem uma placa. A sua agora também.',
        'A tarefa detecta a placa colocada.',
    ])
    c.q('baker', 'C', '&dColega de profissão', 'minecraft:spyglass', 3, 4,
        ['adv:bakery:main/spyglass_at_baker|Observe o padeiro viajante pela luneta'], [
        'Um padeiro viajante passa de vez em quando, vendendo ingredientes e curiosidades. Observe-o pela luneta quando aparecer.',
        'A tarefa detecta a observação. Não dá para marcar hora com ele.',
    ])
    c.gallery('bk', [
        'bakery:crusty_bread', 'bakery:bread', 'bakery:braided_bread', 'bakery:bun', 'bakery:baguette', 'bakery:toast',
        'bakery:croissant', 'bakery:waffle', 'bakery:cornet', 'bakery:donut', 'bakery:sandwich', 'bakery:vegetable_sandwich',
        'bakery:apple_pie', 'bakery:glowberry_tart', 'bakery:chocolate_tart', 'bakery:linzer_tart', 'bakery:bundt_cake', 'bakery:pudding',
        'bakery:strawberry_cake', 'bakery:chocolate_cake', 'bakery:sweetberry_cake', 'bakery:chocolate_gateau', 'bakery:jam_roll', 'bakery:chocolate_truffle',
        'bakery:strawberry_cupcake', 'bakery:sweetberry_cupcake', 'bakery:apple_cupcake', 'bakery:strawberry_glazed_cookie', 'bakery:chocolate_glazed_cookie', 'bakery:sweetberry_glazed_cookie',
        'bakery:strawberry_jam', 'bakery:sweetberry_jam', 'bakery:apple_jam', 'bakery:glowberry_jam', 'bakery:chocolate_jam', 'bakery:misslilitu_biscuit',
    ], 0, 6, 'Uma receita da vitrine. Bolo inteiro e fatia são a mesma página: aqui vale o produto inteiro. '
             'Registrar exige apenas tê-lo uma vez, sem consumo; a receita está no EMI.')
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
        'O diário do Tide registra cada espécie, onde vive e do que gosta. É o álbum oficial da pescaria: este livro não repete a lista de peixes.',
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
    out.append(c)
    return out
