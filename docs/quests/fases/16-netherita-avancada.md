# F16 — Netherita avançada

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **FL02**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado; mapear relação com FL01 sem exigir concluí-lo como jogador.
- Gate local obrigatório: integração funcional e preservação de dados.
- Não bloqueia Ad Astra, dragão, engenharia, fazenda ou casa.

## Checklist de execução futura

- [ ] Revalidar a ponte de receita entre Overgeared e Advanced Netherite nas versões/configurações atuais.
- [ ] Testar as melhorias e a preservação de qualidade, encantamentos, nome, dano, criador e demais dados relevantes.
- [ ] Somente após a auditoria aprovada, entregar a orientação curta, primeiro marco e desafios de ligas.
- [ ] Se a integração exigir rebalanceamento/alteração de receita, apresentar a decisão ao usuário e manter esta fase em espera.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Executar a matriz de melhorias aprovada em cópia de ambiente, não apenas conferir receitas JSON.
- [ ] Comparar dados do equipamento antes/depois, incluindo casos com encantamento e qualidade.
- [ ] Confirmar que não se exige cada peça de todos os tiers e que nenhuma receita foi alterada sem autorização.

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

### FL02 — Além da Netherita

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Melhorar o que já acompanha você — explicar ligas e papel da bancada de ferraria; D/I | Consulta livre; materiais tardios continuam tardios |
| A2 | Primeira liga avançada — obter o material de Netherite-Iron; I | Dependência da receita real, não “termine todas as quests Overgeared” |
| M1 | Uma peça com legado — aplicar primeira melhoria de equipamento; I como peça obtida, E se exigir aplicação pessoal | Confirmar preservação de dados antes |
| C1–C4 | Metalurgia avançada — obter/experimentar as ligas Iron, Gold, Emerald e Diamond, uma meta por identidade | Sem exigir todas as armas e armaduras de cada tier |
| C5 | Ferramenta de profissão — escolher um equipamento útil para fazenda, mineração ou aventura; P/I | Não exigir combate para justificar uma enxada |

**Gate de implementação:** a integração com Overgeared não está aprovada só porque ambos carregam. No JAR local, Overgeared produz o lingote vanilla de netherita por forja; Advanced Netherite usa tags e smithing para suas melhorias. Testar receitas, preservação de qualidade, encantamentos, nome, dano, dados do criador e eventuais modificadores. Se houver conflito, deixar FL02 em espera e apresentar uma decisão de integração; não reequilibrar receitas dentro da implementação das quests sem autorização.
