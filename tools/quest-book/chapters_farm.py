# -*- coding: utf-8 -*-
"""Vida no Campo depois da saída dos mods Let's Do: VC02–VC05 e VC07.

VC01 (Caderno de Receitas) e VC06 (À Beira d'Água) continuam em chapters_a.py.
Cada capítulo aqui usa um número de capítulo novo (0x1B+) para que o progresso
salvo dos capítulos antigos de Farm & Charm, Meadow, Vinery e Bakery não seja
confundido com quests novas.
"""
from core import Chapter

POSSE = 'A tarefa registra posse, sem consumir: troca e presente também valem.'
ALBUM = 'Registrar exige apenas ter o item uma vez; nada é consumido. A receita e a estação de preparo estão no EMI.'


def build():
    out = []

    # ------------------------------------------------------------ VC02
    c = Chapter(0x1B, 'VC02', 'rotina_da_fazenda', 'VC', 1, '&a&lRotina da Fazenda', 'farmersdelight:straw')
    c.q('wild', 'A', '&aSementes da beira da estrada', 'farmersdelight:cabbage_seeds', 0, 0,
        ['adv:farmersdelight:main/get_fd_seed|Colha uma planta selvagem do Farmer\'s Delight'], [
        'Repolho, tomate, cebola e arroz crescem selvagens pelo mundo. Quebre um pé selvagem para começar sua própria horta.',
        'Os vegetais do Veggies Delight e do Vintage Delight também aparecem assim, cada um em seu clima.',
    ])
    c.q('easy', 'A', '&aColher sem replantar', 'minecraft:wheat', 1, 0,
        ['minecraft:wheat*16', 'minecraft:carrot*8', 'minecraft:potato*8'], [
        'Com o Harvest with Ease, clique com o botão direito em uma planta madura: ela é colhida e replantada na hora. Com uma enxada na mão, a colheita alcança uma área maior.',
        'A tarefa só confere a colheita no inventário. Nada de pisotear a horta.',
    ], deps=['wild'])
    c.q('rice', 'A', '&aPés na água', 'farmersdelight:rice_panicle', 2, 0,
        ['adv:farmersdelight:main/plant_rice|Plante arroz'], [
        'O arroz cresce em água rasa, com um bloco de terra embaixo. Um canal de um bloco de profundidade já serve.',
        'A tarefa detecta o plantio.',
    ])
    c.q('tomato', 'A', '&aTomate na corda', 'farmersdelight:rope', 3, 0,
        ['adv:farmersdelight:main/harvest_ropelogged_tomato|Colha tomates de uma corda'], [
        'Tomateiros sobem por cordas penduradas acima da planta. A horta fica mais alta, mais organizada e mais bonita.',
        'A tarefa detecta a colheita do tomate amarrado.',
    ])
    c.q('straw', 'A', '&aPalha para tudo', 'farmersdelight:straw', 4, 0,
        ['adv:farmersdelight:main/harvest_straw|Colha palha com uma faca'], [
        'Quebre capim, trigo ou arroz maduro com uma faca para recolher palha. Ela vira fardos, cordas, lona e cama para os animais.',
        'A tarefa detecta a primeira palha.',
    ])
    c.q('fields', 'M', '&6&lHorta completa', 'farmersdelight:cabbage', 2, 1,
        ['farmersdelight:cabbage', 'farmersdelight:tomato', 'farmersdelight:onion', 'farmersdelight:rice'], [
        'Repolho, tomate, cebola e arroz na despensa: a base de metade do Caderno de Receitas.',
        'O marco confere os quatro no inventário, sem consumir. Plantar continua sendo a parte divertida.',
    ], deps=['rice'])
    c.q('colony', 'C', '&dCogumelos em casa', 'farmersdelight:red_mushroom_colony', 0, 2,
        ['adv:farmersdelight:main/get_mushroom_colony|Obtenha uma colônia de cogumelos'], [
        'Cogumelos plantados em solo rico viram colônias, que podem ser colhidas várias vezes com uma faca.',
        POSSE,
    ])
    c.q('allcrops', 'C', '&dDe tudo um pouco', 'farmersdelight:organic_compost', 1, 2,
        ['adv:farmersdelight:main/plant_all_crops|Plante todas as culturas do Farmer\'s Delight e do vanilla'], [
        'Trigo, cenoura, batata, beterraba, abóbora, melancia, cacau, repolho, tomate, cebola, arroz e mais. Um desafio de quem gosta de horta variada.',
        'Usa o avanço do próprio Farmer\'s Delight.',
    ])
    c.q('crates', 'C', '&dCaixotes no celeiro', 'farmersdelight:cabbage_crate', 2, 2,
        ['farmersdelight:cabbage_crate', 'farmersdelight:tomato_crate', 'farmersdelight:onion_crate'], [
        'Caixotes guardam nove unidades da colheita em um bloco e enfeitam qualquer celeiro.',
        POSSE,
    ], deps=['fields'])
    c.q('bale', 'C', '&dFardos de palha', 'farmersdelight:straw_bale', 4, 2, ['farmersdelight:straw_bale*4'], [
        'Fardos de palha decoram o celeiro, amortecem quedas e, de quebra, guardam a palha que sobrou.',
        POSSE,
    ], deps=['straw'])
    # cozinha da casa
    c.q('board', 'A', '&aTábua sob medida', 'choppersdelight:oak_cutting_board', 6, 0,
        ['choppersdelight:oak_cutting_board|Obtenha uma tábua de corte de carvalho do Chopper\'s Delight'], [
        'O Chopper\'s Delight faz tábuas de corte em todas as madeiras do pack. Funcionam como a tábua do Farmer\'s Delight, só que combinando com a cozinha.',
        'A de carvalho é só um exemplo; qualquer madeira tem receita no EMI. ' + POSSE,
    ])
    c.q('handson', 'A', '&aMão na massa, de verdade', 'farmersdelight:cooking_pot', 7, 0,
        ['farmersdelight:cooking_pot'], [
        'Com o Hands-On Delight, a panela, a tábua de corte, a frigideira e a grelha mostram os ingredientes e o preparo no próprio bloco: dá para ver o que está cozinhando e quanto falta.',
        'Na tábua, alguns ingredientes precisam ser montados em ordem: o primeiro vai embaixo. Olhe para a estação para ver as dicas. ' + POSSE,
    ])
    c.q('copper', 'A', '&aFaca de cobre', 'vanilladelight:copper_knife', 8, 0, ['vanilladelight:copper_knife'], [
        'O Vanilla Delight acrescenta uma faca de cobre, para quem quer trocar a de pederneira cedo, e dezenas de receitas com ingredientes que você já tem: maçã, abóbora, mel, frutas vermelhas.',
        POSSE,
    ])
    c.q('modular', 'C', '&dCozinha planejada', 'vanilladelight:modular_stove', 7, 1,
        ['vanilladelight:modular_stove', 'vanilladelight:modular_cabinet'], [
        'Fogão e armário modulares aceitam padrões de azulejo, e há fogões e armários em pedra, arenito, deepslate e outros acabamentos.',
        'A tarefa pede o fogão e o armário modulares; o projeto da cozinha é seu.',
    ], deps=['handson'])
    c.q('vstove', 'C', '&dFogão de pedra', 'vanilladelight:stone_bricks_stove', 8, 1, ['vanilladelight:stone_bricks_stove'], [
        'Um fogão de tijolos de pedra para a cozinha rústica. Funciona como o fogão do Farmer\'s Delight.',
        POSSE,
    ], deps=['copper'])
    c.gallery('vd', [
        'vanilladelight:apple_salad', 'vanilladelight:berries_salad', 'vanilladelight:carrot_salad', 'vanilladelight:cod_stew',
        'vanilladelight:pufferfish_stew', 'vanilladelight:sweet_fish_soup', 'vanilladelight:glow_tropical_fish_stew',
        'vanilladelight:caramelized_chicken', 'vanilladelight:grilled_beetroot', 'vanilladelight:honey_pudding',
        'vanilladelight:sweet_berry_custard', 'vanilladelight:caramel_candy', 'vanilladelight:honey_candy',
        'vanilladelight:glow_berries_candy', 'vanilladelight:sweet_berries_jam', 'vanilladelight:glow_berries_jam',
        'vanilladelight:golden_apple_cider', 'vanilladelight:carrot_cake', 'vanilladelight:honey_cake',
        'vanilladelight:melon_pie', 'vanilladelight:chorus_pie', 'vanilladelight:milky_pumpkin',
        'vanilladelight:roasted_beets', 'vanilladelight:cooked_apple',
    ], 0, 4, 'Uma receita do Vanilla Delight, feita com ingredientes do Minecraft de sempre. ' + ALBUM)
    out.append(c)

    # ------------------------------------------------------------ VC03
    c = Chapter(0x1C, 'VC03', 'taverna_e_queijaria', 'VC', 2, '&a&lTaverna e Queijaria', 'brewinandchewin:keg')
    c.q('keg', 'A', '&aBarril de fermentação', 'brewinandchewin:keg', 0, 0,
        ['adv:brewinandchewin:main/place_keg|Coloque um barril'], [
        'No Brewin\' and Chewin\', o barril fermenta bebidas e conservas com o tempo. Encha com o líquido base, junte os ingredientes e espere.',
        'A tarefa detecta o barril colocado.',
    ])
    c.q('temp', 'A', '&aTemperatura certa', 'brewinandchewin:heating_cask', 1, 0,
        ['adv:brewinandchewin:main/place_temperature_block_near_keg|Coloque uma fonte de calor ou frio junto ao barril'], [
        'Cada receita pede uma temperatura. Barril de aquecimento, caixote de gelo, fogo ou gelo ao redor mudam o clima do barril; o painel dele mostra a faixa atual.',
        'A tarefa detecta o bloco de temperatura colocado junto ao barril.',
    ], deps=['keg'])
    c.q('tankard', 'A', '&aCaneca na mão', 'brewinandchewin:tankard', 2, 0, ['brewinandchewin:tankard'], [
        'Bebidas do barril se servem em canecas. Um porta-copos na mesa completa a taverna.',
        POSSE,
    ])
    c.q('drink', 'M', '&6&lPrimeira rodada', 'brewinandchewin:beer', 3, 0,
        ['adv:brewinandchewin:main/brew_drink|Obtenha uma bebida fermentada'], [
        'Cerveja, hidromel, vinho de arroz ou qualquer outra: a primeira bebida da sua taverna.',
        'Bebidas fortes dão efeitos e embriaguez; beba com moderação, até em bloco quadrado.',
    ], deps=['tankard'])
    c.q('unripe', 'A', '&aQueijo em cura', 'brewinandchewin:unripe_flaxen_cheese_wheel', 0, 1,
        ['adv:brewinandchewin:main/ferment_cheese|Obtenha uma roda de queijo fresco'], [
        'O barril também coalha leite em rodas de queijo fresco. Coloque a roda no mundo e espere ela curar.',
        'Qualquer um dos dois queijos conta.',
    ], deps=['keg'])
    c.q('cheese', 'M', '&6&lQueijo curado', 'brewinandchewin:flaxen_cheese_wheel', 1, 1,
        ['brewinandchewin:flaxen_cheese_wheel'], [
        'Depois de alguns dias no lugar, a roda fresca cura e pode ser fatiada em cunhas com a faca.',
        'O marco registra a roda de queijo dourado curada.',
    ], deps=['unripe'])
    c.q('scarlet', 'C', '&dQueijo escarlate', 'brewinandchewin:scarlet_cheese_wheel', 2, 1,
        ['brewinandchewin:scarlet_cheese_wheel'], [
        'O queijo escarlate leva fungos do Nether e cura com um sabor bem mais forte.',
        POSSE,
    ])
    c.q('fondue', 'C', '&dFondue flamejante', 'brewinandchewin:fiery_fondue_pot', 1, 2,
        ['adv:brewinandchewin:main/cook_fiery_fondue|Prepare um fondue flamejante'], [
        'Queijo escarlate derretido numa panela no centro da mesa. Sirva em porções com pão.',
        'A tarefa registra a panela de fondue pronta.',
    ], deps=['cheese'])
    c.q('pizza', 'C', '&dNoite da pizza', 'brewinandchewin:pizza', 2, 2, ['brewinandchewin:pizza'], [
        'Massa, molho, queijo e as coberturas que quiser. A pizza vai na mesa e se serve em fatias.',
        POSSE,
    ])
    c.q('coaster', 'C', '&dTaverna montada', 'brewinandchewin:coaster', 4, 0, ['brewinandchewin:coaster', 'brewinandchewin:ice_crate'], [
        'Porta-copos sobre o balcão e um caixote de gelo atrás dele. O resto da decoração fica por conta do taverneiro.',
        POSSE,
    ])
    c.gallery('dr', [
        'brewinandchewin:beer', 'brewinandchewin:vodka', 'brewinandchewin:mead', 'brewinandchewin:rice_wine',
        'brewinandchewin:egg_grog', 'brewinandchewin:strongroot_ale', 'brewinandchewin:saccharine_rum', 'brewinandchewin:pale_jane',
        'brewinandchewin:salty_folly', 'brewinandchewin:steel_toe_stout', 'brewinandchewin:glittering_grenadine',
        'brewinandchewin:bloody_mary', 'brewinandchewin:red_rum', 'brewinandchewin:withering_dross',
        'brewinandchewin:dread_nog', 'brewinandchewin:kombucha',
    ], 0, 4, 'Uma bebida para a carta da taverna. Cada uma pede base, ingredientes e temperatura próprios no barril. ' + ALBUM, cols=8)
    c.gallery('fo', [
        'brewinandchewin:kimchi', 'brewinandchewin:jerky', 'brewinandchewin:pickled_pickles', 'brewinandchewin:kippers',
        'brewinandchewin:cocoa_fudge', 'brewinandchewin:vegetable_omelet', 'brewinandchewin:cheesy_pasta',
        'brewinandchewin:creamy_onion_soup', 'brewinandchewin:scarlet_pierogi', 'brewinandchewin:horror_lasagna',
        'brewinandchewin:quiche', 'brewinandchewin:ham_and_cheese_sandwich', 'brewinandchewin:sweet_berry_jam',
        'brewinandchewin:glow_berry_marmalade', 'brewinandchewin:apple_jelly',
    ], 0, 7, 'Petiscos, conservas e pratos com queijo para acompanhar a bebida. ' + ALBUM, cols=8)
    out.append(c)

    # ------------------------------------------------------------ VC04
    c = Chapter(0x1D, 'VC04', 'grelha_e_fogo', 'VC', 3, '&a&lGrelha e Fogo', 'barbequesdelight:grill')
    c.q('grill', 'A', '&aGrelha acesa', 'barbequesdelight:grill', 0, 0, ['barbequesdelight:grill'], [
        'O Barbeque\'s Delight traz uma grelha de verdade: coloque-a sobre uma fonte de calor e vire os espetos para assar dos dois lados.',
        'Deixar tempo demais queima o espeto. ' + POSSE,
    ])
    c.q('raw', 'A', '&aEspeto montado', 'barbequesdelight:raw_beef_skewer', 1, 0,
        ['tag:barbequesdelight:raw_skewers|Monte um espeto cru de qualquer tipo'], [
        'Carnes, peixes, cogumelos, batatas e vegetais vão no palito: a montagem é feita com o espeto na mão, conforme o EMI.',
        'Qualquer espeto cru conta.',
    ], deps=['grill'])
    c.q('grilled', 'M', '&6&lChurrasco no quintal', 'barbequesdelight:grilled_beef_skewer', 2, 0,
        ['tag:barbequesdelight:grilled_skewers|Obtenha um espeto grelhado de qualquer tipo'], [
        'O primeiro espeto no ponto. Agora é chamar os vizinhos.',
        'Qualquer espeto grelhado conta.',
    ], deps=['raw'])
    c.q('burnt', 'C', '&dPassou do ponto', 'barbequesdelight:burnt_skewer', 1, 1, ['barbequesdelight:burnt_skewer'], [
        'Todo churrasqueiro já queimou um espeto. Este é o seu atestado.',
        POSSE,
    ], deps=['raw'])
    c.gallery('sk', [
        'barbequesdelight:grilled_beef_skewer', 'barbequesdelight:grilled_chicken_skewer', 'barbequesdelight:grilled_lamb_skewer',
        'barbequesdelight:grilled_pork_sausage_skewer', 'barbequesdelight:grilled_rabbit_skewer', 'barbequesdelight:grilled_cod_skewer',
        'barbequesdelight:grilled_salmon_skewer', 'barbequesdelight:grilled_mushroom_skewer', 'barbequesdelight:grilled_potato_skewer',
        'barbequesdelight:grilled_vegetable_skewer', 'barbequesdelight:kebab_sandwich', 'barbequesdelight:kebab_wrap',
        'barbequesdelight:bibimbap',
    ], 0, 3, 'Um espeto ou prato montado da grelha. ' + ALBUM, cols=7)
    out.append(c)

    # ------------------------------------------------------------ VC05
    c = Chapter(0x1E, 'VC05', 'banquete_de_gensokyo', 'VC', 4, '&a&lBanquete de Gensokyo', 'youkaisfeasts:green_tea')
    # chá
    c.q('tea', 'A', '&aChá do campo', 'youkaisfeasts:tea_seeds', 0, 0,
        ['adv:youkaisfeasts:main/tea|Plante um pé de chá'], [
        'O Youkai\'s Feasts traz uma culinária inteira de Gensokyo. Pés de chá selvagens aparecem pelo mundo; plante as sementes para ter a sua plantação.',
        'A tarefa detecta o plantio.',
    ])
    c.q('leaves', 'A', '&aFolhas colhidas', 'youkaisfeasts:tea_leaves', 1, 0,
        ['adv:youkaisfeasts:main/tea_leaves|Colha folhas de chá'], [
        'As folhas frescas viram chá verde, amarelo, branco, oolong, preto ou escuro, conforme secam, fermentam ou torram. O EMI mostra cada caminho.',
        POSSE,
    ], deps=['tea'])
    c.q('kettle', 'A', '&aChaleira de ferro', 'youkaisfeasts:kettle', 2, 0, ['youkaisfeasts:kettle'], [
        'A chaleira de Gensokyo prepara os chás sobre o fogo. Tenha xícaras à mão.',
        POSSE,
    ], deps=['leaves'])
    c.q('cup', 'M', '&6&lHora do chá', 'youkaisfeasts:green_tea', 2, 1,
        ['tag:youkaisfeasts:tea|Obtenha um chá de Gensokyo'], [
        'Uma xícara de chá feita do pé ao bule. Qualquer chá do Youkai\'s Feasts conta.',
        'O marco registra o chá no inventário.',
    ], deps=['kettle'])
    c.q('teamaster', 'C', '&dMestre do chá', 'youkaisfeasts:oolong_tea', 3, 1,
        ['adv:youkaisfeasts:main/tea_master|Beba os seis chás de Gensokyo'], [
        'Verde, amarelo, branco, oolong, preto e escuro. Cada um com seu tempo de preparo e seu sabor.',
        'Usa o avanço do próprio mod.',
    ], deps=['cup'])
    # uvas e vinho
    c.q('grape', 'A', '&aParreira japonesa', 'youkaisfeasts:red_grape_seeds', 5, 0,
        ['adv:youkaisfeasts:main/grape|Plante uma muda de uva'], [
        'Uvas tintas, brancas e pretas crescem em parreiras que sobem e se espalham. Uvas selvagens aparecem pelo mundo.',
        'A tarefa detecta o plantio.',
    ])
    c.q('harvest', 'A', '&aCacho maduro', 'youkaisfeasts:red_grape', 6, 0,
        ['adv:youkaisfeasts:main/grape_harvest|Colha um cacho de uva'], [
        'Cachos maduros pendem da parreira. Podar os galhos mantém a planta produzindo.',
        'A tarefa detecta a colheita.',
    ], deps=['grape'])
    c.q('tank', 'A', '&aTanque de fermentação', 'youkaisfeasts:fermentation_tank', 7, 0, ['youkaisfeasts:fermentation_tank'], [
        'O tanque fermenta sucos em vinhos e arroz em saquê. Uma torneira de cobre facilita encher as garrafas.',
        POSSE,
    ], deps=['harvest'])
    c.q('wine', 'M', '&6&lSafra de Gensokyo', 'youkaisfeasts:red_wine', 7, 1,
        ['tag:youkaisfeasts:wine|Obtenha um vinho de Gensokyo'], [
        'Tinto, branco, Borgonha, champanhe e outros rótulos. Qualquer vinho conta.',
        'O marco registra a garrafa no inventário.',
    ], deps=['tank'])
    # soja e tofu
    c.q('soy', 'A', '&aSoja no quintal', 'youkaisfeasts:soybean', 9, 0,
        ['adv:youkaisfeasts:main/soybean|Plante soja'], [
        'Soja selvagem aparece pelo mundo. É a base de tofu, molho de soja, missô e natto.',
        'A tarefa detecta o plantio.',
    ])
    c.q('basin', 'A', '&aPrensa de madeira', 'youkaisfeasts:wood_basin', 10, 0,
        ['adv:youkaisfeasts:main/squeeze|Esprema ingredientes na bacia'], [
        'A bacia de madeira espreme soja, uvas e outros ingredientes. Pule ou clique para prensar.',
        'A tarefa detecta o uso da bacia.',
    ], deps=['soy'])
    c.q('tofu', 'M', '&6&lTofu caseiro', 'youkaisfeasts:tofu', 10, 1, ['youkaisfeasts:tofu'], [
        'Leite de soja coalhado e prensado: o tofu abre caminho para mapo tofu, hambúrguer de tofu e muito mais.',
        'O marco registra o tofu no inventário.',
    ], deps=['basin'])
    # cozinha
    c.q('board', 'A', '&aTábua de culinária', 'youkaisfeasts:cuisine_board', 0, 3,
        ['adv:youkaisfeasts:main/cuisine_board|Monte um prato na tábua de culinária'], [
        'Na tábua de culinária, sushis, rolinhos e pratos montados são feitos colocando os ingredientes na ordem certa.',
        'A tarefa detecta o uso da tábua.',
    ])
    c.q('pot', 'A', '&aPanelinha de ferro', 'youkaisfeasts:small_iron_pot', 1, 3,
        ['adv:youkaisfeasts:main/small_pot|Cozinhe na panelinha de ferro'], [
        'Panelinha, panela baixa e caldeirão grande cozinham sopas e ensopados sobre o fogo.',
        'A tarefa detecta o cozimento.',
    ])
    c.q('steamer', 'A', '&aVapor', 'youkaisfeasts:steamer_rack', 2, 3,
        ['adv:youkaisfeasts:main/steamer|Cozinhe no vapor'], [
        'Empilhe bandejas de vapor sobre uma panela com água no fogo e tampe. Pãezinhos, ovos e peixes saem macios.',
        'A tarefa detecta o primeiro cozimento a vapor.',
    ])
    c.q('rack', 'A', '&aVaral de secar', 'youkaisfeasts:drying_rack', 3, 3, ['youkaisfeasts:drying_rack'], [
        'O varal seca peixes, folhas de chá, uvas-passas e couro ao sol.',
        POSSE,
    ])
    c.q('sushi', 'C', '&dMestre do sushi', 'youkaisfeasts:otoro_nigiri', 0, 4,
        ['adv:youkaisfeasts:main/sushi_master|Prepare os quatro sushis clássicos'], [
        'Otoro, gunkan de ovas, nigiri de atum e outros: cortes precisos na tábua de culinária.',
        'Usa o avanço do próprio mod.',
    ], deps=['board'])
    c.q('tower', 'C', '&dTorre de vapor', 'youkaisfeasts:steamer_lid', 2, 4,
        ['adv:youkaisfeasts:main/max_steamer|Monte uma torre de vapor com muitas bandejas'], [
        'Quanto mais bandejas, mais coisas cozinham juntas. Até onde vai a sua torre?',
        'Usa o avanço do próprio mod.',
    ], deps=['steamer'])
    c.q('kaguya', 'C', '&dPrincesa de bambu', 'youkaisfeasts:kaguya_hime', 1, 4,
        ['adv:youkaisfeasts:main/kaguya_hime|Prepare o kaguya-hime'], [
        'Um prato servido dentro do bambu, digno de uma princesa da lua.',
        POSSE,
    ], deps=['pot'])
    c.q('udumbara', 'C', '&dFlor de udumbara', 'youkaisfeasts:udumbara_flower', 3, 4,
        ['adv:youkaisfeasts:main/udumbara_flower|Obtenha uma flor de udumbara'], [
        'Dizem que a udumbara floresce uma vez a cada três mil anos. Em Lilyvale, com paciência e o cuidado certo, um pouco antes.',
        POSSE,
    ])
    c.gallery('gk', [
        'youkaisfeasts:mapo_tofu', 'youkaisfeasts:tofu_burger', 'youkaisfeasts:stinky_tofu', 'youkaisfeasts:cold_tofu',
        'youkaisfeasts:miso_soup', 'youkaisfeasts:seafood_miso_soup', 'youkaisfeasts:longevity_noodles', 'youkaisfeasts:lions_head',
        'youkaisfeasts:onigili', 'youkaisfeasts:pork_rice_ball', 'youkaisfeasts:grilled_eel_over_rice', 'youkaisfeasts:kabayaki',
        'youkaisfeasts:tamagoyaki', 'youkaisfeasts:steamed_egg_in_bamboo', 'youkaisfeasts:mantou', 'youkaisfeasts:bun',
        'youkaisfeasts:oyaki', 'youkaisfeasts:steamed_crab', 'youkaisfeasts:tekka_maki', 'youkaisfeasts:kappa_maki',
        'youkaisfeasts:california_roll', 'youkaisfeasts:tuna_nigiri', 'youkaisfeasts:egg_nigiri', 'youkaisfeasts:volcano_roll',
        'youkaisfeasts:mochi', 'youkaisfeasts:sakura_mochi', 'youkaisfeasts:matcha_mochi', 'youkaisfeasts:mitarashi_dango',
        'youkaisfeasts:tsukimi_dango', 'youkaisfeasts:assorted_dango', 'youkaisfeasts:senbei', 'youkaisfeasts:candy_apple',
        'youkaisfeasts:avgolemono', 'youkaisfeasts:pastitsio', 'youkaisfeasts:tuscan_salmon', 'youkaisfeasts:blazing_red_curry',
    ], 0, 6, 'Um prato do banquete de Gensokyo. ' + ALBUM)
    c.gallery('gd', [
        'youkaisfeasts:green_tea', 'youkaisfeasts:yellow_tea', 'youkaisfeasts:white_tea', 'youkaisfeasts:oolong_tea',
        'youkaisfeasts:black_tea', 'youkaisfeasts:dark_tea', 'youkaisfeasts:genmai_tea', 'youkaisfeasts:sakura_honey_tea',
        'youkaisfeasts:red_wine', 'youkaisfeasts:white_wine', 'youkaisfeasts:burgundy', 'youkaisfeasts:champagne',
        'youkaisfeasts:mead', 'youkaisfeasts:dassai', 'youkaisfeasts:kiku', 'youkaisfeasts:hakutsuru',
        'youkaisfeasts:red_grape_juice', 'youkaisfeasts:white_grape_juice',
    ], 8, 6, 'Uma bebida da casa de chá. Chás vêm da chaleira; vinhos e saquês, do tanque de fermentação. ' + ALBUM, cols=3)
    out.append(c)

    # ------------------------------------------------------------ VC07
    c = Chapter(0x1F, 'VC07', 'sabores_de_outros_mundos', 'VC', 6, '&a&lSabores de Outros Mundos', 'mynethersdelight:nether_bricks_stove')
    c.q('nstove', 'A', '&aFogão do Nether', 'mynethersdelight:nether_bricks_stove', 0, 0, ['mynethersdelight:nether_bricks_stove'], [
        'O My Nether\'s Delight leva a cozinha ao Nether. O fogão de tijolos do Nether (há uma versão de alma) cozinha como o do Farmer\'s Delight.',
        'Este capítulo é opcional e depende de viajar ao Nether e ao End; nada na fazenda precisa dele. ' + POSSE,
    ])
    c.q('pepper', 'A', '&aPimenta-bala', 'mynethersdelight:bullet_pepper', 1, 0, ['mynethersdelight:bullet_pepper'], [
        'A pimenta-bala cresce em solo do Nether. Dá ardência a curries, espetinhos e sopas.',
        POSSE,
    ])
    c.q('soil', 'A', '&aSolo ressurgente', 'mynethersdelight:resurgent_soil', 2, 0, ['mynethersdelight:resurgent_soil'], [
        'O composto de Letios vira solo ressurgente, que faz fungos e plantas do Nether crescerem melhor.',
        POSSE,
    ])
    c.q('hoglin', 'M', '&6&lBanquete do Nether', 'mynethersdelight:roast_stuffed_hoglin', 1, 1, ['mynethersdelight:roast_stuffed_hoglin'], [
        'Hoglin recheado e assado na panela, servido como banquete no centro da mesa. Não é para qualquer jantar.',
        'O marco registra o banquete no inventário.',
    ], deps=['pepper'])
    c.q('estove', 'A', '&aFogão do End', 'ends_delight:end_stove', 5, 0,
        ['adv:ends_delight:the_end_chef|Obtenha um fogão do End'], [
        'O End\'s Delight transforma frutas de coro, carne de shulker e até restos da dragoa em comida.',
        POSSE,
    ])
    c.q('eknife', 'A', '&aFaca do vazio', 'ends_delight:purpur_knife', 6, 0,
        ['adv:ends_delight:get_knife|Obtenha uma faca do End'], [
        'Facas de pedra do End, púrpura ou casca de ovo de dragão funcionam na tábua de corte como qualquer outra.',
        'Qualquer faca do End conta.',
    ])
    c.q('tea', 'A', '&aChá de flor de coro', 'ends_delight:chorus_flower_tea', 7, 0,
        ['adv:ends_delight:get_chorus_flower_tea|Prepare um chá de flor de coro'], [
        'Flores de coro secas viram um chá de cor estranha e sabor mais estranho ainda.',
        POSSE,
    ])
    c.q('dragon', 'M', '&6&lCeia da dragoa', 'ends_delight:dragon_meat_stew', 6, 1,
        ['adv:ends_delight:dragon_egg_shell_feast|Prepare o ensopado de dragão e o ovo de dragão no vapor'], [
        'Os dois grandes banquetes do End: ensopado de carne de dragão e ovo de dragão no vapor.',
        'Usa o avanço do próprio mod, que pede os dois.',
    ], deps=['eknife'])
    c.gallery('ne', [
        'mynethersdelight:spicy_hoglin_stew', 'mynethersdelight:spicy_curry', 'mynethersdelight:spicy_noodle_soup',
        'mynethersdelight:strider_stew', 'mynethersdelight:crimson_stroganoff', 'mynethersdelight:hotdog',
        'mynethersdelight:chilidog', 'mynethersdelight:nether_burger', 'mynethersdelight:hot_wings',
        'mynethersdelight:scotch_eggs', 'mynethersdelight:deviled_egg', 'mynethersdelight:breakfast_sampler',
        'mynethersdelight:giant_takoyaki', 'mynethersdelight:fries_ghasta', 'mynethersdelight:ghast_salad',
        'mynethersdelight:hot_cream_cone', 'mynethersdelight:magma_cake', 'mynethersdelight:tear_popsicle',
    ], 0, 3, 'Um prato do Nether, apimentado e quente. ' + ALBUM)
    c.gallery('en', [
        'ends_delight:ender_noodle', 'ends_delight:ender_congee', 'ends_delight:ender_bamboo_rice',
        'ends_delight:shulker_soup', 'ends_delight:stir_fried_shulker_meat', 'ends_delight:shulker_omelette',
        'ends_delight:roasted_dragon_steak', 'ends_delight:dragon_leg_with_sauce', 'ends_delight:dragon_breath_and_chorus_soup',
        'ends_delight:end_mixed_salad', 'ends_delight:assorted_salad', 'ends_delight:stuffed_rice_cake',
        'ends_delight:chorus_fruit_pie', 'ends_delight:chorus_cookie', 'ends_delight:chorus_fruit_popsicle',
        'ends_delight:bubble_tea', 'ends_delight:chorus_fruit_milk_tea', 'ends_delight:dragon_breath_soda',
    ], 7, 3, 'Um prato do End, feito com o que sobra das ilhas e da dragoa. ' + ALBUM)
    out.append(c)
    return out
