# F13 — Ferrovias

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **EF03**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita, F01.1 aprovado e inventário de migração de Create compartilhado com F12.
- F12/F13 podem ser invertidas ou paralelas somente com ownership de IDs/arquivos explícito e sem referências ausentes.
- O jogador não precisa concluir EF01/EF02 inteiros para usar este capítulo.

## Checklist de execução futura

- [ ] Completar a migração da parte ferroviária de Create para EF03, reutilizando o mapa iniciado em F12.
- [ ] Entregar montagem, viagem e sinalização de forma curta, integrada a Steam Rails e Navigator.
- [ ] Adicionar especializações opcionais em vez de uma obrigação de todos os trilhos/cosméticos.
- [ ] Remover apenas referências legadas já substituídas e validadas; manter cada ID com destino único.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar trem operacional e viagem real entre estações.
- [ ] Testar o cenário anunciado de sinalização e consulta do Navigator.
- [ ] Conferir todos os IDs históricos de Create entre EF01–EF03 e validar progresso preservado.

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

### EF03 — Estações e Ferrovias

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Um caminho de ferro — trilhos, revestimento e estação; I | Após materiais reais, não conclusão de EF01 |
| A2 | Base sobre rodas — bogey e estrutura de um trem; I/O | Não confundir obter com montar |
| A3 | Todos a bordo — montar um trem operacional; E ou P | Reutilizar ID atual; a task atual de controls precisa ser reconhecida como posse, não montagem |
| A4 | Uma viagem com destino — estação, condução e parada; E/P | Primeiro uso real |
| A5 | Tráfego com cuidado — sinalização e divisão de blocos; I das peças + cenário P | Após o aprendizado de circulação |
| A6 | Consultar a próxima saída — Railways Navigator e leitura de itinerário; I/E | Integrado à mesma ferrovia, sem tutorial duplicado de estação |
| A7 | Personalizar sem complicar — uma função relevante de Steam 'n' Rails disponível na versão; I/O | Não exigir todos os trilhos/bitolas/cosméticos |
| M1 | Duas estações, uma viagem — completar trajeto entre dois pontos; E/P | Não basta duas estações no inventário |
| M2 | Passageiros ou carga — operar um serviço escolhido; P | Alternativas válidas |
| C1 | Linha cênica — percurso por paisagens preferidas; P | Sem metragem arbitrária para fingir detecção |
| C2 | Rede regional — conectar três destinos com operação legível; P | Opcional |
| C3 | A estação da vila — projeto comunitário com plataforma e informação; P | Pode colaborar em equipe |
