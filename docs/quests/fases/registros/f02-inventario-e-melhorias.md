# F02 — Inventário e melhorias: execução e migração

**Registro histórico da primeira entrega, substituído pela [simplificação solicitada pelo usuário](f02-simplificacao.md).** O livro atual não contém PD03 nem os quatro checks de gameplay: somente sete aquisições em PD02. Totais, layout e política de checks descritos abaixo pertencem à entrega anterior, não devem ser reimplementados.

**Estado:** implementada e validada estaticamente; aguardando validação em jogo e aceite. **F03 não iniciada.**

O usuário informou a validação da F01 e pediu a próxima fase. A F01/F01.1 foi encerrada com esse aceite, atribuído ao relato do usuário — não a um teste de gameplay observado pelo agente. Esta autorização cobre a F02, não commit/push nem fases seguintes.

[Especificação](../02-inventario-e-melhorias.md) · [Mapa completo de IDs, destinos e evidências](f02-mapa-de-ids.json) · [Índice](../README.md)

## 1. Baseline e preservação

- Branch `dev`, HEAD `1b0d7b7e9318d8af8458c5a8e5cee2bd5c102304`; o Git estava limpo antes da execução. Nenhuma alteração preexistente precisou ser sobrescrita.
- Baseline real: nove grupos, seis capítulos, **294 quests, 343 tasks e 328 recompensas**, incluindo Início. Não se assumiu que o livro ainda tinha somente as 290 quests históricas.
- Snapshot dos oito SNBT em `build/f02-storage-migration/20261106-210828/quests/`; hashes de manifests, scripts e quests protegidos no checkpoint.
- O mapa de origem/destino das **210 quests de armazenamento** foi publicado antes de mover qualquer uma: sete para PD02 e 203 para PD03, com dono único, IDs de tasks/recompensas e hashes dos payloads.
- Tasks, recompensas e dependências das 210 entradas foram preservadas, incluindo consumo, quantidades, NBT, filtros e `one_completed`. Os blocos SNBT das tasks/recompensas também foram comparados literalmente, para não perder tipos numéricos ao converter para JSON.
- Os outros cinco capítulos, a configuração global, grupos, mods, manifests e receitas não foram alterados.

## 2. PD02 — Mochila e Organização

Novo arquivo `config/ftbquests/quests/chapters/mochila_e_organizacao.snbt`, capítulo `6A10000000000002`, grupo **Primeiros Dias**, `order_index: 1` — depois de Primeiros Passos e antes do Caderno.

### Sete aquisições reutilizadas, sem nova recompensa pela mesma posse

| Nó | Quest atual | ID preservado |
| --- | --- | --- |
| A1 | Cabe no passeio — mochila básica | `6A110000000003E9` |
| A2 | Um lugar para cada coisa — módulo de coleta da mochila | `6A110000000003F0` |
| A3a | O baú cresce com a casa — baú Sophisticated | `6A11000000000001` |
| A3b | Ou um barril para o depósito — alternativa independente | `6A11000000000007` |
| A4 | Melhorar sem perder — aplicador básico | `6A11000000000036` |
| A5a | Conectar o depósito — conector de inventário Tom’s | `6A110000000007D1` |
| A5b | Um depósito, uma busca — terminal Tom’s | `6A110000000007D2` |

Os nomes e textos foram adaptados ao aprendizado; tasks e recompensas continuam exatamente as mesmas. Baú/barril são alternativas, a mochila não exige rede, e os componentes Tom’s não dependem de completar módulos Sophisticated. Nenhuma dessas entradas exige concluir cobre ou Início.

### Quatro atividades novas com confirmação transparente

| Nó | Atividade | Critério | XP |
| --- | --- | --- | ---: |
| A6 | Alcançar o que já guardou | Montar a pequena rede, pesquisar e retirar um item; check após o teste, não posse do terminal | 50 |
| M1 | Preparado para sair | Organizar provisões/ferramentas na mochila e conseguir reabri-la; check | 150 |
| M2 | Depósito em funcionamento | Organizar pelo menos duas categorias e testar encontrar/recuperar itens; baús comuns, Sophisticated ou Tom’s aceitos | 150 |
| C1 | Uma mochila para cada aventura | Preparar um kit temático; check opcional, sem exigir cores/tiers/módulos | 25 |

