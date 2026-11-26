# -*- coding: utf-8 -*-
"""O Mundo Lá Fora: MF04 Estaleiro (aleki's Nifty Ships).

Regras de montagem conferidas no mod 1.0.14 (ShipbuildingMultiblocks, OarlockBlock, CleatBlock,
AngledWoodenBoatFrameBlock e SloopUnderConstructionEntity). As plantas saem de ship_diagrams.py.
"""
import os

from PIL import Image

from core import ROOT, Chapter

PLANTA = 'lilyvale:textures/quests/estaleiro/'
ROWBOAT_IMG = PLANTA + 'barco_a_remo.png'
SLOOP_IMG = PLANTA + 'sloop.png'

PAGINA = '{@pagebreak}'   # quebra de página na descrição do FTB Quests

LEGENDA = [
    '&3&lComo ler a planta',
    'Cada quadrado é uma armação vista de cima, com a proa no alto.',
    '&6Seta&r: andaime inclinado. A seta mostra para onde você deve olhar ao colocá-lo, sempre para fora do casco; assim a borda alta fica do lado de fora. Os cantos se ajustam sozinhos, como degraus de escada; coloque primeiro as armações retas e depois os cantos.',
    '&eListras&r: andaime plano, sem direção.',
    'O ícone na margem marca as armações que recebem uma peça em cima. Forquetas e cunhos são colocados de fora do barco, '
    'olhando para o casco: assim ficam virados para fora, como o mod exige.',
]

TABUAS = ('Depois de montar a planta, clique com &etábuas&r em cada armação: a primeira tábua define a madeira '
          'e mais três completam a armação, ou seja, quatro tábuas por armação. Use a mesma madeira no casco inteiro: '
          'é ela que dá a cor do barco e os materiais das próximas etapas.')


