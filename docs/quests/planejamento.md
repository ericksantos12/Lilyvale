# Lilyvale — plano editorial e visual das quests

**Estado: proposta para implementação futura. Nenhuma quest, receita, configuração ou progresso é alterado por este documento.**

**Execução incremental:** consulte [as fases F00–F18](fases/README.md). As especificações detalhadas de cada capítulo ficam nos arquivos de sua fase; este documento preserva arquitetura, layout comum, políticas e critérios de aceite.

Fonte de escopo: `quest-mods.md`. O plano cobre seus 49 mods em **30 capítulos-base**, organizados nas nove categorias do arquivo atual. Catálogos usam regras de expansão descritas abaixo; o número final de quests só deve ser fechado depois da auditoria de obtenção no survival. Não se trata de 30 mods escolhidos: vários capítulos reúnem mods, enquanto Create e a jornada ao End são divididos por experiência.

## 1. Decisões centrais

1. **O livro é um convite, não um roteiro obrigatório.** Fazenda, casa, criação de animais, música, indústria e exploração têm conquistas próprias. Não há conclusão geral necessária para liberar outras categorias.
2. **Aprendizado é curto e proporcional à mecânica nova.** Uma bancada não justifica um tutorial inteiro. Farmer's Delight recebe uma introdução pequena e um grande caderno opcional de pratos; Vinery recebe uma sequência curta de processamento e um catálogo independente de bebidas.
3. **Marcos reconhecem resultados, não apenas peças.** Possuir uma prensa não comprova uma fábrica; possuir trilhos não comprova uma ferrovia; possuir tanque não comprova oxigênio carregado.
4. **Coleções registram variedade, não quantidade acumulada.** Um prato por receita final, um vinho por identidade, um instrumento por instrumento. Nada de exigir uma pilha, todas as cores ou todos os ingredientes simultaneamente.
5. **Projetos criativos podem ser autodeclarados.** Uma casa acolhedora ou um museu não tem um detector objetivo simples. Nesses casos a quest deve dizer “projeto pessoal — marque quando terminar”, sem fingir detecção automática.
6. **Sem ligação obrigatória entre estilos de jogo.** Aether, Otherside, Lua e dragão não são pré-requisitos editoriais para plantar, decorar, cozinhar ou cuidar de um companheiro. Receitas reais podem exigir materiais de exploração; isso precisa ser informado, não disfarçado como independência mecânica absoluta.
7. **Documentação é consultável antes de concluir atividades.** Requisitos reais podem orientar trilhas, mas textos, receitas e dicas não ficam trancados atrás de completismo.
8. **O escopo atual prevalece sobre a organização anterior.** Armazenamento tem sua entrada em Primeiros Dias. A Jornada até o End é uma nona categoria proposta porque aparece na lista atual; não substituir nem editar os oito grupos já existentes durante o planejamento.
9. **Não somar todos os catálogos como uma barra de “progresso do pack”.** Uma pessoa pode avançar muito em agricultura sem ter qualquer interesse em metalurgia avançada. Evitar também recompensas exclusivas por completar 100% de uma categoria.

## 2. Tipos de atividade e linguagem

| Código editorial | Atividade | Objetivo | Apresentação |
| --- | --- | --- | --- |
| A | Aprendizado | Ensinar um sistema ou uma ação nova e útil | Círculo, acento azul, título curto e instrução prática |
| M | Marco de progressão | Reconhecer um resultado significativo da trilha escolhida | Hexágono maior, acento dourado, resultado explícito |
| C | Desafio ou coleção opcional | Diversidade, completismo, criatividade e metas pessoais | Quadrado, acento lilás, rótulo “Opcional” |
| R | Referência | Consulta sem uma nova obrigação | Painel/nota ou link; não é um quarto tipo de atividade nem uma nova task inventada |

Formas são uma proposta visual a verificar no editor instalado. Texto A/M/C acompanha a forma: não depender apenas de cor. Os códigos deste documento, como `VC04-A2`, são identificadores de planejamento, **não IDs hexadecimais de FTB Quests**.

### Contrato de conclusão

- **I — item:** posse de um exemplar, sem consumo. Prova descoberta/obtenção, não fabricação, uso, plantio, captura ou autoria.
- **O — observação:** ver o bloco/entidade por um mecanismo nativo suportado. Prova encontro, não domesticação, alimentação ou reprodução.
- **E — evento:** ação real ou avanço nativo do mod, somente após inspecionar os critérios e testar a versão. Um avanço de inventário continua sendo apenas posse.
- **L — local:** dimensão, bioma ou estrutura confirmados. Visitar uma dungeon não equivale a concluí-la.
- **K — combate:** derrota real do alvo. Ajustar crédito de equipe e não exigir matar de novo um chefe já vencido.
- **P — projeto pessoal:** checkmark transparente, com checklist de sugestão, sem valor econômico alto.
- **Q — catálogo:** regra de expansão em uma quest independente por identidade elegível; modo I por padrão. Se o texto disser “preparei/cozinhei/capturei”, exige E correspondente ou marcação manual explícita, nunca apenas uma task I renomeada.

Preferir tasks nativas disponíveis. Avanços próprios, hooks KubeJS ou rastreamento persistente são possibilidades futuras, não requisitos silenciosamente adicionados por este plano. Falta de detector não autoriza prometer uma validação que não existe.

