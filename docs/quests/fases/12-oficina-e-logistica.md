# F12 — Oficina e logística

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **EF01, EF02**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Se já houve migração parcial de Create, usar o mapa atualizado e não a contagem histórica como verdade absoluta.
- Não depende da conclusão de catálogos culinários ou de Advanced Netherite.

## Checklist de execução futura

- [ ] F12.1 — classificar as 35 quests existentes de Create por destino EF01/EF02/EF03 e marcar pré-requisitos reais das receitas do pack.
- [ ] F12.2 — migrar oficina/processos para EF01 e logística para EF02, preservando IDs e progresso.
- [ ] Manter as quests ferroviárias existentes e referências válidas até F13; não apagá-las só porque seu novo capítulo ainda não foi entregue.
- [ ] Revisar objetivos que prometem produzir/automatizar: evento confirmado ou projeto pessoal, nunca simples posse de máquina.
- [ ] Adicionar o ramo curto de Contraption Terminals e os projetos logísticos sem obrigar todas as tecnologias.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar rotação, um processamento, um circuito logístico e o comportamento do terminal de contraption anunciado.
- [ ] Conferir referências para as quests ferroviárias que continuam no legado até F13.
- [ ] Testar progresso/recompensas em equipe migrada e revisar nenhum marco funcional baseado só em item.

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

### EF01 — Oficina de Engenhos

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | A linguagem das peças — liga de andesita e Ponder; I e nota R | Livre |
| A2 | Dar movimento — escolher água ou vento; I da fonte | Alternativas, não água E vento |
| A3 | Levar a rotação — transmissão e ajuste básico; I, uso explicado | Depois da fonte como orientação |
| A4 | A primeira prensa — obter prensa e observar instalação; I/O | Não afirmar produção ainda |
| A5 | Tratar materiais — primeiro resultado de um processo escolhido: moer, lavar ou serrar; I/E | Ramos de escolha, não catálogo de todas as máquinas |
| A6 | Mistura e calor — mistura aquecida e primeiro latão; I/E | Materiais reais do pack |
| A7 | Trabalhar com fluidos — um circuito de bombeamento/enchimento; E ou P, com I das peças só como aprendizagem | Ramo paralelo |
| A8 | Peças com precisão — uma produção de precisão representativa; I/E | Sem exigir o estoque de todas as peças |
| M1 | Uma linha que produz — entrada, processamento e saída operando; P ou detector específico a validar | Não basta ter máquinas no inventário |
| M2 | Fábrica de uso diário — produzir automaticamente algo usado na propriedade; P | O jogador escolhe o produto |
| C1 | A fábrica também pode ser bonita — projeto industrial integrado à construção; P | Opcional |
| C2 | Energia em escala — projeto de vapor ou alternativa avançada; P | Nunca requisito de trens apenas por prestígio |

Redistribuir as 35 quests atuais de Create entre EF01–EF03. Entradas de função muito específica podem continuar como C/R, sem forçar a leitura do manual completo para construir uma primeira máquina.

### EF02 — Logística em Movimento

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Tirar da máquina, guardar no lugar — transporte e filtros; I | Entrada local própria |
| A2 | Um inventário que se move — contraption com armazenamento; I/E conforme o objetivo | Ramo distinto de pacotes |
| A3 | Acesso quando para — introdução ao Create Contraption Terminals; I da peça adequada | Confirmar comportamento parado/móvel e alcance no mod instalado |
| A4 | O primeiro pacote — preparar o empacotamento; I das peças e resultado | Somente receitas reais de papelão/packager |
| A5 | Pedir em vez de procurar — stock ticker/rede de pedidos; I da peça + explicação | Não exigir frogport para todo pedido |
| A6 | Entrega pela rede — fluxo de pedido e entrega; E a validar ou P | Saída funcional, não posse de pacotes quaisquer |
| M1 | Da origem ao destino — um item chega onde será usado; P/E | Pode escolher esteira, pacote ou contraption; não exigir as três |
| C1 | Despensa abastecida — projeto de abastecimento da cozinha/fazenda; P | Receita final e sistema escolhidos livremente |
| C2 | Central de distribuição — projeto maior de pedidos; P | Opcional |

Criar a ponte temática entre tecnologia e vida rural como inspiração, sem exigir tecnologia para concluir o caderno de receitas.