def build():
    out = []

    # ------------------------------------------------------------ MF04
    c = Chapter(0x20, 'MF04', 'estaleiro', 'MF', 3, '&3&lEstaleiro', 'alekiships:sloop_icon_only')

    c.q('scaffold', 'A', '&3Andaime de estaleiro', 'alekiships:watercraft_frame_angled', 0, 0,
        ['alekiships:watercraft_frame_angled*6'], [
        'Barcos de verdade nascem em terra firme. No aleki\'s Nifty Ships, o casco é desenhado no chão com andaimes de estaleiro '
        'e depois forrado de tábuas.',
        'O andaime inclinado (Sloped Shipwright\'s Scaffolding) sai de seis andaimes comuns em escada na bancada e rende cinco. '
        'O barco a remo pede seis.',
        'Escolha um lugar plano perto da água: o barco aparece onde o casco foi montado.',
    ])
    c.q('oarlock', 'A', '&3Forquetas e remos', 'alekiships:oarlock', 1, 0,
        ['alekiships:oarlock*2', 'alekiships:oar*2'], [
        'As forquetas (Oarlock) apoiam os remos e são a peça que fecha o barco a remo. Cada uma leva quatro barras de ferro.',
        'Os remos (Oar) saem de gravetos e uma laje de madeira. Com o barco pronto, clique nele com os remos para encaixá-los.',
    ], deps=['scaffold'])
    c.q('rowboat', 'M', '&6&lBarco a remo', 'alekiships:rowboat_icon_only', 2, 0,
        ['adv:alekiships:rowboat_completed|Monte um barco a remo'], [
        'Seis andaimes inclinados formam um casco de duas armações de largura por três de comprimento:',
        '{image:%s width:80 height:100 align:center}' % ROWBOAT_IMG,
        'Vire a página para ler a planta, montar o barco e ver os controles.',
        PAGINA,
    ] + LEGENDA + [
        PAGINA,
        '&3&lMontagem',
        TABUAS + ' São 24 tábuas no total.',
        'Por fim, coloque uma forqueta em cima de cada armação do meio, uma de cada lado, de fora do barco e olhando para o casco. '
        'Tábuas e forquetas podem vir em qualquer ordem: quando o casco estiver completo e as duas forquetas no lugar, o barco aparece.',
        'Se aparecer "No Valid Hull Structure Found", confira a direção das setas e se todas as armações levaram as quatro tábuas.',
        'O marco usa o avanço do próprio mod.',
        PAGINA,
        '&3&lControles padrão',
        '&eW&r / &eS&r: remar para a frente e para trás.',
        '&eA&r / &eD&r: virar para a esquerda e para a direita.',
        '&eShift&r: sair do barco.',
        'Com os remos encaixados o barco anda cerca de 60% mais rápido; sem eles, se arrasta como um bote comum. O vento '
        'também empurra um pouco o barco.',
    ], deps=['oarlock'])

    c.q('flat', 'A', '&3Fundo plano', 'alekiships:watercraft_frame_flat', 0, 2,
        ['alekiships:watercraft_frame_flat*6', 'alekiships:watercraft_frame_angled*18'], [
        'O sloop tem fundo largo. Além de 18 andaimes inclinados, ele pede 6 andaimes planos (Flat Shipwright\'s Scaffolding), '
        'feitos com três andaimes comuns em linha.',
        'Separe também madeira à vontade: só o casco leva 96 tábuas.',
    ], deps=['scaffold'])
    c.q('cleat', 'A', '&3Cunho e âncora', 'alekiships:cleat', 1, 2,
        ['alekiships:cleat*4', 'alekiships:anchor'], [
        'Os cunhos (Cleat) são onde se amarram os cabos do barco, e são eles que transformam o casco pronto em um sloop em construção. '
        'O sloop pede quatro, um em cada canto marcado na planta.',
        'A âncora (Anchor) entra perto do fim da obra e segura o barco parado contra o vento. Ela pede um bloco de ferro.',
    ], deps=['flat'])
    c.q('sloop', 'M', '&6&lSloop', 'alekiships:sloop_icon_only', 2, 2,
        ['adv:alekiships:sloop_completed|Termine um sloop'], [
        'O sloop é um veleiro de verdade. O casco tem 24 armações: duas de largura nas duas primeiras fileiras da proa e quatro da '
        'metade até a popa:',
        '{image:%s width:96 height:144 align:center}' % SLOOP_IMG,
        'Vire a página para ler a planta, montar o casco, terminar a obra e ver os controles.',
        PAGINA,
    ] + LEGENDA + [
        PAGINA,
        '&3&lCasco',
        TABUAS + ' São 96 tábuas só no casco.',
        'Com o casco completo, coloque um cunho em cima de cada um dos quatro cantos marcados, de fora do barco e olhando para o '
        'casco. Com os quatro no lugar, o casco vira um sloop em construção.',
        PAGINA,
        '&3&lTerminando a obra',
        'Clique na obra com cada material, nesta ordem, todos da madeira do casco:',
        '1. Quilha: 8 toras descascadas',
        '2. Convés: 20 tábuas',
        '3. Gurupés: 6 toras descascadas',
        '4. Mastro: 12 toras descascadas',
        '5. Retranca: 8 toras descascadas',
        '6. Vela grande: 16 lãs brancas',
        '7. Bujarrona: 8 lãs brancas',
        '8. Grade da popa: 8 cercas',
        '9. Grade da proa: 8 cercas',
        '10. Âncora: 1',
        '11. Cordame: 8 laços',
        'Na conta final: 34 toras descascadas, 116 tábuas, 24 lãs brancas, 16 cercas, 8 laços, uma âncora e quatro cunhos.',
        'O marco usa o avanço do próprio mod.',
        PAGINA,
        '&3&lControles padrão',
        'Sente-se no lugar do leme, na popa: é ele que pilota.',
        '&eA&r / &eD&r: virar o leme. Ao soltar, o leme volta ao centro.',
        '&eW&r / &eS&r: soltar e caçar a escota da vela grande, abrindo ou fechando a retranca.',
        '&eBotão direito&r nos controles &oSail&r: içar ou recolher a vela grande e a bujarrona.',
        '&eBotão direito&r no &oWindlass&r: soltar ou recolher a âncora. Com ela no fundo, o barco fica parado.',
        '&eShift&r: sair do assento.',
        'O sloop anda com o vento, não com remos: ajuste a vela conforme o vento mostrado na tela.',
    ], deps=['cleat'])

    c.q('cannon', 'C', '&dCanhão a bordo', 'alekiships:cannon', 0, 4,
        ['adv:alekiships:cannon|Fabrique um canhão'], [
        'O sloop tem lugares próprios para canhões: clique num lugar vazio com o canhão (Cannon) e, se ele não encaixar, tente outro. '
        'A munição (Cannonball) sai de ferro, papel e pólvora. Ninguém precisa de guerra para gostar de um estrondo bonito.',
        'Usa o avanço do próprio mod.',
    ])
    c.q('broadside', 'C', '&dSalva completa', 'alekiships:cannonball', 1, 4,
        ['adv:alekiships:full_broadside|Dispare uma salva completa'], [
        'Com três canhões do mesmo lado do sloop, dispare todos juntos.',
        'Usa o avanço do próprio mod.',
    ], deps=['cannon'])
    c.q('wilson', 'C', '&dTripulante de madeira', 'minecraft:armor_stand', 2, 4,
        ['adv:alekiships:armor_stand_on_boat|Leve um suporte de armadura a bordo'], [
        'Todo marinheiro solitário merece companhia. Coloque um suporte de armadura num dos lugares do barco.',
        'Usa o avanço do próprio mod.',
    ])
    c.q('barrel', 'C', '&dPerdido no mar', 'minecraft:barrel', 0, 5,
        ['adv:alekiships:ride_barrel|Viaje dentro de um barril'], [
        'Os lugares do barco aceitam blocos: clique num assento vazio com um baú, barril, fornalha ou bancada e ele vira um '
        'compartimento. Agora experimente viajar dentro de um barril.',
        'Usa o avanço do próprio mod.',
    ])
    c.q('pearl', 'C', '&dPérola Negra', 'minecraft:black_dye', 1, 5,
        ['adv:alekiships:dye_ship_black|Batize um navio preto de The Black Pearl'], [
        'Tinja o barco de preto e batize-o com uma etiqueta de nome: "The Black Pearl". O resto da lenda é com você.',
        'Usa o avanço do próprio mod.',
    ])

    c.image(ROWBOAT_IMG, 4.3, 0.0, 1.6, 2.0, ['Planta do barco a remo', 'A seta aponta para onde olhar ao colocar cada andaime'])
    c.image(SLOOP_IMG, 4.3, 3.7, 2.0, 3.0, ['Planta do sloop', 'A seta aponta para onde olhar ao colocar cada andaime'])
    # Decoração (estaleiro_art.py): título, uma flâmula por fileira, rosa dos ventos e a marinha no rodapé.
    c.image(PLANTA + 'titulo.png', 2.2, -2.2, None, 2.2, ['&3&lEstaleiro', 'Do andaime ao alto-mar'])
    for img, y, dica in (('flamula_remo', -0.7, 'Primeiro barco: seis andaimes e duas forquetas'),
                         ('flamula_sloop', 1.3, 'O veleiro: casco largo, cunhos, âncora e muita madeira'),
                         ('flamula_bordo', 3.3, 'Desafios opcionais para quem já tem um barco')):
        with Image.open(os.path.join(ROOT, 'kubejs', 'assets', 'lilyvale', 'textures', 'quests', 'estaleiro',
                                     img + '.png')) as im:
            w = 0.45 * im.width / im.height
        # alinhadas pela esquerda, logo à direita da linha de dependência que desce em x = 0
        c.image(PLANTA + img + '.png', 0.15 + w / 2, y, w, 0.45, [dica])
    c.image(PLANTA + 'rosa_dos_ventos.png', -2.2, 2.0, None, 2.4, ['O sloop anda com o vento', 'Ajuste a vela conforme o vento mostrado na tela'])
    c.image(PLANTA + 'marinha.png', 2.2, 7.0, 7.0, None, ['Bons ventos, marinheiro'])
    out.append(c)
    return out
