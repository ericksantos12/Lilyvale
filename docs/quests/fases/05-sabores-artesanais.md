# F05 — Sabores artesanais

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **VC03, VC04, VC05**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- As convenções de identidade/recompensa da F04 ajudam, mas sua execução integral não é pré-requisito. Reutilizar decisões já aprovadas sem duplicá-las.
- Um detector de vinho ou idade inconsistente bloqueia somente a atividade que o utiliza; não todo o capítulo ou as outras artes culinárias.

## Checklist de execução futura

- [ ] F05.1 — entregar Meadow: aprendizado de laticínios, marco de queijaria e catálogo de queijos realmente obteníveis.
- [ ] F05.2 — entregar Vinery: cultivo/suco/fermentação, ramal de maçãs e rótulos opcionais, sem etapa de destilação presumida.
- [ ] F05.3 — entregar Bakery: massas/estações corretas e produtos finais, conferindo integração com Farm & Charm e a massa do pack.
- [ ] Cada lote pode ser executado e validado separadamente; atualizar o estado de cada um, sem exigir terminar o álbum de outro mod.
- [ ] Aplicar regras de aliases para queijo/bolo/fatia e de identidade para vinho envelhecido.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar um ciclo de cada estação incluída e uma identidade de coleção/alias por família.
- [ ] Conferir que o catálogo de rótulos ignora NBT irrelevante e não usa o avanço de uvas inconsistente como prova.
- [ ] Verificar que a vitrine de Bakery pode ser um projeto sem exigir concluir LR02.

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

### VC03 — Sabores do Prado

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Vida alpina — conhecer a paisagem e seus animais; L/O, não exigência para o resto da fazenda | Livre |
| A2 | O leite certo — obter um leite elegível de Meadow; I | Não afirmar ordenha se apenas comprado/recebido |
| A3 | Começo da queijaria — coalho e prensa de queijo; I/O | Materiais reais do processo |
| A4 | Primeira peça — obter um queijo produzido pela receita instalada; I/E | Sem usar queijo lunar de Ad Astra como requisito |
| M1 | Queijaria da casa — demonstrar um ciclo de leite → queijo; E ou P | Marco local |
| C1 | Chalé do prado — construir espaço rural com despensa/queijaria; P | Não depende de explorar todas as paisagens |
| Q1 | Queijo descoberto: `<tipo>` — uma folha por queijo elegível | Independente; roda e fatia contam como a mesma família após validação |

O processo `meadow:cheese` e receitas de leite/coalho foram encontrados no JAR local. Não transformar variantes cosméticas de chalés e madeira em coleta obrigatória.

### VC04 — Vinhedos e Adegas

A proposta usa **uva → suco → fermentação → vinho**. A documentação do autor descreve pisar uvas no Grapevine Pot e produzir vinho no Fermentation Barrel.[12][13] O plano não inclui uma etapa de “destilar” por analogia com outras bebidas: não foi estabelecido que seja um processo desta versão.

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | A primeira videira — obter uma variedade de uva/semente; I | Livre; não exigir todas as variedades |
| A2 | Colheita na cesta — cultivar e colher sua uva; E a validar ou P explícito | Orientação de cultivo, não barreira de catálogo |
| A3 | Suco sob os pés — conhecer o Grapevine Pot e obter suco compatível; O/I do resultado | Não exigir um número de saltos de outra versão |
| A4 | A adega começa no barril — obter barril de fermentação e garrafa; I/O | Só materiais necessários |
| A5 | A primeira fermentação — obter seu primeiro vinho; I como descoberta, E se quiser autoria | Processo central |
| A6 | O caminho da maçã — prensa e primeiro resultado de maçã; I/O | Ramo paralelo, não obrigação para vinhos de uva |
| M1 | Primeira safra — concluir um ciclo completo de sua escolha; E ou P | Não exigir todos os sucos |
| C1 | Adega com identidade — construir uma adega e expor preferidos; P | Opcional |
| C2 | Uma garrafa para guardar — projeto de envelhecimento; E/NBT só depois de testar armazenamento e idade | Não exigir anos de espera para liberar qualquer trilha |
| Q1 | Rótulo descoberto: `<vinho>` — uma quest por vinho/bebida produzível | Ignorar idade comum, marca de criador e garrafa decorativa na identidade |

Envelhecimento faz parte da proposta do autor, mas números e condições dependem da versão/configuração.[14] O JAR local é 1.4.41: receitas `vinery:wine_fermentation`, `vinery:apple_mashing` e `vinery:apple_fermenting` são a referência de implementação. O avanço local `grape_picker` tem condições que não correspondem fielmente a alguns nomes de critérios; **não reutilizá-lo cegamente como prova de todas as uvas**.

### VC05 — Pães e Confeitaria

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | A massa da casa — identificar a massa e ingredientes efetivos do pack; I | Verificar integração com Farm & Charm/Create |
| A2 | Calor de padaria — primeira cocção por estação instalada; I/O | Processo real, não exigir construir cozinha de três mods |
| A3 | Recheios e coberturas — preparar uma geleia/cobertura; I/E | Ramo próprio |
| A4 | Hora de montar — usar a Caking Station/estação de montagem aplicável; I/O e um produto I | Não ensinar massas e forno duplicados quando uma receita já compartilhada resolver |
| M1 | Uma fornada para a vila — servir uma pequena seleção escolhida; P | Sem exigir todos os bolos |
| C1 | A vitrine da padaria — projeto decorativo integrado a Display Delight; P | Referência cruzada, sem desbloqueio obrigatório de LR02 |
| Q1 | Receita descoberta: `<pão/doce/bolo>` — uma folha por produto final | Não contar bolo inteiro e todas as fatias como receitas novas |

As receitas locais usam `bakery:baking_station`, `bakery:crafting_bowl`, `bakery:pot_cooking` e `bakery:stove`. A seleção das etapas deve seguir essa versão, sem copiar máquinas de versões novas.

## Sources

[12] https://lets-do.ch/wiki/vinery/grapevine-pot
[13] https://lets-do.ch/wiki/vinery/fermentation-barrel
[14] https://lets-do.ch/wiki/vinery/wine