## 3. Arquitetura do livro

| Categoria | Capítulo | Mods e propósito | Ênfase |
| --- | --- | --- | --- |
| Primeiros Dias | PD01 — Primeiros Passos | Sobrevivência inicial e cobre; reutilizar o capítulo atual | A, primeiro M |
| Primeiros Dias | PD02 — Mochila e Organização | Sophisticated Backpacks, Sophisticated Storage e Tom's Simple Storage; começo prático | A curta, M de uso |
| Primeiros Dias | PD03 — Caderno de Melhorias | Referência e desafios opcionais dos mesmos três mods | R/C, sem caminho obrigatório |
| Primeiros Dias | PD04 — Tips & Tricks | Gliders, Camerapture, Comforts, Nature's Compass e Carry On | Dicas A independentes, pequenos C |
| Vida no Campo | VC01 — Caderno de Receitas | Farmer's Delight, Farmer's Respite, Ocean's Delight, Veggies Delight e Vintage Delight | Predomínio Q; A apenas dos processos novos |
| Vida no Campo | VC02 — Rotina da Fazenda | Farm & Charm e Harvest with Ease | A de sistemas rurais, M e projetos C |
| Vida no Campo | VC03 — Sabores do Prado | Meadow: criação, laticínios e vida alpina | A curta, Q de queijos e projetos |
| Vida no Campo | VC04 — Vinhedos e Adegas | Vinery: da uva à garrafa | A de processamento e Q de vinhos |
| Vida no Campo | VC05 — Pães e Confeitaria | Bakery | A curta das estações e Q de receitas |
| Vida no Campo | VC06 — À Beira d'Água | Tide | A de pesca e M do diário; C especializados |
| Engenhos e Ferrovias | EF01 — Oficina de Engenhos | Create: energia, processamento e automação | A e M funcionais |
| Engenhos e Ferrovias | EF02 — Logística em Movimento | Create e Create Contraption Terminals | A de sistemas e projetos M/C |
| Engenhos e Ferrovias | EF03 — Estações e Ferrovias | Create, Steam 'n' Rails e Create Railways Navigator | A ferroviária, M de viagem, C de rede |
| O Mundo Lá Fora | MF01 — Atlas de Descobertas | Regions Unexplored e Lootr | Exploração C, poucas dicas A |
| O Mundo Lá Fora | MF02 — Memórias Sob a Terra | Better Archeology | A de escavação/identificação, Q de fósseis |
| O Mundo Lá Fora | MF03 — Caminhos que Conectam | Via Romana | A de infraestrutura, M e projetos C |
| Além do Horizonte | AH01 — Entre as Nuvens | The Aether | A de adaptação, M de expedição e C |
| Além do Horizonte | AH02 — Ecos das Profundezas | Deeper and Darker | A curta, M de exploração e combate isolados |
| Além do Horizonte | AH03 — Diário de Bordo | Ad Astra | A forte até a Lua, M de destinos, C de bases |
| Forja e Legado | FL01 — Fogo, Martelo e Aço | Overgeared | A forte, M de equipamento, C de qualidade |
| Forja e Legado | FL02 — Além da Netherita | Advanced Netherite | A mínima da melhoria, M locais e C opcionais |
| Companheiros e Coleções | CC01 — Pequenos e Grandes Companheiros | Critters and Companions, Naturalist e Hamsters Plus Lite | Encontros e projetos C; A só onde há interação nova |
| Companheiros e Coleções | CC02 — Vida no Estábulo | Icy's Better Horses | A de cuidado/equipamento, M e C de raças |
| Companheiros e Coleções | CC03 — Música para Lilyvale | Immersive Melodies | Q de instrumentos e projetos sociais |
| Criando seu Lar | LR01 — Da Planta à Fachada | Chipped, Construction Sticks e Amendments | Dicas A e projetos C, sem catálogo de blocos |
| Criando seu Lar | LR02 — Um Lar com Vida | Another Furniture, Display Delight, Chimes, Cluttered e Dusty Decorations | Projetos M/C, quase nenhum tutorial |
| Criando seu Lar | LR03 — Prateleira de Abraços | Perfect Plushies | Q apenas do conteúdo obtenível e projetos C |
| A Jornada até o End | JE01 — Olhos do Mundo | End Remastered | A curta e coleção exploratória; 100% é opcional |
| A Jornada até o End | JE02 — O Último Voo | True Ending | Preparação curta, M de combate voluntário |
| A Jornada até o End | JE03 — Ilhas do Vazio | Endercon | Exploração e construção C; sem árvore tecnológica |

**Por que esta divisão:** Farmer e addons compartilham a mesma cozinha e o mesmo álbum; Meadow, Vinery e Bakery têm identidades/processos próprios. Os quatro mods de Create se dividem em oficina, logística e ferrovia, não em quatro tutoriais sobrepostos. Decoração se divide por construir, habitar e colecionar. End Remastered prepara a jornada, True Ending muda o confronto e Endercon sustenta a exploração posterior; nenhum dos três é tratado como “mais um mod de equipamentos”.

## 4. Layout: regras e mapas executáveis como especificação

### 4.1 Regras comuns

