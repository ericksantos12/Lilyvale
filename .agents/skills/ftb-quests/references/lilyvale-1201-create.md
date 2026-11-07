# Lilyvale 1.20.1: lições do capítulo Create Mod

Use estas notas ao editar quests deste repositório. Elas descrevem o Create 6.0.8 e o FTB Quests instalados quando o capítulo foi escrito; confira novamente o jar e as receitas KubeJS se o pack mudar. O capítulo de referência é `config/ftbquests/quests/chapters/create_mod.snbt`.

## Formato observado no pack

- O arquivo pode ter nome legível: `filename: "create_mod"` corresponde a `create_mod.snbt`. O `id` do capítulo, das quests, tasks e recompensas continua sendo hexadecimal único de 16 caracteres.
- Títulos, descrições e títulos de tasks ficam no próprio capítulo (`title`, `description: ["..."]`). Ícones e itens simples são strings, por exemplo `icon: "create:wrench"` e `item: "create:water_wheel"`. Não copie o formato de componentes de item de 1.21+ para este pack.
- Para reconhecer posse no inventário sem consumir, use `type: "item"`, `item: "namespace:id"` e `consume_items: false`. Para quantidades, acrescente `count: 2L` na task. Isso verifica o item possuído; não prova que o jogador o fabricou pessoalmente. Escreva o título como “Obtenha” quando houver outras fontes possíveis.
- No FTB Quests 2001.4.22 instalado, a task `item` lê um ID de item, não uma tag como `#minecraft:logs`. O pack agora tem Item Filters e FTB XMod Compat: para qualquer tronco, preserve o filtro existente `item: { Count: 1, id: "itemfilters:tag", tag: { value: "minecraft:logs" } }` e `consume_items: false`. Não reintroduza o advancement KubeJS removido nem substitua o filtro por `item: "#minecraft:logs"` ou uma espécie específica.
- Recompensas de item usam `type: "item"`, `item: "namespace:id"` e `count` inteiro quando necessário. O capítulo usa `default_hide_dependency_lines: false` para mostrar as ligações.
- A migração posterior removeu os advancements KubeJS e usa tasks nativas. As antigas tarefas de ação de Create hoje verificam itens; controles, sinais, horários e máquinas no inventário não comprovam montagem, viagem ou operação. Não reintroduza referências para `lilyvale:create_mod/progresso`, que não existe mais. Nas F12/F13, revise esses objetivos com detector real validado ou orientação em texto sem task manual; não prometa uma ação só porque a task de item passou.

Exemplos mínimos deste formato:

```snbt
{ id: "6C14000000000002", type: "item", item: "create:water_wheel", consume_items: false }
{ id: "6C14000000000001", type: "item", item: "create:andesite_casing", count: 2L, consume_items: false }
{ id: "6C12000000000031", type: "item", item: "create:controls", consume_items: false, title: "Obtenha controles de trem" }
{ id: "6C13000000000004", type: "item", item: "minecraft:iron_ingot", count: 8 }
```

## Dependências, tarefas e recompensas

- Prefira tasks de item não consumíveis para máquinas e materiais. Reserve avanços para ações que ter o item no inventário não demonstra. Não use checkmarks de gameplay, mesmo quando faltar detector; a exceção é informação/leitura em capítulos como Início.
- Ligue uma quest à anterior quando seu objetivo exige um ingrediente dela, a máquina necessária para produzir um ingrediente intermediário ou uma ação anterior necessária ao uso pedido. Se a task só pede **obter** uma máquina, não exija outra máquina que serve apenas para operá-la depois. Quando o usuário solicitar ordem didática de uso no mesmo sistema, ela é permitida desde que documentada como aprendizado, não ingrediente obrigatório. Deixe sistemas independentes começarem livres e remova ligações transitivas redundantes.
- Confira a cadeia completa no jar instalado e nos scripts que removem/substituem receitas. O EMI e o Ponder são boas dicas para o jogador, mas não substituem a verificação da receita usada pelo pack.
- Siga os contratos da F00: conteúdo novo recebe somente pontos de XP, A=50, M=150 e C/Q=25. Preserve recompensas legadas de item e XP sem rebalanceamento implícito. Não entregue o próprio objetivo seguinte como recompensa nem duplique claims ao mover uma quest. Separe na descrição o que conclui a task do que é orientação de uso.
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
- Confira estaticamente IDs únicos, referências existentes, ausência de ciclos, quantidades, itens do jar, critérios quando usados, coordenadas e linhas. Siga o gate de cada fase para os testes em jogo, incluindo cópia de mundo/equipe com progresso. Não trate checagem estática ou roundtrip como prova de comportamento no mundo.
- O capítulo atual mantém 35 quests e 60 tasks nativas de item sem consumo. Consulte o próprio SNBT para dependências, coordenadas e classificações; a revisão editorial de Create pertence às F12/F13, não à F01.

