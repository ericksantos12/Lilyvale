# F01 — Fundação e legado

**Estado: aguardando validação em jogo e aceite.** A execução foi autorizada explicitamente pelo usuário; F01.1–F01.3 foram implementadas e verificadas estaticamente. O checkpoint de migração F01.1 ainda não está aprovado e a fase não está concluída.

[Registro de execução e gates](registros/f01-fundacao-e-legado.md) · [Mapa real de IDs](registros/f01-mapa-de-ids.json)

**Revisão de apresentação aprovada pelo pedido do usuário:** [Início](registros/f01-ajuste-inicio.md), capítulo auxiliar com quatro checks informativos, substitui a orientação extensa e os atalhos na primeira quest de PD01. Não cria bloqueios ou recompensas.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **PD01, FL01**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita.
- As fases de conteúdo exigem apenas o checkpoint F01.1 validado. Uma pendência na revisão de FL01 não trava o restante do pack; F01 permanece parcial até seus outros lotes passarem.
- Nenhum ID novo é alocado por estes documentos; só durante a implementação efetiva.

## Checklist de execução

- [x] F01.1 — checkpoint estrutural: capturar snapshot de arquivos e IDs reais, preservar estado sujo do Git e preparar cópia de mundo/equipe para testar a migração.
- [x] F01.1 — inventariar as 290 quests históricas como referência, sem assumir que o número permaneceu igual; montar mapa de IDs de capítulo/quest/task/recompensa e origem/destino.
- [x] F01.1 — preparar somente as categorias/identidade visual e regras comuns necessárias à entrega incremental, preservando IDs reutilizáveis; não criar quests ou links quebrados para capítulos futuros.
- [x] F01.2 — revisar PD01 e seus nove objetivos existentes sem duplicar o tutorial vanilla ou bloquear o restante do livro.
- [x] F01.3 — revisar FL01 preservando o processo de Overgeared, qualidade opcional e ausência das bigornas desativadas.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [x] Executar parser nativo, unicidade/faixa dos IDs, referências e ciclos antes e depois da migração.
- [ ] Testar no mundo copiado o progresso de cobre/polimento e ferro/aço; não retirar recompensas já reconhecidas.
- [x] Registrar F01.1 separadamente como aprovado ou pendente; não chamar toda a fase de concluída com testes de FL01 faltando. **F01.1 pendente da validação em jogo da migração.**

- [ ] Aplicar o protocolo comum do índice: integridade de arquivos/IDs, contratos de conclusão, visual e teste em jogo correspondente ao lote.
- [ ] Registrar testes executados, evidências, falhas, pendências e aceite do usuário. Validação estática não substitui validação no jogo.
- [x] Não marcar a fase inteira como concluída se um lote ou um gate continuar pendente. Marcar parcial/em espera conforme o caso.

## Como encerrar ou retomar

Atualizar a linha desta fase no índice e preencher a ficha de passagem abaixo. Um bloqueio local deve identificar o nó/lote afetado e os itens que ainda podem ser entregues com segurança. Não substituir o gate por uma detecção falsa.

| Registro | Preencher durante a execução |
| --- | --- |
| Lote executado | F01.1–F01.3: implementação e validação estática; aceite ainda pendente |
| Arquivos e IDs envolvidos | Quatro SNBT; nove grupos, seis capítulos, 294 quests, 343 tasks e 328 recompensas; [mapa original](registros/f01-mapa-de-ids.json) e [IDs da introdução](registros/f01-ajuste-inicio.md) |
| Decisões e fontes conferidas | Contratos F00, receitas Overgeared e classes FTB instaladas; [registro](registros/f01-fundacao-e-legado.md) |
| Testes estáticos | Oito arquivos no parser/roundtrip nativos; IDs, referências, ciclos, preservação do legado e NBT aprovados |
| Testes no jogo / evidência | Não executados; duas cópias jogáveis com dados reais preparadas |
| Pendências e bloqueios locais | Migração/claims, visual, cobre/polimento, ferro/aço e equipe; pré-lançamento original executa Pakku fetch e foi preservado |
| Próximo lote seguro | Validar F01 nas cópias; não iniciar F02–F18 por inferência |
| Aceite do usuário | Execução autorizada; aceite final não solicitado enquanto os testes estiverem pendentes |

## Especificações dos capítulos

Os blocos abaixo foram movidos do plano original sem reescrever quests, relações ou ressalvas. As regras comuns das seções 1–4 e 6–11 do plano principal continuam obrigatórias.

### PD01 — Primeiros Passos

**Reutilizar o capítulo atual**, sem criar uma segunda sequência vanilla.

| Nós | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1–A4 | Contrato com a floresta → Oficina portátil → Pedra teimosa → Picareta sob medida; manter os quatro objetivos atuais I/O e IDs | Sequência inicial já existente, reavaliada apenas se as receitas mudarem |
| A5–A8 | Primeira expedição → Fogo de oficina → Pedra que aguenta pancada → O brilho vem depois; ensinar aquecimento, bigorna e polimento sem antecipar aço | Mesma trilha técnica atual |
| M1 | Primeira obra de metal — picareta de cobre; I, não prova de autoria | Final local, não chave universal do livro |
| R1 | Orientações transferidas para o capítulo auxiliar Início: quatro cartões de leitura com checks manuais, sem hyperlinks | Independentes, opcionais, sem recompensas ou desbloqueios; ajuste solicitado pelo usuário |

As nove quests atuais permanecem reconhecíveis. A experiência inicial é a única pequena sequência geral; PD02, PD04 e os demais temas não devem ser trancados por sua conclusão.

### FL01 — Fogo, Martelo e Aço

Reaproveitar as 25 quests atuais de Overgeared como base. Os nove estágios do cobre ficam em PD01; aqui não se recomeça a forja do zero.

| Conjunto | Tratamento futuro |
| --- | --- |
| A — Ferro | Ferro para a oficina → mais calor → ferro no ponto → acabamento; explicar apenas diferenças do cobre |
| M — Primeira ferramenta de ferro | Manter “Um cabo, novos caminhos” com ID atual e contrato I |
| A — Aço | Forno/processamento → material bruto → lingote; depender somente das estações reais |
| M — Aço útil | Uma ferramenta de aço escolhida, sem exigir kit de cada ferramenta |
| A — Fundição/projetos | Ramais próprios para molde, projeto e fundição; não exigir todos para uma melhoria que não os usa |
| M — Diamante e netherita | Manter resultados importantes como finais locais; não dependências universais de outras categorias |
| C — Qualidade | Perfect como objetivo de maestria voluntário, nunca requisito da ferramenta comum |
| C — Especializações | Armadura, ferramentas secundárias e flechas; não encadear todas as profissões da oficina |

Preservar todos os IDs, inclusive dos conteúdos que passem a consulta/C. Não voltar a usar as bigornas Tier A/B desativadas. Não entregar uma recompensa que já conclua a próxima etapa de forja.
