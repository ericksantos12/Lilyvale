# F04 — Fazenda e cozinha

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **VC01, VC02**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Receitas condicionais e saídas não confirmadas ficam fora do lote publicado, com pendência explícita.
- Auditar integração de massas antes de prometer preparo específico; conflito de receita exige decisão separada, não correção silenciosa de KubeJS.

## Checklist de execução futura

- [ ] F04.1 — auditar as receitas carregadas de Farmer e addons, as estações de Farm & Charm e a substituição de massa por Create.
- [ ] F04.2 — entregar primeiro a orientação curta, os marcos rurais e os projetos, já utilizáveis sem catálogo completo.
- [ ] F04.3 — aprovar pratos/bebidas por identidade final e equivalência de apresentação; excluir intermediários, comida de pet e compat ausente.
- [ ] F04.3 — publicar as coleções aprovadas em lotes pequenos por família, sem encadear folhas; manter um inventário aprovado/rejeitado/pendente.
- [ ] Manter as fases seguintes independentes da conclusão pessoal desses álbuns.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Verificar geração de receita no EMI e pelo menos um ciclo real de cada processo publicado.
- [ ] Conferir que cada folha registra descoberta sem consumir e sem exigir posse simultânea do cardápio.
- [ ] Testar marcos de fazenda sem chefes/dimensões como pré-requisitos editoriais e revisar duplicatas entre VC01/VC02.

- [ ] Aplicar o protocolo comum do índice: integridade de arquivos/IDs, contratos de conclusão, visual e teste em jogo correspondente ao lote.
- [ ] Registrar testes executados, evidências, falhas, pendências e aceite do usuário. Validação estática não substitui validação no jogo.
- [ ] Não marcar a fase inteira como concluída se um lote ou um gate continuar pendente. Marcar parcial/em espera conforme o caso.

## Como encerrar ou retomar

Atualizar a linha desta fase no índice e preencher a ficha de passagem abaixo. Um bloqueio local deve identificar o nó/lote afetado e os itens que ainda podem ser entregues com segurança. Não substituir o gate por uma detecção falsa.

| Registro | Preencher durante a execução |
| --- | --- |
| Lote executado | — |
| Arquivos e IDs envolvidos | — |
| Decisões e fontes conferidas | — |
| Testes estáticos | — |
| Testes no jogo / evidência | — |
| Pendências e bloqueios locais | — |
| Próximo lote seguro | — |
| Aceite do usuário | — |

## Especificações dos capítulos

Os blocos abaixo foram movidos do plano original sem reescrever quests, relações ou ressalvas. As regras comuns das seções 1–4 e 6–11 do plano principal continuam obrigatórias.

### VC01 — Caderno de Receitas

**Predomínio: coleções opcionais.** Farmer's Delight, Ocean's Delight e Veggies Delight não viram três tutoriais quase iguais. Farmer's Respite e Vintage Delight só ganham uma ramificação didática quando mudam o processo.

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Bancada de preparo — faca e tábua de corte; I, com usos no EMI | Livre |
| A2 | A primeira panela — panela e fonte de calor compatível; I/O, distinguindo montagem de operação | Livre ou receita real |
| A3 | Uma refeição de verdade — obter o resultado de uma receita simples da panela; I como “descoberta” | Recomendada após A2; não pré-requisito do álbum |
| A4 | Pausa para chá — preparar infraestrutura inicial de infusão de Farmer's Respite; I da estação | Ramo próprio, não exigir cafés e todos os chás |
| A5 | Folhas e infusões — uma bebida de Farmer's Respite; I ou E de preparo validado | Após o processo correspondente, sem tempo numérico presumido |
| A6 | Um pote de possibilidades — estação de fermentação de Vintage Delight; I/O | Ramo curto independente da coleção |
| A7 | Conserva da casa — uma conserva/resultado de fermentação real; I ou E | Não ensinar receitas de compat de mods ausentes |
| M1 | Mesa da casa — reunir escolhas de prato principal e bebida para servir; P, sem detector de “banquete” inventado | Sem meta de catálogo completo |
| C1 | Cardápio da estação — escolher três pratos diferentes para um encontro; P, sem exigir sistema de estações do ano | Opcional |
| Q1 | Receita descoberta: `<prato>` — uma folha por prato final elegível dos cinco mods | Todas independentes e sem consumo |
| Q2 | Bebida descoberta: `<bebida>` — chá, café e bebidas próprias elegíveis | Mesmo álbum, filtro por família/origem |

Organizar o álbum por **refeições**, **lanches**, **sobremesas**, **bebidas** e **conservas**, usando o mod como etiqueta secundária. Não cobrar cada ingrediente ou corte cru. Refeições compartilhadas entre addons têm uma só entrada. FD e addons não dependem do catálogo de Bakery, Vinery ou Farm & Charm.

### VC02 — Rotina da Fazenda

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Um canteiro novo — conhecer cultivos de Farm & Charm; I de uma colheita elegível | Livre; plantio real exige E |
| A2 | Colher sem desmontar — explicar Harvest with Ease e a configuração ativa; D/P de leitura | Sem tutorial falso de fabricação |
| A3 | Preparar a terra — apresentar fertilizante/solo e uso correspondente; I/O | Ramo de produtividade opcional |
| A4 | Água no lugar certo — apresentar irrigação disponível; I/O do aspersor | Não afirmar operação a partir da posse |
| A5 | Do grão à cozinha — primeira produção por crafting bowl/processamento aplicável; I do resultado | Conferir receitas e farinha/massa usadas no pack |
| A6 | Cozinha de campo — uma estação que introduza processo distinto: panela, fogão, assador ou moedor; I/O e R para alternativas | Não quatro tutoriais idênticos em sequência |
| A7 | Cuidar do rebanho — apresentar alimentação e infraestrutura rural suportadas; I/O | Sem matar animal para ensinar cuidado |
| M1 | Horta de uso diário — cultivar uma seleção diversa escolhida pelo jogador; P ou E de colheita a validar | Não exigir todas as sementes |
| M2 | Fazenda que alimenta — colher, processar e servir algo feito com a produção; P com checklist clara | Marco rural equivalente em destaque a um marco industrial |
| C1 | Pomar e canteiros — projeto de pequena propriedade com caminho e área de trabalho; P | Opcional |
| Q1 | Colheita/receita descoberta: `<identidade>` — cultivos e pratos próprios de Farm & Charm | Sem repetir pratos já presentes em outro álbum |

O Jar instalado contém processos de mincer, drying, crafting bowl, pot cooking, roaster e stove; o texto final precisa seguir as receitas habilitadas, não um fluxograma genérico de outro mod. Conferir `data/farm_and_charm/recipes/` no JAR e integração com Bakery.