## Fundação e migração da F01

- Consulte os registros e mapas de IDs em `docs/quests/fases/registros/` antes de continuar uma migração. A F01 registra a fundação; a revisão atual da F02 está em `f02-simplificacao.md`; a divisão PD02/PD03 foi cancelada. O mapa da F01 é histórico; a divisão de Create continua pendente das F12/F13.
- Reserve `0000000000000001` ao livro: o construtor `BaseQuestFile` do JAR instalado usa esse ID interno. Não aloque o ID a grupos, capítulos, quests, tasks ou recompensas.
- Para identidade editorial em 1.20.1, use `subtitle`, `shape`, `hide_details_until_startable: false` e `hide_text_until_complete: false`, confirmados no JAR. A usa círculo azul, M hexágono dourado e C quadrado lilás com texto Opcional; um ramal A também pode continuar tecnicamente opcional.
- Classifique somente capítulos efetivamente revisados e valide os códigos A/M/C. Subtítulos legados de armazenamento são texto livre: extrair uma letra por posição produz classificações falsas. No inventário, deixe a classificação não revisada como `null`.
- Concentre boas-vindas, escolha de trilhas, funcionamento das tasks e legenda A/M/C no capítulo `inicio.snbt`, com cartões curtos, checks manuais opcionais e sem recompensas/dependências. O usuário prefere essa apresentação a uma descrição inicial extensa e dispensou hyperlinks entre capítulos. Mantenha a primeira quest de Primeiros Passos dedicada ao tronco. Esses cartões são informação/confirmação de leitura, não provas de gameplay nem um novo tipo de atividade.
- Evite subtítulos redundantes como “leitura opcional” ou “confirmação manual”. Os cartões de Início não precisam de subtítulo; mantenha os títulos diretos e reserve explicações necessárias à descrição.
- Antes de lançar pelo Prism para testar, examine o pré-lançamento da instância. Nesta instância ele executa Pakku `fetch`; não use o teste de quests para autorizar implicitamente download/resolução de mods. Prefira teste isolado com esse hook desabilitado e sem alterar a configuração original.

## Migração de armazenamento da F02

- A revisão do usuário retirou `armazenamento.snbt`/PD03 e seus 203 objetivos. Mantenha apenas PD02, `mochila_e_organizacao.snbt`/`6A10000000000002`, com sete aquisições; não restaure o catálogo ou seus quatro checks a partir de scripts antigos.
- Faça um mapa único antes de mover e compare tasks/recompensas também como trechos SNBT: JSON normaliza sufixos numéricos e não prova preservação de tipos. A retirada posterior está mapeada em `f02-simplificacao-ids.json`; os sete payloads restantes foram preservados. Não criar clones para preencher espaços.
- A árvore atual tem três ramais compactos sem dependências entre mods. Baú e barril são alternativas: o aplicador exige `one_completed`, não ambos. Mochila antecede o módulo; conector Tom’s antecede o terminal. São relações de aprendizado/uso, não uma alegação sobre ingredientes da receita.
- Consulte `config/sophisticatedcore-common.toml` programaticamente para as flags `enabledItems`. Não despeje a linha inteira no contexto. Em Storage, `dropPacked = false` exige cuidado ao ensinar transporte: quebrar um recipiente não garante um pacote com conteúdo; consulte a fita e teste cópia antes de operar um depósito real.
- Use `python build/f02-simplificacao/verify.py` para a revisão atual; o validador `f02-storage-migration/verify.py` é histórico; preparadores de checkpoint são de execução única. Caso haja processos Java ativos, não copie um save em uso: reutilize uma cópia imutável verificada e explicite que ela não representa o progresso atual.