Não foi introduzido detector customizado nem disfarçada posse como instalação/uso. As descrições dizem para marcar depois de realizar a prática. Os checks não se repetem e não dão itens valiosos. Subtítulos usam somente as classificações úteis A/M/C, sem “confirmação manual” ou “leitura opcional”.

A6 depende apenas do conector/terminal; M1, da mochila. M2 e C1 são independentes. O catálogo de upgrades não bloqueia nenhum aprendizado ou marco. O progresso segue a infraestrutura FTB já instalada: não foi prometido ou implementado rastreamento individual dentro da mesma equipe; os gates EQ-01/EQ-02 continuam separados.

## 3. PD03 — Caderno de Melhorias

Reutilizado `config/ftbquests/quests/chapters/armazenamento.snbt`, mantendo o capítulo `6A10000000000001` e o filename. Título **Caderno de Melhorias**, movido para **Primeiros Dias**, `order_index: 2`.

- **203 quests residentes**, todas opcionais, com quadrado e identificação C. Os valores históricos de 50 XP não foram rebalanceados.
- Coordenadas do layout compacto mantidas integralmente: Storage à esquerda, Backpacks no centro e Tom’s à direita. Os espaços deixados pelas sete entradas movidas não foram preenchidos com clones ou links.
- Consulta de texto/detalhes fica acessível antes das dependências. As primeiras entradas restantes de cada área receberam orientação curta sobre o novo destino da introdução.
- Conversores continuam independentes; alternativas e linhas de atalho ocultas foram preservadas.
- Filtros por regex de madeiras do conector e variantes do trim continuam literalmente iguais. Nenhuma variante cosmética virou nova aquisição.
- Dependências de upgrades ainda podem apontar aos mesmos IDs básicos agora residentes em PD02. Essas são referências globais válidas, não cópias; nenhum requisito novo foi criado entre mods.

## 4. Recompensas e totais reais

| Medida | Resultado |
| --- | ---: |
| Quests legadas de armazenamento preservadas | 210 |
| Legadas movidas a PD02 | 7 |
| Legadas mantidas em PD03 | 203 |
| Atividades novas de prática/projeto | 4 |
| Quests finais PD02 / PD03 | 11 / 203 |
| XP histórico preservado | 10.500 |
| XP novo | 375 |
| XP dos dois capítulos após a F02 | 10.875 |
| Total atual do livro | 298 quests, 347 tasks, 332 recompensas |

O livro passa a sete capítulos e nove grupos. Há **13 IDs novos**: um capítulo e quatro conjuntos quest/task/recompensa. Nenhum ID anterior foi removido ou realocado a outro objeto; a lista completa está no mapa.

## 5. Fontes locais conferidas

Os quatro JARs correspondem aos SHA-1 do `pakku-lock.json`:

- `sophisticatedbackpacks-1.20.1-3.26.14.2226.jar`.
- `sophisticatedstorage-1.20.1-1.5.7.2195.jar`.
- `sophisticatedcore-1.20.1-1.5.15.2427.jar`.
- `toms_storage-1.20-1.7.1.jar`.

Receitas realmente inspecionadas, não avanços de desbloqueio:

- Backpacks: `data/sophisticatedbackpacks/recipes/backpack.json` e `pickup_upgrade.json` — mochila básica; módulo feito com base, pistão grudento, linha e redstone.
- Storage: `data/sophisticatedstorage/recipes/generic_chest.json`, `generic_barrel.json`, `oak_chest.json`, `oak_barrel.json` e `basic_tier_upgrade.json` — recipientes básicos e aplicador com alavanca/gravetos.
- Tom’s: `data/toms_storage/recipes/inventory_connector.json`, `storage_terminal.json`, `inventory_cable.json` e `inventory_cable_connector.json`.
- `assets/toms_storage/lang/en_us.json`: os tooltips confirmam que o conector reúne inventários encostados, o terminal é colocado em inventário e cabos/conectores tratam extensões. A introdução compacta não obriga fabricar toda a infraestrutura de expansão; o funcionamento concreto ainda deve ser testado.

