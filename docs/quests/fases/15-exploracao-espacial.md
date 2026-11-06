# F15 — Exploração espacial

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **AH03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Gate local: não anunciar reserva de oxigênio, combustível carregado ou pressurização por mera posse de uma peça.
- Se faltar detector validado, aprovar P explícito; não iniciar uma integração KubeJS ampla sem autorização.
- Não exige toda a fábrica Create nem todos os equipamentos Advanced Netherite.

## Checklist de execução futura

- [ ] F15.1 — auditar energia, materiais, refino, equipamento, combustível e carregamento de oxigênio reais do pack.
- [ ] F15.2 — entregar primeiro o percurso Terra–Lua com lançamento e chegada verificáveis.
- [ ] F15.3 — entregar orientação de base e marco de suprimento de ar funcional.
- [ ] F15.4 — ampliar em lotes por destinos aprovados, mantendo estações/projetos como escolhas opcionais.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar ciclo de equipamento/oxigênio/combustível e retorno seguro antes de liberar a viagem para usuários.
- [ ] Validar lançamento, chegada à Lua e a condição usada para base funcional.
- [ ] Testar cada destino publicado, incluindo tier/proteção, sem afirmar validação dos destinos ainda pendentes.

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

### AH03 — Diário de Bordo

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Planejar a ida e a volta — manual, perigos e retorno; I do guia ou D | Informações acessíveis antes de viajar |
| A2 | Energia para a missão — primeiro sistema de energia aceito por Ad Astra; I/O | Não exigir fábrica completa de Create |
| A3 | Materiais de voo — liga/compressão necessárias; I/E | Verificar compat com a forja do pack |
| A4 | Combustível não é decoração — refino e abastecimento; E/NBT a validar ou P | Posse do recipiente não comprova combustível carregado |
| A5 | Um traje completo — conjunto básico adequado; I, distinguindo posse/equipamento | Não usar equipamento avançado como primeiro requisito |
| A6 | Respirar fora de casa — carregar oxigênio e verificar reserva; E/NBT a validar ou P | Posse de Oxygen Gear/Loader não basta |
| A7 | Montagem da missão — NASA Workbench, foguete inicial e plataforma; I/O | Apenas os pré-requisitos da receita real |
| M1 | Decolagem — lançamento real; E ou P | Não apenas obter o foguete |
| M2 | Um pequeno passo — chegar à Lua; L | Marco de destaque |
| A8 | Um lar pressurizado — introdução ao distribuidor e sistema de base; I/O e explicação | Depois da viagem como orientação, sem trancar a consulta |
| M3 | Fôlego para ficar — base com suprimento de ar funcional; E validado ou P | Não provar por bloco de distribuidor no inventário |
| C1 | Casa entre as estrelas — base lunar com função escolhida; P | Opcional |
| C2 | Estação orbital — projeto orbital válido; L/E/P conforme detector | Sem exigir por causa do prestígio |
| C3 | A próxima fronteira — preparar melhoria do foguete e visitar um novo destino; I + L | Ramo pós-Lua |
| Q1 | Diário de destinos — uma folha por destino real acessível desta versão, com L | Marte, Vênus, Mercúrio e demais só após conferir sequência e proteção |

Não criar uma quest por parafuso de foguete. Usar poucos nós de processo e marcos por destino. O guia local de Ad Astra e receitas são a fonte para combustível, atmosfera, tier e proteção; não transportar receitas de versões recentes para 1.20.1.