- Orientação horizontal da esquerda para a direita. Entrada em `(0, 0)`; não usar uma coluna infinita de pré-requisitos.
- Grade-base com passo **4 pontos**; distância livre mínima planejada de 2 pontos entre centros. Ícones normais com tamanho 1; marcos até 1,3. A checagem final deve considerar dimensões reais e linhas, não só coordenadas únicas.
- A em `y = 0` e, se necessário, `y = 4`; M em `y = 8`; C/projetos em `y = 16`. Para uma trilha A com até seis nós, usar `x = 0, 4, 8, 12, 16, 20`. Trilhas maiores viram dois processos paralelos, não uma serpentina com linhas cruzadas.
- Um marco deve ficar alinhado ao processo que reconhece. Não desenhar linhas apenas para “dar aparência de progressão”. Uma nota ou um link não é dependência.
- Álbuns: painéis de seis colunas; posição local do item `n`, começando em zero: `x = 4 × (n mod 6)`, `y = 4 × floor(n/6)`. Cada painel começa abaixo de um cabeçalho, com quatro pontos de margem; não ligar seus itens uns aos outros.
- Até 36 folhas por painel. Até dois painéis lado a lado, com origens `x = 0` e `x = 32`. Se o inventário final exceder 72 folhas em um capítulo, a implementação deverá propor um anexo adicional ou redivisão, **em vez de comprimir ícones**. Os 30 capítulos são a arquitetura-base; anexos só se a auditoria demonstrar necessidade.
- Grupos de coleção não são desbloqueados ao concluir a trilha A. Podem ser consultados e registrados desde que o jogador encontre o item legitimamente. A trilha A serve para ensinar como obtê-lo.
- Aprendizado e marcos aparecem na primeira área visível; arquivos de consulta e completismo não devem dominar a primeira tela.
- Cenas decorativas discretas: sem texto sobre ícones, sem figuras que pareçam objetivos e sem transformar ilustrações em divisórias gigantes.
- O catálogo legado de armazenamento usa o layout compacto já existente como exceção de migração; não reexecutar o gerador antigo e não recolocar sua altura anterior.

### 4.2 Templates

```text
T — Processo:        A1 → A2 → A3       A4 → A5
                              ↓             ↓
                             M1            M2
                    C1       C2       C3       [sem bloqueio externo]

B — Balcão:          A1       A2       A3       A4    [independentes]
                    M1                 M2
                    C1       C2       C3       C4

G — Galeria:         R: como registrar / como encontrar
                    C01 C02 C03 C04 C05 C06
                    C07 C08 C09 C10 C11 C12 ...       [sem setas]

X — Expedição:       Preparação → Entrada → Experiência local
                                              ↓
                                            Marco
                    Descobertas opcionais em ilhas separadas

P — Projeto:         inspiração / ferramentas
                    Projeto 1       Projeto 2       Projeto 3
                    [cada um tem sua própria checklist autodeclarada]
```

### 4.3 Mapa particular de cada capítulo

| Capítulo | Template e distribuição |
| --- | --- |
| PD01 | T, duas linhas curtas: sobrevivência em cima; oficina de cobre embaixo, com ligação interna somente onde necessária |
| PD02 | B/T: mochila à esquerda, recipientes no centro, rede Tom's à direita; entradas paralelas, três marcos alinhados |
| PD03 | G legado: três áreas já compactadas — Storage, Backpacks, Tom's; títulos “consulta opcional”; nenhuma linha sai para outro capítulo |
| PD04 | B: cinco cartões independentes, em duas linhas; dois projetos pequenos embaixo |
| VC01 | B+G: balcão de preparação no topo; ilhas curtas “infusões” e “conservas”; álbum por família de prato e etiqueta do mod |
| VC02 | T/P: canteiros à esquerda, processamento no centro, cuidado rural à direita; projetos de fazenda embaixo |
| VC03 | T+G: leite → preparo do queijo no topo; coleção de queijos embaixo; casa alpina como projeto lateral |
| VC04 | T+G: cultivo → suco → fermentação → primeira garrafa; maçãs como ramal paralelo; vinho por família de suco em dois painéis inferiores |
| VC05 | T+G: massa → cocção; cobertura/montagem em ramal próprio; álbum de pães, doces e bolos, sem duplicar cada fatia |
| VC06 | T/X: aprender a pescar em cima; diário e progresso no centro; lava, vazio e raridades em ilhas laterais opcionais |
| EF01 | T/P: energia → transmissão → processamento; ramos de sólidos, fluidos e peças de precisão; fábrica funcional no centro inferior |
| EF02 | T/P: mover itens → pacotes → pedidos; acesso a contraptions em ramal distinto; projeto de abastecimento embaixo |
| EF03 | T/P: preparar linha → montar trem → operar viagem; sinalização, Navigator e especializações como ramais |
| MF01 | B/G: leitura do mundo e Lootr no topo; seis famílias de paisagem em ilhas, sem exigir todos os biomas |
| MF02 | T+G: escovar → recuperar → identificar; fósseis em pequena galeria independente |
| MF03 | T/P: caminho → pontos válidos → viagem; projetos de conexão embaixo, sem dependência de ferrovia |
| AH01 | X: chegada e segurança no centro; recursos/estações à esquerda; masmorras à direita; coleções embaixo |
| AH02 | X: preparação no topo, acesso ao Otherside no centro; exploração à esquerda, combate à direita; nunca ligar à fazenda |
| AH03 | X em quatro setores: preparo/oxigênio `(0,0)`, lançamento/Lua `(28,0)`, base `(28,16)`, novos destinos `(56,0)`; não misturar todos os planetas numa cadeia vertical |
| FL01 | T: ferro à esquerda, aço no centro, diamante/netherita à direita; projetos, moldes e qualidade em ramos opcionais inferiores |
| FL02 | T+G: leitura do upgrade → uma melhoria; quatro ligas como pequenos marcos locais, sem exigir todos os equipamentos de cada tier |
| CC01 | B/G: cuidado geral no topo; vida selvagem, pequenos companheiros e hamsters em ilhas próprias; observação não passa por combate |
| CC02 | T/G: vínculo → equipamento → cuidado; galeria das raças embaixo; estábulo e criação como projetos paralelos |
| CC03 | G/P: preservar a galeria independente de 11 instrumentos; orientação de uso no topo e palco/concerto embaixo |
| LR01 | B/P: três cartões de ferramentas; projetos de fachada, paleta e reforma embaixo |
| LR02 | P: núcleos de cozinha, sala, quarto, jardim e espaço comunitário; nenhum deles exige os outros |
| LR03 | G/P: galeria por tema, apenas variantes com obtenção confirmada; exposição embaixo; raridades em canto separado |
| JE01 | G/X: olhos agrupados por origem; orientação de portal no topo; entrada no End como resultado real, não “colete os 16” |
| JE02 | X: preparação voluntária → confronto → vitória; pós-vitória não fecha o resto do livro |
| JE03 | B/P: exploração das ilhas e ruínas em cartões; ponte, rota e observatório como projetos independentes |

