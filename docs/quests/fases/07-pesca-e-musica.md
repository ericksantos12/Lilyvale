# F07 — Pesca e música

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **VC06, CC03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Os dois lotes são independentes. Falha no detector do diário não impede o projeto musical.
- Atividades dimensionais de pesca podem ter validação adiada explicitamente, sem bloquear os objetivos de águas comuns.

## Checklist de execução futura

- [ ] F07.1 — preservar os 11 instrumentos existentes e suas recompensas; acrescentar apenas a orientação única e projetos musicais previstos.
- [ ] F07.2 — confirmar os avanços/critérios do Tide e entregar a trilha curta de equipamento e captura.
- [ ] Usar o diário nativo para a coleção de espécies e FTB Quests para marcos; não gerar um segundo álbum de peixes.
- [ ] Separar pesca comum das atividades tardias em lava/vazio; marcar conteúdo ainda não testado como pendente, sem inventar detector.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Conferir IDs/recompensas/progresso dos instrumentos antes e depois da alteração.
- [ ] Testar captura real versus posse e os marcos de diário que forem publicados.
- [ ] Garantir que projetos musicais aceitam solo e que o diário completo não bloqueia outros capítulos.

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

### VC06 — À Beira d'Água

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Um diário na mochila — obter o Fishing Journal; I | Livre |
| A2 | Preparar a linha — vara e uma modificação útil/iscas; I | Sem exigir todas as varas |
| A3 | Ler a água — diário, Fish Finder e condições de pesca; I mais R de uso | Não duplicar a wiki inteira na quest |
| A4 | A primeira captura — pescar de verdade; E do sistema de pesca | Posse de peixe não prova captura |
| M1 | Histórias de pescador — primeiro grupo de descobertas registrado no diário; E só se houver critério adequado | Se não houver, não inventar um contador |
| M2 | Metade do diário — avanço nativo de metade concluída, depois de testado | Marco opcional; não trava outras atividades |
| C1 | Diário completo — avanço nativo de conclusão do Tide | Opcional de longo prazo |
| C2 | Uma captura lendária — avanço nativo de captura, não item entregue por recompensa | Opcional |
| C3 | Águas improváveis — pesca em lava; E nativo | Ramo tardio, não exigência da pesca comum |
| C4 | Pescaria no vazio — E nativo do Tide | Ramo do End separado do diário rural básico |
| C5 | Cantinho de pescaria — construir um píer/refúgio; P | Pode ser concluído sem peixe raro |

**Não criar outra quest para cada peixe se o diário já faz esse trabalho melhor.** As coleções ficam no Tide; FTB Quests celebra as etapas. O JAR contém `tide:journal_halfway_complete` e `tide:journal_complete` nos critérios de seus avanços; IDs de avanço e integração ainda precisam de teste.

### CC03 — Música para Lilyvale

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | A primeira nota — orientação única para tocar um instrumento; D/I ou E se houver | Não exigir um instrumento específico como entrada |
| Q1 | Um novo timbre: `<instrumento>` — preservar as 11 quests independentes já implementadas | I, sem consumo/NBT, sem cadeia entre instrumentos |
| C1 | Um palco para a vila — construir espaço para música; P | Opcional |
| C2 | Uma noite de música — tocar sozinho ou com outras pessoas; P | Não exigir multiplayer para concluir |

Manter os 50 XP atuais por instrumento durante a primeira migração; qualquer rebalanceamento geral deve ser aprovado em separado.
