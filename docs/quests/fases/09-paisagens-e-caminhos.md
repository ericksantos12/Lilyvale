# F09 — Paisagens e caminhos

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **MF01, MF03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- IDs de biomas/locais e regras de viagem precisam ser confirmados para os objetivos usados.
- Se o detector de Via Romana exigir integração não aprovada, usar P declarado ou adiar essa atividade; MF01 pode ser entregue.

## Checklist de execução futura

- [ ] Agrupar alternativas reais de biomas em famílias acessíveis, respeitando geração e chunks existentes.
- [ ] Entregar a nota de Lootr sem transformar o mod em uma sequência de obtenção de baús.
- [ ] Auditar Via Romana e implementar sua orientação de caminho/pontos/viagem com conclusão honesta.
- [ ] Criar os projetos opcionais de expedição e estradas sem exigir ferrovia ou fotografia como desbloqueio.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar alternativas de uma família de bioma e disponibilidade em mundo antigo quando aplicável.
- [ ] Validar o comportamento de loot por jogador/equipe nas configurações do pack.
- [ ] Fazer uma conexão/viagem real de Via Romana ou registrar explicitamente o projeto manual.

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

### MF01 — Atlas de Descobertas

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | O mundo não termina na cerca — nota de exploração segura e retorno; D/P | Livre |
| A2 | Tesouros para cada viajante — explicar Lootr e comportamento de equipe; D/P, sem pedir baú fabricável inexistente | Conferir configurações do servidor |
| M1 | Uma nova paisagem — visitar um bioma de Regions Unexplored; L | Encontro, não coleção total |
| C1–C6 | Expedições por seis famílias visuais: floresta, terreno aberto, região fria, ambiente úmido, costa/água, paisagem incomum | Cada qual aceita alternativas reais do catálogo local de biomas |
| C7 | Álbum de viagem — registrar três lugares favoritos; P com Camerapture como sugestão, não requisito | Sem avaliar beleza automaticamente |
| C8 | Um abrigo longe de casa — projeto de base de excursão; P | Não vincular a chefe ou dimensão |

Não exigir visitar todos os biomas: disponibilidade depende da geração, chunks antigos e compatibilidade do mundo.

### MF03 — Caminhos que Conectam

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | A estrada é a infraestrutura — explicar regra real de Via Romana e material de referência; D/P | Não reduzir o mod a “teleporte livre” |
| A2 | Marcar origem e destino — estabelecer pontos válidos pelo mecanismo instalado; E/P | Validar distância, caminho e configuração |
| A3 | Testar o percurso — realizar uma viagem válida; E ou P | Não usar item/placa isolada como prova |
| M1 | Casa e vizinhança — conexão funcional entre dois lugares úteis; P/E | Independente de trens |
| C1 | Estrada de verdade — projeto de caminho legível com iluminação e descanso; P | Opcional |
| C2 | Rede da vila — mais de uma conexão útil; P | Sem exigir distância/contador não implementado |