## 5. Especificações distribuídas por fase

As especificações detalhadas foram **movidas, sem reescrever seu conteúdo**, para os arquivos de execução incremental. Cada capítulo tem uma única fase responsável; as regras comuns deste documento continuam valendo para todas elas.

[Comece pelo índice de execução e seus critérios de passagem](fases/README.md). Nenhuma fase foi implementada por esta reorganização documental.

| Capítulo | Especificação e fase responsável |
| --- | --- |
| PD01 — Primeiros Passos | [F01 — Fundação e legado](fases/01-fundacao-e-legado.md) |
| PD02 — Mochila e Organização | [F02 — Inventário e melhorias](fases/02-inventario-e-melhorias.md) |
| PD03 — Caderno de Melhorias | [F02 — Inventário e melhorias](fases/02-inventario-e-melhorias.md) |
| PD04 — Tips & Tricks | [F03 — Tips & Tricks](fases/03-tips-and-tricks.md) |
| VC01 — Caderno de Receitas | [F04 — Fazenda e cozinha](fases/04-fazenda-e-cozinha.md) |
| VC02 — Rotina da Fazenda | [F04 — Fazenda e cozinha](fases/04-fazenda-e-cozinha.md) |
| VC03 — Sabores do Prado | [F05 — Sabores artesanais](fases/05-sabores-artesanais.md) |
| VC04 — Vinhedos e Adegas | [F05 — Sabores artesanais](fases/05-sabores-artesanais.md) |
| VC05 — Pães e Confeitaria | [F05 — Sabores artesanais](fases/05-sabores-artesanais.md) |
| VC06 — À Beira d'Água | [F07 — Pesca e música](fases/07-pesca-e-musica.md) |
| EF01 — Oficina de Engenhos | [F12 — Oficina e logística](fases/12-oficina-e-logistica.md) |
| EF02 — Logística em Movimento | [F12 — Oficina e logística](fases/12-oficina-e-logistica.md) |
| EF03 — Estações e Ferrovias | [F13 — Ferrovias](fases/13-ferrovias.md) |
| MF01 — Atlas de Descobertas | [F09 — Paisagens e caminhos](fases/09-paisagens-e-caminhos.md) |
| MF02 — Memórias Sob a Terra | [F10 — Arqueologia](fases/10-arqueologia.md) |
| MF03 — Caminhos que Conectam | [F09 — Paisagens e caminhos](fases/09-paisagens-e-caminhos.md) |
| AH01 — Entre as Nuvens | [F14 — Outras dimensões](fases/14-outras-dimensoes.md) |
| AH02 — Ecos das Profundezas | [F14 — Outras dimensões](fases/14-outras-dimensoes.md) |
| AH03 — Diário de Bordo | [F15 — Exploração espacial](fases/15-exploracao-espacial.md) |
| FL01 — Fogo, Martelo e Aço | [F01 — Fundação e legado](fases/01-fundacao-e-legado.md) |
| FL02 — Além da Netherita | [F16 — Netherita avançada](fases/16-netherita-avancada.md) |
| CC01 — Pequenos e Grandes Companheiros | [F08 — Companheiros e estábulo](fases/08-companheiros-e-estabulo.md) |
| CC02 — Vida no Estábulo | [F08 — Companheiros e estábulo](fases/08-companheiros-e-estabulo.md) |
| CC03 — Música para Lilyvale | [F07 — Pesca e música](fases/07-pesca-e-musica.md) |
| LR01 — Da Planta à Fachada | [F06 — Construir e habitar](fases/06-construir-e-habitar.md) |
| LR02 — Um Lar com Vida | [F06 — Construir e habitar](fases/06-construir-e-habitar.md) |
| LR03 — Prateleira de Abraços | [F11 — Pelúcias](fases/11-pelucias.md) |
| JE01 — Olhos do Mundo | [F17 — Jornada até o End](fases/17-jornada-ate-o-end.md) |
| JE02 — O Último Voo | [F17 — Jornada até o End](fases/17-jornada-ate-o-end.md) |
| JE03 — Ilhas do Vazio | [F17 — Jornada até o End](fases/17-jornada-ate-o-end.md) |

