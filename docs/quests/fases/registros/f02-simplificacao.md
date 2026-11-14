# F02 — Simplificação solicitada pelo usuário

**Estado:** aplicada e validada estaticamente; aguardando conferência no jogo. Esta revisão substitui a divisão inicial PD02/PD03 e seus quatro projetos com check.

## Pedido aplicado

1. Retirado **Caderno de Melhorias**, incluindo seus 203 objetivos, do livro ativo. O catálogo não foi transferido em massa para Mochila e Organização.
2. Retiradas as quatro quests de check de gameplay, com suas tasks e recompensas. Checks permanecem somente em **Início**, que é informativo. Essa passa a ser uma regra para as próximas fases; propostas antigas de projetos/checks precisam ser reformuladas com detector real ou virar orientação em texto.
3. **Mochila e Organização** conserva sete aquisições, sem consumo, em três ramais compactos. IDs, payloads de tasks e recompensas dessas sete quests foram preservados.

## Dependências e coordenadas

| Ramal | Ordem didática | Coordenadas |
| --- | --- | --- |
| Mochila | Mochila → módulo de coleta | `(0,0)` → `(2,0)` |
| Recipientes | Baú **ou** barril → aplicador básico | `(0,2)` / `(0,4)` → `(2,3)` |
| Tom’s | Conector de inventário → terminal | `(0,6)` → `(2,6)` |

O aplicador usa `one_completed`: basta uma das duas alternativas. Os três sistemas continuam independentes, sem exigir Início, cobre ou completar outro mod. Essas ligações organizam o aprendizado/uso, não declaram que os itens anteriores sejam ingredientes obrigatórios das receitas. A receita direta dos recipientes continua disponível e descrita.

O desenho ocupa dois pontos de largura por seis de altura entre centros, com espaçamento mínimo de dois pontos. As dicas de uso continuam na descrição, sem tarefas de autodeclaração nem referência a uma “próxima atividade” que foi excluída.

## Retirada e progresso

- Snapshot anterior à revisão: `build/f02-simplificacao/before/`.
- [Lista exata dos IDs retirados e mantidos](f02-simplificacao-ids.json), publicada antes da remoção.
- Retirados 207 objetivos: 203 do catálogo e quatro checks. Incluindo capítulo/tasks/recompensas, são 622 identidades retiradas e nenhum ID novo.
- Nenhum arquivo de progresso de mundo foi editado pelo agente. Isso **não** significa preservar objetivos retirados no livro: eles deixam de aparecer, e não se promete retenção/restauração automática de seus registros pelo FTB após um reload. Para preservar esse histórico, guardar uma cópia do mundo antes de recarregar.
- As sete quests mantidas somam 350 XP, com os mesmos IDs e recompensas anteriores. Não foram concedidas recompensas de compensação.

## Verificação

`python build/f02-simplificacao/verify.py` aprovou:

- Oito SNBT no parser/roundtrip nativos; IDs válidos e únicos, sem referências a objetos retirados nem ciclos.
- Comparação com a baseline: demais capítulos intactos; nas sete aquisições, somente texto pontual, coordenadas e dependências foram alterados.
- Nenhum `checkmark` fora de Início.
- Modelo de caixas `size/2`: sem sobreposições e sem linhas atravessando ícones. Ainda exige inspeção no renderer do jogo.
- `git diff --check` sem erros.

O livro ativo agora tem nove grupos, seis capítulos, 91 quests, 140 tasks e 125 recompensas. Os mapas e validadores da primeira entrega da F02 são históricos; o comando acima é o da revisão atual.

Aplicar com `/ftbquests reload`, após guardar backup do mundo caso queira preservar o histórico descartado. Sem teste em jogo pelo agente, commit ou push; F03 não iniciada.
