# F11 — Pelúcias

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **LR03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Gate local obrigatório: fonte de survival por identidade.
- Esta fase não bloqueia LR01/LR02, música, fazenda, engenharia ou dimensões.

## Checklist de execução futura

- [ ] Resolver primeiro a fonte inicial de cada pelúcia candidata, verificando comerciante/registros/configuração e não apenas loot de quebrar bloco.
- [ ] Separar identidades aprovadas, rejeitadas e pendentes; não exigir itens de autor/administrativos.
- [ ] Entregar primeiro marco, galeria apenas de fontes válidas e projeto de exposição.
- [ ] Se nenhuma fonte confiável estiver aprovada, manter a fase em espera e não publicar objetivos impossíveis.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Obter legitimamente uma amostra de cada tipo de fonte publicado.
- [ ] Conferir que variantes/recompensas não duplicam registros e que raridades são opcionais.
- [ ] Registrar claramente o que permanece pendente e impedir sua inclusão na coleção publicada.

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

### LR03 — Prateleira de Abraços

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| R1 | Como conseguir pelúcias — explicar fonte de survival efetivamente confirmada | Obtenção ainda precisa ser auditada; loot de quebrar bloco não é fonte inicial |
| M1 | Um abraço na estante — obter a primeira pelúcia legítima; I | Marco pequeno e local |
| Q1 | Amigo de pano: `<pelúcia>` — uma folha por identidade com fonte válida | Ignorar dados irrelevantes; raridades sem cadeia obrigatória |
| C1 | Coleção com carinho — montar exposição pessoal; P | Não exigir a coleção completa |

O JAR local tem vários itens/pelúcias e não contém receitas convencionais catalogadas nesta inspeção. Verificar comerciante, tabelas, registros e compat antes de aprovar a lista final. Itens de autor, raros ou administrativos não entram só por aparecerem no criativo.
