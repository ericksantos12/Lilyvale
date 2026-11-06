# F02 — Inventário e melhorias

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **PD02, PD03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Instalação/consulta funcional sem detector confirmado usa projeto pessoal explícito ou texto de obtenção, nunca posse disfarçada de ação.
- Não é necessário resolver nenhum conteúdo de fazenda, chefe ou dimensão.

## Checklist de execução futura

- [ ] Auditar as quests atuais dos três mods e escolher quais ensinam a entrada prática de mochila, recipientes e rede.
- [ ] Preparar o mapa conjunto PD02/PD03 antes de mover qualquer quest: cada ID existente tem um único destino ou referência válida.
- [ ] Entregar as entradas curtas e alternativas de PD02, sem exigir utilizar os três sistemas ao mesmo tempo.
- [ ] Mover consulta/completismo para PD03 mantendo o layout legado compacto, independência dos conversores e texto acessível.
- [ ] Aplicar a migração dos dois capítulos no mesmo lote consistente; não deixar metade do catálogo duplicada como solução temporária.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Contabilizar cada uma das entradas históricas de armazenamento e seus IDs/recompensas, incluindo referências.
- [ ] Testar posse, filtros, upgrades e não consumo; conferir consulta de descrição antes das dependências.
- [ ] Verificar na cópia de equipe que mover uma quest não exige repeti-la nem permite recompensa duplicada.

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
