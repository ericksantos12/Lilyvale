# Lilyvale 1.20.1: lições do capítulo Create Mod

Use estas notas ao editar quests deste repositório. Elas descrevem o Create 6.0.8 e o FTB Quests instalados quando o capítulo foi escrito; confira novamente o jar e as receitas KubeJS se o pack mudar. O capítulo de referência é `config/ftbquests/quests/chapters/create_mod.snbt`.

## Formato observado no pack

- O arquivo pode ter nome legível: `filename: "create_mod"` corresponde a `create_mod.snbt`. O `id` do capítulo, das quests, tasks e recompensas continua sendo hexadecimal único de 16 caracteres.
- Títulos, descrições e títulos de tasks ficam no próprio capítulo (`title`, `description: ["..."]`). Ícones e itens simples são strings, por exemplo `icon: "create:wrench"` e `item: "create:water_wheel"`. Não copie o formato de componentes de item de 1.21+ para este pack.
- Para reconhecer posse no inventário sem consumir, use `type: "item"`, `item: "namespace:id"` e `consume_items: false`. Para quantidades, acrescente `count: 2L` na task. Isso verifica o item possuído; não prova que o jogador o fabricou pessoalmente. Escreva o título como “Obtenha” quando houver outras fontes possíveis.
- No FTB Quests 2001.4.22 instalado, a task `item` lê um ID de item, não uma tag como `#minecraft:logs`. O filtro de tag da interface requer FTB Filter System e FTB XMod Compat, ausentes neste pack. Para “qualquer tronco”, preserve o avanço `minecraft:inventory_changed` com a tag `minecraft:logs`; ele detecta a posse sem consumir o item. Não substitua por `item: "#minecraft:logs"` nem por uma espécie específica.
- Recompensas de item usam `type: "item"`, `item: "namespace:id"` e `count` inteiro quando necessário. O capítulo usa `default_hide_dependency_lines: false` para mostrar as ligações.
- Para uma ação real, use task de avanço com `advancement: "lilyvale:create_mod/progresso"` e `criterion: "nome"`. O JSON correspondente em `kubejs/data/lilyvale/advancements/create_mod/progresso.json` reúne os critérios sem `parent`; cada task aponta para seu próprio critério. Use gatilhos confirmados na versão instalada e retire critérios sem tasks. No capítulo atual são sete ações: montar trem, instalar sinal, instruir condutor, mostrar chegada, receber pacote no frogport, fazer pedido no stock ticker e disparar pedido no factory gauge.

Exemplos mínimos deste formato:

```snbt
{ id: "6C14000000000002", type: "item", item: "create:water_wheel", consume_items: false }
{ id: "6C14000000000001", type: "item", item: "create:andesite_casing", count: 2L, consume_items: false }
{ id: "6C12000000000031", type: "advancement", advancement: "lilyvale:create_mod/progresso", criterion: "trem", title: "Monte um trem na estação" }
{ id: "6C13000000000004", type: "item", item: "minecraft:iron_ingot", count: 8 }
```

## Dependências, tarefas e recompensas

- Prefira tasks de item não consumíveis para máquinas e materiais. Reserve avanços para ações que ter o item no inventário não demonstra. Evite checklists manuais para etapas verificáveis.
- Ligue uma quest à anterior quando seu objetivo exige um ingrediente dela, a máquina necessária para produzir um ingrediente intermediário ou uma ação anterior necessária ao uso pedido. Se a task só pede **obter** uma máquina, não exija outra máquina que serve apenas para operá-la depois. Deixe trilhas independentes começarem sem dependência e remova ligações transitivas redundantes.
- Confira a cadeia completa no jar instalado e nos scripts que removem/substituem receitas. O JEI e o Ponder são boas dicas para o jogador, mas não substituem a verificação da receita usada pelo pack.
- Dê recompensas úteis para a próxima etapa da trilha, em quantidades coerentes. Não entregue como recompensa o próprio resultado exigido pela quest seguinte se isso a concluir automaticamente ao desbloquear. Separe na descrição o que conclui a task do que é apenas orientação de uso.
- Preserve IDs de quests, tasks e recompensas ao corrigir ordem, texto ou layout para não descartar progresso existente. Crie IDs novos apenas para novos objetos ou para uma task realmente substituída.

## Receitas que decidiram o grafo do Create

| Sistema | Fato observado e consequência |
|---|---|
| Revestimentos | `kubejs/server_scripts/create_construction.js` troca os três casings: liga/chapa + qualquer tronco rende 2. `kubejs/server_scripts/trains.js` troca o railway casing: golden sheet + deepslate rende 2. A prensa é relevante para os casings de cobre, latão e ferrovia. |
| Energia e prensa | Water wheel e windmill bearing usam shaft, sem andesite casing. A mechanical press usa andesite casing. Uma fonte de rotação é necessária **para usar** a prensa, mas não para concluir uma task que só pede a prensa no inventário. |
| Processamento | O millstone transforma pedregulho em cascalho; isso ajuda na lavagem, mas não é ingrediente do encased fan. Serra e broca não exigem o ventilador. Fluid pipe/pump não exigem copper casing; hose pulley e spout exigem, mas não exigem a etapa anterior de tubos ou tanque. |
| Vapor | A receita do steam engine usa andesite alloy, bloco de cobre e golden sheet. Tanque/queimador são relevantes para a caldeira em funcionamento, não para obter o item do motor. |
| Papelão e packager | `create:mixing` faz polpa com quatro itens da tag `create:pulpifiable` (bambu, cana-de-açúcar ou mudas) e água. A prensa faz cardboard; quatro cardboard fazem cardboard block; o bloco entra no packager. Portanto, mixer e prensa são pré-requisitos de produção legítimos para essa trilha. |
| Esquemáticos | Schematic table usa pedra lisa e lajes de madeira; schematicannon usa blocos de ferro, troncos, pedra lisa e dispenser. Nenhum exige sturdy sheet ou peças de contraptions: a trilha pode começar sem essas dependências. |
| Sturdy sheet | `kubejs/server_scripts/create_processing.js` altera o esmagamento da obsidiana para entregar powdered obsidian sem devolver obsidiana. A sturdy sheet exige esse pó, preenchimento com lava e prensagem; crushing wheels e spout justificam duas dependências. |
| Trens e logística | A montagem de tracks usa deployers e prensa; track station usa railway casing. A rede de chegadas usa trem e display link. Para atender pedidos do stock ticker, a trilha usa packager; a entrega por frogport é opcional. Factory gauge usa stock link e precision mechanism. |

## Layout e checagem

- Planeje um grafo acíclico antes de posicionar ícones. No capítulo Create, use coordenadas em múltiplos de 2 e posições únicas; cada dependência visível deve compartilhar `x` ou `y` com a quest predecessora para produzir linha reta horizontal ou vertical. Muitas ramificações de um mesmo nó podem fazer linhas passarem atrás de outros ícones; avalie cruzamentos e legibilidade em vez de criar bloqueios artificiais apenas para simplificar o desenho.
- Confira estaticamente IDs únicos, referências existentes, ausência de ciclos, quantidades, itens do jar, critérios JSON, coordenadas e linhas. Preserve a preferência do usuário quanto ao teste no jogo: neste trabalho, a inspeção visual e dos gatilhos ficou para os prints dele. Não trate a checagem estática como prova de comportamento no mundo.
- O capítulo aceito aqui tem 35 quests, 53 tasks de item sem consumo, sete tasks de ação e 37 dependências. O layout em grade de 2 tem um cruzamento entre trem e logística. Consulte o próprio SNBT para o grafo e as coordenadas atuais, pois esses números podem mudar com novas quests.
