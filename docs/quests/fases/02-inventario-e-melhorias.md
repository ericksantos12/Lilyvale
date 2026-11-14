# F02 — Inventário e melhorias

**Estado: revisão implementada e aguardando validação em jogo/aceite.** O usuário retirou PD03 e os quatro checks de gameplay. O estado atual é somente PD02, com sete aquisições, layout compacto e três ramais com dependências didáticas. [Revisão atual](registros/f02-simplificacao.md) · [IDs retirados/mantidos](registros/f02-simplificacao-ids.json).

[Registro de execução](registros/f02-inventario-e-melhorias.md) · [Mapa conjunto de IDs e evidências](registros/f02-mapa-de-ids.json)

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulo ativo: **PD02 — Mochila e Organização**. **PD03 foi cancelado pelo usuário**, sem transferir seus 203 objetivos de volta a PD02. A divisão inicial em dois capítulos é histórica, não o desenho atual.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Gameplay exige detector real; se não houver detector, manter orientação em texto, sem check de confirmação nem posse disfarçada de ação. Checkmarks ficam restritos aos capítulos informativos.
- Não é necessário resolver nenhum conteúdo de fazenda, chefe ou dimensão.

## Checklist da primeira entrega — histórico, superado pela revisão

- [x] Auditar as quests atuais dos três mods e escolher quais ensinam a entrada prática de mochila, recipientes e rede.
- [x] Preparar o mapa conjunto PD02/PD03 antes de mover qualquer quest: cada ID existente tem um único destino ou referência válida.
- [x] Entregar as entradas curtas e alternativas de PD02, sem exigir utilizar os três sistemas ao mesmo tempo.
- [x] Mover consulta/completismo para PD03 mantendo o layout legado compacto, independência dos conversores e texto acessível.
- [x] Aplicar a migração dos dois capítulos no mesmo lote consistente; não deixar metade do catálogo duplicada como solução temporária.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [x] Registrar a retirada autorizada de 203 objetivos de PD03 e quatro checks; sete aquisições mantêm seus IDs/tasks/recompensas. Não se alega preservação ativa de objetivos descartados.
- [ ] Testar as sete aquisições, não consumo, desbloqueios alternativos e consulta antes das dependências.
- [ ] Conferir o reconhecimento do progresso das sete quests mantidas; objetivos retirados não estarão mais visíveis.

- [ ] Aplicar o protocolo comum do índice: integridade de arquivos/IDs, contratos de conclusão, visual e teste em jogo correspondente ao lote.
- [ ] Registrar testes executados, evidências, falhas, pendências e aceite do usuário. Validação estática não substitui validação no jogo.
- [x] Não marcar a fase inteira como concluída se um lote ou um gate continuar pendente. **F02 aguardando validação em jogo.**

## Como encerrar ou retomar

Atualizar a linha desta fase no índice e preencher a ficha de passagem abaixo. Um bloqueio local deve identificar o nó/lote afetado e os itens que ainda podem ser entregues com segurança. Não substituir o gate por uma detecção falsa.

| Registro | Preencher durante a execução |
| --- | --- |
| Lote executado | Revisão: somente sete aquisições em PD02, sem checks de gameplay |
| Arquivos e IDs envolvidos | `mochila_e_organizacao.snbt` mantido; `armazenamento.snbt` removido; lista de identidades arquivada no registro da simplificação |
| Decisões e fontes conferidas | Receitas, tooltips, habilitação e caminhos de NBT dos JARs instalados; posse não prova instalação/uso |
| Testes estáticos | Oito SNBT no parser/roundtrip; IDs restantes, payloads, referências, ciclos e geometria aprovados |
| Testes no jogo / evidência | Não executados pelo agente; cópia histórica real preparada em `saves/Lilyvale-F02-Legado` |
| Pendências e bloqueios locais | Conferir visual, dependências e progresso das quests mantidas; EQ-01/EQ-02 sem nova implementação |
| Próximo lote seguro | Validar F02 e obter aceite antes da F03 |
| Aceite do usuário | Execução autorizada; aceite da entrega F02 ainda pendente |

## Especificações originais — históricas, não implementar checks ou PD03

Os blocos abaixo preservam a proposta original. A revisão atual prevalece: mochila → coleta; baú ou barril → aplicador; conector Tom’s → terminal, sem dependências entre sistemas. Os nós A6/M1/M2/C1 manuais e o PD03 abaixo foram cancelados. Consulte o registro da simplificação para coordenadas, IDs e testes atuais.

### PD02 — Mochila e Organização

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Cabe no passeio — obter a primeira mochila; I | Livre; reutilizar a quest correspondente do catálogo |
| A2 | Um lugar para cada coisa — configurar um filtro ou módulo simples; I do módulo mais instrução, E apenas se houver detector de instalação | Sugestão após A1, não bloquear outros sistemas |
| A3 | O baú cresce com a casa — obter baú/barril Sophisticated básico; I | Livre, independente da mochila |
| A4 | Melhorar sem perder — apresentar conversão e cuidados com conteúdo/NBT; um upgrade básico I | Somente pré-requisito material verdadeiro |
| A5 | Um depósito, uma busca — obter conector/controlador e terminal Tom's representativos; I, sem chamar isso de rede funcional | Entrada própria do Tom's |
| A6 | Alcançar o que já guardou — operar uma consulta/retirada pela rede; E a validar; alternativa P explicitamente manual | Não usar só posse do terminal como prova |
| M1 | Preparado para sair — mochila equipada/organizada; E se possível, caso contrário P | Resultado pessoal da faixa da mochila |
| M2 | Depósito em funcionamento — armazenar e recuperar itens por sua organização escolhida; P com checklist curta | Não exigir Storage e Tom's simultaneamente |
| C1 | Uma mochila para cada aventura — configurar uma mochila temática; P | Opcional, sem exigir todas as cores ou tiers |

Um jogador que usa só baús não precisa montar Tom's; um jogador que usa Tom's não precisa terminar o catálogo de módulos Sophisticated.

### PD03 — Caderno de Melhorias

Este capítulo **não recebe uma sequência nova de 210 tarefas**. É o destino editorial do catálogo já existente: o aprendizado essencial vai para PD02, e o restante permanece consultável como R/C. Reutilizar IDs e links, não duplicar a mesma aquisição para ganhar XP duas vezes.

| Conjunto | Tratamento futuro |
| --- | --- |
| Recipientes e capacidade | Comparativo consultável; obtenção dos tiers como C, nunca obrigação para a próxima categoria |
| Módulos de função | Uma entrada por função real; cosméticos agrupados; consulta antes do desbloqueio |
| Conversores | Manter independentes quando são consumíveis/rotas alternativas, não uma longa escada obrigatória |
| Rede Tom's e ferramentas | Mostrar quando cada peça resolve um problema; não exigir fabricar cada variante de madeira |
| Melhorias opcionais | Recompensa simbólica; não criar “domine todos os upgrades” como requisito externo |

Na migração: manter as 210 quests atuais em um mapa de origem/destino. Se algumas forem movidas a PD02, o arquivo de consulta terá essas referências ou menos quests residentes; não serão 210 antigas mais cópias novas.
