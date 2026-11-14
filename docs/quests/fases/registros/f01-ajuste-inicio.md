# F01 — Ajuste de apresentação: Início

**Estado:** aceito após o usuário informar “validação realizada, siga para a proxima fase”. A validação em jogo foi relatada pelo usuário, sem evidência por cenário observada pelo agente. Este ajuste foi solicitado após a primeira entrega da F01 e substitui a orientação extensa e os hyperlinks na quest do tronco.

## Alterações

- Novo capítulo auxiliar `config/ftbquests/quests/chapters/inicio.snbt`, título **Início**, no grupo Primeiros Dias, antes de Primeiros Passos (`order_index: -1`). Não substitui nem desbloqueia outro capítulo.
- Quatro cartões curtos e independentes: **Bem-vindo a Lilyvale**, **Escolha seu caminho**, **Como registrar seu progresso** e **Entenda as atividades**.
- Cada cartão tem uma task nativa `checkmark`, opcional e não repetível, sem dependências, recompensas ou hyperlinks. É confirmação de leitura, não prova de ação de gameplay. Esta apresentação informativa foi solicitada explicitamente pelo usuário; não aplica XP de aprendizado a notas de referência.
- A descrição de **Contrato com a floresta** voltou ao texto curto sobre qualquer tronco. Nenhum outro campo das nove quests de Primeiros Passos foi alterado neste ajuste.
- Todos os outros capítulos, IDs anteriores, tasks, recompensas, dependências e coordenadas permanecem iguais ao estado imediatamente anterior a este pedido.

## IDs adicionados

- Capítulo: `6B10000000000001`.
- Quests: `6B11000000000001`, `6B11000000000002`, `6B11000000000003`, `6B11000000000004`.
- Tasks: `6B12000000000001`, `6B12000000000002`, `6B12000000000003`, `6B12000000000004`.

O [mapa da primeira entrega](f01-mapa-de-ids.json) permanece como snapshot histórico daquela revisão. Este registro complementa seus objetos com os nove IDs acima; o inventário atual tem **nove grupos, seis capítulos, 294 quests, 343 tasks e 328 recompensas**. A arquitetura-base de 30 capítulos de conteúdo não ganha um novo mod ou trilha: Início é uma introdução auxiliar.

## Verificação executada

- Snapshot pré-ajuste em `build/inicio-guide/before/`, sem substituir o checkpoint original da F01.
- Comparação estrutural de todos os arquivos anteriores: somente a descrição inicial mudou.
- Oito SNBT passaram no parser/roundtrip nativos; também passaram os casos de comparação NBT do helper existente.
- Novos IDs sem colisões, no formato/faixa válidos; referências e grafo acíclico verificados.
- Quatro checks sem recompensas, sem repetição e sem dependências; nenhuma quest anterior depende deles.
- Posições únicas em grade 2 × 2, passo quatro; nenhum hyperlink no novo capítulo.
- `git diff --check` passou.

**Validador do estado atual:** `python build/inicio-guide/verify.py`; evidência em `build/inicio-guide/result.json`. Os validadores `build/f01-foundation/verify_phase.py` e `verify_handoff.py` estão presos à primeira entrega e seus totais/atalhos antigos; não representam este ajuste.

Na entrega original, o agente orientou aplicar com `/ftbquests reload` e deixou a validação pendente, sem teste no jogo, alteração de progresso, commit ou push. Depois o usuário informou a validação e autorizou a F02; a F01 está encerrada conforme o aceite registrado no cabeçalho.