Os códigos de nós A/M/C/R/Q, contratos de conclusão e ressalvas de cada capítulo permanecem nas respectivas especificações. Alterar uma especificação futura exige atualizar sua fase responsável, não criar uma cópia concorrente neste arquivo.
## 6. Política dos catálogos e registro de descobertas

### 6.1 Pratos e bebidas

- Criar **uma folha por produto final distinguível**, com marcação permanente após a descoberta. Nunca pedir ter o cardápio inteiro no inventário de uma vez.
- Preferência inicial: modo **“Receita descoberta”** com I não consumível. Isso permite troca, colaboração, presentes e exploração, compatíveis com o pack cozy.
- Caso a intenção final seja registrar estritamente “eu cozinhei”, implementar E para saída dos processos relevantes (panela, preparo, fermentação, forno etc.). Não supor que evento de crafting cubra máquinas, líquidos, blocos servidos e todos os addons.
- Também é válido usar checkmark manual do álbum, se o jogador preferir registrar experiências pessoais. Deve estar rotulado; recompensa pequena e sem economia explorável.
- Não confundir receita com uma variante de apresentação. Bolo inteiro/fatia, garrafa colocada/na mão e roda/fatia de queijo precisam de regra única de equivalência.
- Excluir ingredientes básicos, recipientes vazios, comida de pet, itens de depuração, spawn eggs, todas as cores de prato e integração com mods ausentes. Intermediários entram apenas se forem também um alimento/produto final com propósito próprio.
- Duplicatas entre addons têm um só registro. Adotar a origem do item final, não o arquivo que repete a receita.
- NBT comum de idade, nome, autor e dano não cria nova coleção. Produtos distintos representados pelo mesmo item/NBT, como certas bebidas de Vintage Delight, exigem inspeção semântica; não usar qualquer `minecraft:potion` como substituto universal.
- A lista em `catalogos-candidatos.md` é uma base extraída das versões instaladas, **não um catálogo final aprovado**. Receitas condicionais precisam ser filtradas pelo conjunto real de mods e pelo reload do pack.

### 6.2 Coleções que NÃO devem ser duplicadas

- **Tide:** usar o diário do próprio mod; FTB Quests acompanha os marcos, não replica todas as espécies.
- **Chipped e decoração:** projetos e paletas, não todos os blocos/cores.
- **Regions Unexplored:** famílias de paisagem com alternativas, não checklist de cada bioma.
- **Advanced Netherite:** ligas e um equipamento escolhido, não todas as ferramentas de todos os tiers.
- **Animais:** encontro/cuidado sem matar, possuir todos ou capturar toda a fauna. Não usar eggs como prova de exploração.
- **Armazenamento:** o manual legado continua opcional; não construir uma segunda cópia dele para virar trilha principal.

### 6.3 Metas agregadas

Marcos por diversidade podem usar 5/10 descobertas, uma seleção de três pratos etc., mas são sugestões de balanceamento, não contadores já disponíveis. Antes de implementar, verificar se o FTB Quests instalado aceita o limiar proposto sem uma dependência “todos”. Se precisar de rastreador customizado, apresentar esse custo; a alternativa segura é projeto pessoal ou marcos menores explícitos.

Nunca colocar uma recompensa de “coleção completa” num evento repetível ou consumir as peças da coleção. Ter 100% do álbum pode ser um título/lembrança, mas não desbloqueia outra profissão.

## 7. Cobertura dos 49 mods e nível de intervenção

A = merece orientação própria; M = sustenta um marco; C = desafio/coleção; R = só consulta naquilo que não apresenta processo novo. O papel indicado é editorial, não obrigação de inventar uma quest de cada tipo para cada mod.