`config/sophisticatedcore-common.toml` foi lido como TOML, sem despejar a lista inteira: mochila, módulo de coleta, baú, barril e upgrade básico estão explicitamente habilitados. Não foram encontrados overrides desses namespaces em `kubejs/server_scripts/`.

O bytecode instalado de `BackpackUpgradeRecipe` lê/copia a tag da mochila e ajusta espaços; `StorageTierUpgradeRecipe` transfere a tag ao resultado e ajusta espaços. Isso fundamenta usar as rotas próprias dos mods, **não** uma garantia universal para qualquer receita, inventário vinculado ou NBT arbitrário. A entrada A4 recomenda cópia/teste antes de mexer num depósito em uso.

`config/sophisticatedstorage-common.toml` tem `dropPacked = false`: não se deve ensinar que basta quebrar um baú/barril para transportar tudo como pacote. O texto orienta consultar a fita de empacotamento. Nenhuma configuração foi alterada.

A primeira auditoria delegada falhou por restrição do provedor. Após a correção informada pelo usuário, a segunda tentativa respondeu, mas não concluiu todos os pontos; habilitação dos itens, receitas/tooltips e caminhos de NBT foram conferidos diretamente pelo agente. Não há aprovação independente completa alegada.

## 6. Verificações e mundo de teste

- Parser/roundtrip nativos: oito arquivos da baseline e **nove arquivos finais** aprovados; também passaram os casos de comparação NBT do helper instalado.
- IDs: formato, faixa positiva assinada, reserva do ID interno do livro, unicidade e retenção dos anteriores aprovados.
- Mapa: todas as 210 entradas têm destino único; payloads e coordenadas conferidos contra o arquivo final, sem aquisição/recompensa duplicada.
- Grafo: referências válidas, ausência de ciclos e nenhum requisito de PD03 sobre PD02.
- Layout: comparação com coordenadas anteriores e modelo conservador de caixas `size/2`; zero sobreposições e zero linhas visíveis atravessando outras caixas. O modelo não substitui o renderer do jogo.
- Hashes: somente o SNBT de armazenamento mudou entre os arquivos de jogo protegidos, além do novo capítulo criado. Scripts, manifests e demais quests intactos.
- `git diff --check` passou; nenhum JavaScript foi alterado, portanto ESLint não se aplica.

Havia processos `javaw.exe` ativos. Para não copiar um save em uso, foi reutilizado o snapshot imutável de `Flat` da F01 — **não uma fotografia do progresso atual**. Uma nova cópia foi preparada em `saves/Lilyvale-F02-Legado/`, com 125 arquivos conferidos por SHA-256. O nome interno continua `Flat`; conferir o diretório antes de abrir.

Essa cópia contém 37 entradas em `completed` e 16 em `claimed_rewards` (não são 37 quests). Inclui o barril `6A11000000000007` e o terminal `6A110000000007D2` já concluídos, justamente dois objetivos movidos. Todas as identidades referenciadas continuam existentes. **Isso é verificação offline, não prova de carga/claims em runtime.** Nenhum mundo original ou dado de progresso foi editado.

Validador atual: `python build/f02-storage-migration/verify.py`. Checkpoint, snapshot, bytecode e relatórios estão em `build/f02-storage-migration/`, ignorado pelo Git. Os preparadores são de execução única; não os usar para substituir a baseline.

## 7. Aceite pendente da F02

- [ ] Recarregar com `/ftbquests reload` e conferir os dois capítulos em Primeiros Dias.
- [ ] Testar mochila, baú/barril alternativos, coleta e Tom’s sem consumir itens nas tasks.
- [ ] Confirmar que texto do Caderno abre antes das dependências e que seus conversores/filtros continuam corretos.
- [ ] Na cópia de teste, conferir que barril/terminal concluídos permanecem reconhecidos e que claims antigos não reaparecem.
- [ ] Testar os quatro checks de prática/projeto e suas recompensas, sem prometer detecção automática ou progresso individual.
- [ ] Aprovar visual/funcionamento e dar aceite da F02 antes de avançar à F03.

Não houve lançamento/reload do jogo pelo agente, execução de Pakku, mudança de mods/receitas, commit ou push. A F01 foi aceita pelo usuário; a **F02 permanece aguardando validação em jogo**.