| Mod da lista | Capítulo principal | Papel recomendado |
| --- | --- | --- |
| Sophisticated Backpacks | PD02 / PD03 | A curta, M de preparo e C/R de melhorias |
| Sophisticated Storage | PD02 / PD03 | A curta, M de organização e C/R de módulos |
| Tom's Simple Storage | PD02 / PD03 | A curta de rede, M funcional e R de componentes |
| Gliders | PD04 | Uma dica A e desafio de passeio C |
| Camerapture | PD04 | Uma dica A; projetos fotográficos C transversais |
| Comforts | PD04 | Uma dica A, sem trilha de fabricação |
| Nature's Compass | PD04 | Uma dica A, sem exigir todos os biomas |
| Carry On | PD04 | Uma dica R/A, incluindo limites reais do pack |
| Farmer's Delight | VC01 | A mínima; sobretudo C de pratos |
| Farmer's Respite | VC01 | A curta de infusão; sobretudo C de bebidas |
| Ocean's Delight | VC01 | C de pratos, sem tutorial separado |
| Veggies Delight | VC01 | C de pratos e descobertas agrícolas, sem tutorial separado |
| Vintage Delight | VC01 | A de conservação/fermentação e C de receitas |
| [Let's Do] Farm & Charm | VC02 | A dos processos novos, M rurais, C de cultivos/pratos |
| [Let's Do] Meadow | VC03 | A de laticínios, M de queijaria, C de queijos/ambientes |
| [Let's Do] Vinery | VC04 | A de suco/fermentação, M de safra, C de rótulos |
| [Let's Do] Bakery | VC05 | A curta de preparo/montagem, C de produtos e projeto de padaria |
| Harvest with Ease | VC02 | Uma dica de uso/configuração; sem capítulo próprio |
| Tide | VC06 | A de pesca, M do diário, C de raridades e habitats |
| Create | EF01 / EF02 / EF03 | A e M funcionais; C de projetos |
| Create Contraption Terminals | EF02 | Ramo A curto de acesso à contraption |
| Create: Steam 'n' Rails | EF03 | A das funções distintas; C de especializações ferroviárias |
| Create Railways Navigator | EF03 | A curta de itinerário/consulta, integrada à rede |
| Regions Unexplored | MF01 | C de exploração por famílias; sem árvore tecnológica |
| Better Archeology | MF02 | A de escavação/identificação, M de achado, C de fósseis |
| Via Romana | MF03 | A de rede/caminho, M de conexão, C de projetos |
| Lootr | MF01 | Uma dica de exploração e saque por jogador; sem coleção de baús |
| The Aether | AH01 | A de adaptação, M de masmorra, C de expedição |
| Deeper and Darker | AH02 | A de acesso/adaptação, M de viagem, C de exploração/combate |
| Ad Astra | AH03 | A forte de preparação/oxigênio, M por viagem/base, C de projetos |
| Overgeared | FL01 | A forte e reaproveitada, M de equipamento, C de qualidade |
| Advanced Netherite | FL02 | A pequena de upgrade, M/C de equipamento; depende de auditoria de integração |
| Critters and Companions | CC01 | C de encontros/cuidado; A só das interações distintas |
| Naturalist | CC01 | C de observação e habitat, não “domestique todos” |
| Icy's Better Horses | CC02 | A de vínculo/equipamento, M de passeio, C de criação/raças |
| Hamsters Plus Lite | CC01 | A de habitat/cuidado e C de projeto; sem capítulo separado |
| Immersive Melodies | CC03 | Uma orientação A, coleção C e projetos sociais |
| Chipped | LR01 | Uma orientação A, C de paletas; sem coleção de texturas |
| Another Furniture | LR02 | R/A de funções e C de ambientes |
| Amendments | LR01 | R/A de interações e C de uso criativo |
| Construction Sticks | LR01 | Uma dica A, aplicada nos projetos |
| Display Delight | LR02 | Uma orientação A, C de mesa/vitrine |
| Perfect Plushies | LR03 | C de pelúcias com fontes válidas, sem grind obrigatório |
| Chimes | LR02 | Uma referência de uso e C de ambiente sonoro |
| Cluttered | LR02 | C de interiores, sem tutorial de cada móvel |
| Dusty Decorations | LR02 | C de interiores, sem tutorial de cada adereço |
| End Remastered | JE01 | A curta, M de acesso e C de relíquias |
| Endercon | JE03 | C de exploração/rotas; sem progressão tecnológica inventada |
| True Ending | JE02 | A curta de preparação e M de confronto voluntário |

## 8. Dependências permitidas e proibidas

### Permitidas, quando comprovadas

- Estação → resultado cujo processo usa essa estação.
- Acesso à dimensão → visita/atividade naquela dimensão, **não o contrário**.
- Material/tier real → melhoria que de fato o consome.
- Trilho/estação e materiais de montagem → atividade ferroviária operacional.
- Resultado funcional → desafio de ampliar a mesma construção, se isso não impedir alternativas.

### Não criar

- “Complete Primeiros Dias para ler o resto”.
- “Derrote o dragão para concluir sua fazenda/casa/música”.
- “Faça todos os pratos para liberar Vinery/Bakery”.
- “Complete as 210 entradas de armazenamento para melhorar a base”.
- “Tenha todas as ligas de Advanced Netherite para ir à Lua”.
- “Faça toda a engenharia antes de construir uma ferrovia”.
- “Colecione os 16 olhos para o portal”, quando a mecânica/config exigir uma seleção menor.
- “Capture todas as espécies” para um capítulo de convivência com animais.

Dois sistemas podem ter receitas relacionadas sem uma dependência editorial de conclusão de capítulo. A relação pode ser texto/link, não uma linha de bloqueio.

## 9. Recompensas e cooperação

- **A:** pequena ajuda relacionada ao processo, sem fornecer o objetivo seguinte pronto; sugestão de 25–50 pontos de XP.
- **M:** reconhecimento maior, equivalente entre fazenda, casa, ferrovia e aventura; sugestão de 100–250 pontos de XP ou lembrança cosmética aprovada.
- **C/Q:** recompensa simbólica, sem economia baseada em repetir checkmarks; sugestão de 10–25 pontos de XP por nova folha, com orçamento por álbum a aprovar.
- **P autodeclarado:** preferir reconhecimento sem item valioso. Honestidade e criatividade não devem virar uma estratégia de farm de recompensas.
- Números são uma proposta para conteúdo novo. Não mudar os 50 XP atuais das coleções nem o total histórico do armazenamento sem aprovação de balanceamento e regra de migração.
- Não dar companheiros/artefatos raros ou equipamento final como atalhos de recompensa. Não sortear uma recompensa que conclua a próxima folha de um álbum.
- Decidir explicitamente quais conquistas são individuais e quais são de equipe. Chefes e construções compartilhadas devem reconhecer colaboração; o diário pessoal de receitas/fotos pode continuar individual se o sistema suportar.
- Não converter checkmarks de projeto em requisitos de outras atividades; não há obrigação de provar beleza, tamanho de casa ou qualidade musical a um sistema automático.

## 10. Migração do que já existe

| Conteúdo atual | Tratamento planejado |
| --- | --- |
| Primeiros Passos: 9 quests | PD01, preservar IDs, conteúdo reconhecível e a etapa de polimento antes do cobre |
| Armazenamento: 210 quests | Distribuir aprendizado essencial em PD02 e consulta/C em PD03; mapa de migração por ID, sem cópias de aquisição/recompensa |
| Create: 35 quests | Separar em EF01–EF03 preservando IDs de quests/tasks/recompensas; rever cada objetivo que hoje detecta peça mas cujo título sugere ação |
| Overgeared: 25 quests | FL01; preservar ramos e IDs, qualidade Perfect opcional; adaptar nível editorial sem invalidar progresso |
| Immersive Melodies: 11 quests | CC03; manter independência e identidades; novos projetos não substituem as folhas |

As 290 quests existentes não são lixo a ser apagado nem um número a ser mantido artificialmente no desenho final. A migração começa com preservação de identidades e progresso; qualquer remoção/mesclagem precisa de lista explícita e aceite. Mover uma quest entre capítulos deve ser testado com cópia de um mundo/equipe com progresso, não só com arquivos vazios.

Não gerar IDs finais agora. Na implementação, novos IDs devem ser hexadecimais maiúsculos de 16 caracteres, positivos e até `7FFFFFFFFFFFFFFF`, sem colisão global.

## 11. Auditoria técnica antes de implementar

| Item | Evidência já obtida | O que ainda precisa ser confirmado |
| --- | --- | --- |
| Escopo | `quest-mods.md` contém 49 mods; há versões resolvidas no lockfile | Receitas e configurações efetivamente carregadas após reload |
| Vinery | JAR 1.4.41 com grapevine pot, prensa e receitas de fermentação; wiki do autor sobre pisar/fermentar[12][13] | Tempos, envelhecimento, consumo e rastreamento real de produção; não usar o avanço defeituoso como contador de uvas |
| Farmer/addons | Recipes locais e tipos de panela/fermentação/infusão inspecionados | Catálogo final de pratos, comidas de pet/intermediários, compat e saídas de máquinas |
| Massa compartilhada | `kubejs/server_scripts/farmers_delight_dough.js` troca saídas de massa FD por `create:dough` | Impacto nas receitas de Bakery/Farm & Charm e suporte às tags reais |
| Meadow/Bakery | Processos específicos identificados nos JARs locais | Obtenção, integração e equivalência de fatia/inteiro |
| Tide | Critérios nativos de diário completo/metade presentes no JAR | Integração das tasks de avanço, crédito de captura e uso cooperativo |
| Advanced Netherite × Overgeared | Inspeção estática das receitas de forja e materiais/tags de melhoria | Teste dos quatro níveis e preservação de NBT/dados, sem alterar receitas automaticamente |
| Animais | Raças de Icy's registradas e exemplos de avanço; fauna e hamsters instalados | Doma/reprodução por espécie, identificadores, cooperação, variantes legítimas |
| Perfect Plushies | Itens/loot de blocos presentes; receitas convencionais ausentes na inspeção | Fonte inicial válida de cada pelúcia no survival; comerciante e raridades |
| End Remastered | 16 olhos no JAR e documentação do autor sobre portal com 12[16] | Regras da versão/configuração local, olhos distintos, consumo e estado histórico do jogador |
| True Ending | Avanços locais de entrada/dragão e descrição do combate pelo autor[6] | Vitória, crédito em equipe e interação com Endercon no mundo do pack |
| Endercon | JAR 1.0.2 com worldgen, ruínas e biomas | IDs de locais da versão, chunks existentes e interação do terreno com o combate |
| Projetos funcionais | Resultados editoriais definidos no plano | Detector real, ou P declarado sem fingir automação |
| Layout | Templates, áreas, espaçamento e orientação definidos | Coordenadas finais com número real de folhas; linhas, telas, zoom e navegação no jogo |

## 12. Plano incremental de execução

O plano é executável em **19 fases, F00–F18**, com entregas menores, gates locais, testes e fichas de passagem. A numeração é prioridade de trabalho, não ordem obrigatória para o jogador.

[Índice completo, estados e protocolo de execução](fases/README.md). Todas as fases começam **não iniciadas**; esta edição só separa documentos.

| Fase | Entrega | Capítulos |
| --- | --- | --- |
| [F00](fases/00-contratos-e-preparacao.md) | Contratos e preparação | Preparação |
| [F01](fases/01-fundacao-e-legado.md) | Fundação e legado | PD01, FL01 |
| [F02](fases/02-inventario-e-melhorias.md) | Inventário e melhorias | PD02, PD03 |
| [F03](fases/03-tips-and-tricks.md) | Tips & Tricks | PD04 |
| [F04](fases/04-fazenda-e-cozinha.md) | Fazenda e cozinha | VC01, VC02 |
| [F05](fases/05-sabores-artesanais.md) | Sabores artesanais | VC03, VC04, VC05 |
| [F06](fases/06-construir-e-habitar.md) | Construir e habitar | LR01, LR02 |
| [F07](fases/07-pesca-e-musica.md) | Pesca e música | VC06, CC03 |
| [F08](fases/08-companheiros-e-estabulo.md) | Companheiros e estábulo | CC01, CC02 |
| [F09](fases/09-paisagens-e-caminhos.md) | Paisagens e caminhos | MF01, MF03 |
| [F10](fases/10-arqueologia.md) | Arqueologia | MF02 |
| [F11](fases/11-pelucias.md) | Pelúcias | LR03 |
| [F12](fases/12-oficina-e-logistica.md) | Oficina e logística | EF01, EF02 |
| [F13](fases/13-ferrovias.md) | Ferrovias | EF03 |
| [F14](fases/14-outras-dimensoes.md) | Outras dimensões | AH01, AH02 |
| [F15](fases/15-exploracao-espacial.md) | Exploração espacial | AH03 |
| [F16](fases/16-netherita-avancada.md) | Netherita avançada | FL02 |
| [F17](fases/17-jornada-ate-o-end.md) | Jornada até o End | JE01, JE02, JE03 |
| [F18](fases/18-catalogos-e-aceite-integrado.md) | Catálogos e aceite integrado | Aceite integrado |

F00 e o checkpoint estrutural F01.1 dão a base comum. Depois disso, as frentes podem ser executadas conforme interesse e prontidão; pendências de pelúcias (F11) e netherita avançada (F16) não bloqueiam fazenda/casa. A migração compartilhada de Create (F12/F13) exige mapa de IDs coordenado. F18 só declara o escopo completo quando todas as entregas e validações previstas estiverem cobertas; adiamentos aceitos permitem release parcial, não uma falsa conclusão integral.
### Critérios de aceite do livro futuro

- Todos os 49 mods têm um papel claro; mods pequenos não recebem tutoriais artificiais.
- Fazenda, casa, música e companhia têm marcos relevantes mesmo sem chefes.
- Toda quest que promete ação funcional realmente a detecta ou declara autodeclaração.
- Cada prato/vinho elegível é registrável independentemente; não há entrega consumível do álbum completo.
- Catálogos cosméticos não bloqueiam funcionalidades nem poluem a primeira tela de aprendizado.
- Ninguém precisa repetir objetivos já concluídos apenas porque uma quest foi movida.
- Parser nativo, IDs, referências, ciclos, receitas, filtros/NBT e recompensas passam na validação estática.
- Novo mundo e cópia de mundo com progresso passam nos testes visuais e funcionais, incluindo equipe.

## 13. Rastreabilidade local e limites da pesquisa

Este é um projeto editorial apoiado em inspeção estática, não um relatório de testes em jogo.

- Lista de intenção: `quest-mods.md`.
- Versões e projetos: `pakku-lock.json`, `pakku.json`.
- Estado e IDs existentes: `config/ftbquests/quests/chapter_groups.snbt` e `config/ftbquests/quests/chapters/*.snbt`.
- Regras anteriores de desenho: `.agents/skills/ftb-quests/references/lilyvale-quest-design.md`.
- Exemplos locais: `mods/letsdo-vinery-forge-1.4.41.jar!/data/vinery/recipes/`; `mods/letsdo-farm_and_charm-forge-1.0.14.jar!/data/farm_and_charm/recipes/`; `mods/letsdo-meadow-forge-1.3.25.jar!/data/meadow/recipes/`; `mods/letsdo-bakery-forge-1.1.15.jar!/data/bakery/recipes/`.
- Pesca: `mods/tide-forge-1.20.1-2.1.1-hotfix.jar!/data/tide/advancements/`.
- Integração: `mods/overgeared-forge-1.20.1-1.6.36.jar!/data/minecraft/recipes/netherite_ingot.json`, receitas/tags do `advancednetherite-forge-2.1.3-1.20.1.jar` e scripts KubeJS locais.
- Final de jornada: `endrem_forge-5.3.3-R-1.20.1.jar`, `tru.e-ending-v1.1.0c.jar`, `endercon-1.0.2 [Forge-Neoforge].jar`; considerar a configuração local, não versões novas das páginas públicas.

A notação `arquivo.jar!/caminho` aponta para um recurso dentro do arquivo instalado, não para um arquivo extraído que este plano exige criar. Wikia/documentação recente serve de contexto: se divergir do JAR, configuração ou receita carregada, a versão do pack prevalece. As fontes públicas citadas abaixo foram consultadas por resultados de pesquisa; detalhes numéricos de duração, idade ou balanceamento não foram importados como regra do Lilyvale.

## Sources

[6] https://www.curseforge.com/minecraft/mc-mods/true-ending
[12] https://lets-do.ch/wiki/vinery/grapevine-pot
[13] https://lets-do.ch/wiki/vinery/fermentation-barrel
[14] https://lets-do.ch/wiki/vinery/wine
[16] https://curseforge.com/minecraft/mc-mods/endremastered
