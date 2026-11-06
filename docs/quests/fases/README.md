# Execução incremental das quests de Lilyvale

**Estado inicial: todas as fases abaixo estão não iniciadas.** A existência de quests legadas e de pesquisa documental não é conclusão de uma fase desta reformulação.

[Plano editorial e regras comuns](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Como usar

1. Solicitar uma fase ou lote explicitamente: por exemplo, “execute F02” ou “execute somente F05.2”. Este desmembramento não inicia nenhuma implementação.
2. Ler este índice, as regras comuns do plano principal, a skill técnica local e o arquivo da fase. Conferir o estado real do repositório, versões e trabalho preexistente.
3. Confirmar os pré-requisitos daquele lote; executar apenas o escopo correspondente e preservar os demais capítulos/IDs.
4. Cada entrega de conteúdo inclui um corte vertical: objetivo, critério honesto, texto, dependências, recompensa, layout e validação. Não publicar só uma árvore de ícones como fase concluída.
5. Manter o livro utilizável após cada lote: nenhuma referência para ID ausente, nenhum capítulo legado apagado antes da migração completa e nenhum duplicado temporário de recompensa.
6. Aplicar validações e registrar evidências/aceite. Se faltar acesso ao jogo, marcar “aguardando validação em jogo”, não concluída.
7. Atualizar a tabela e a ficha da fase; parar no limite autorizado. Commit/push só quando solicitado.

## Ordem sugerida e pré-requisitos reais

- F00 resolve contratos e aprovação; F01.1 entrega a base estrutural segura. Esses são os pré-requisitos comuns, não uma obrigação de resolver todo mod antecipadamente.
- A partir de F01.1, a numeração prioriza vida cotidiana, mas as frentes podem ser reordenadas conforme interesse. F01 pode estar parcial por FL01 sem impedir uma fase que depende apenas de F01.1.
- F02 migra PD02/PD03 em conjunto. F12/F13 compartilham o inventário dos IDs de Create e exigem coordenação; manter as quests antigas válidas até cada parte migrar.
- F05.1/2/3, F07.1/2, F14.1/2 e F17.1/2/3 são lotes explícitos. Um lote concluído não conclui automaticamente a fase que contém outros lotes.
- F11 e F16 têm gates próprios de survival/integração. Em espera nesses gates não significa pausar fazenda, decoração, música ou engenharia.
- F18 integra o escopo entregue. Pendências adiadas podem acompanhar uma release parcial, mas não justificam declarar os 30 capítulos completos.
- Estas são dependências de execução e migração. Não criar correspondências automáticas com dependências de quests no jogo.

## Fases

| Fase | Entrega | Capítulos responsáveis | Estado |
| --- | --- | --- | --- |
| [F00](./00-contratos-e-preparacao.md) | Contratos e preparação | Preparação | Não iniciada |
| [F01](./01-fundacao-e-legado.md) | Fundação e legado | PD01, FL01 | Não iniciada |
| [F02](./02-inventario-e-melhorias.md) | Inventário e melhorias | PD02, PD03 | Não iniciada |
| [F03](./03-tips-and-tricks.md) | Tips & Tricks | PD04 | Não iniciada |
| [F04](./04-fazenda-e-cozinha.md) | Fazenda e cozinha | VC01, VC02 | Não iniciada |
| [F05](./05-sabores-artesanais.md) | Sabores artesanais | VC03, VC04, VC05 | Não iniciada |
| [F06](./06-construir-e-habitar.md) | Construir e habitar | LR01, LR02 | Não iniciada |
| [F07](./07-pesca-e-musica.md) | Pesca e música | VC06, CC03 | Não iniciada |
| [F08](./08-companheiros-e-estabulo.md) | Companheiros e estábulo | CC01, CC02 | Não iniciada |
| [F09](./09-paisagens-e-caminhos.md) | Paisagens e caminhos | MF01, MF03 | Não iniciada |
| [F10](./10-arqueologia.md) | Arqueologia | MF02 | Não iniciada |
| [F11](./11-pelucias.md) | Pelúcias | LR03 | Não iniciada |
| [F12](./12-oficina-e-logistica.md) | Oficina e logística | EF01, EF02 | Não iniciada |
| [F13](./13-ferrovias.md) | Ferrovias | EF03 | Não iniciada |
| [F14](./14-outras-dimensoes.md) | Outras dimensões | AH01, AH02 | Não iniciada |
| [F15](./15-exploracao-espacial.md) | Exploração espacial | AH03 | Não iniciada |
| [F16](./16-netherita-avancada.md) | Netherita avançada | FL02 | Não iniciada |
| [F17](./17-jornada-ate-o-end.md) | Jornada até o End | JE01, JE02, JE03 | Não iniciada |
| [F18](./18-catalogos-e-aceite-integrado.md) | Catálogos e aceite integrado | Aceite integrado | Não iniciada |

## Protocolo comum de validação

- **Estado inicial:** snapshot e inventário dos arquivos/IDs envolvidos. Não confundir a contagem histórica de 290 quests com uma auditoria atual; conferir novamente.
- **Migração:** cada ID mantém dono/destino único. Referências e recompensas já reconhecidas devem sobreviver ao movimento; testar cópia de equipe com progresso.
- **Estrutura:** parser nativo, formato/faixa de IDs, unicidade, referências válidas e ausência de ciclos. Nenhum link aponta para um capítulo/quest que ainda não existe.
- **Conteúdo:** receita/fonte realmente carregada, task coerente com o verbo, aliases corretos, itens não consumidos quando previsto, P explícito quando manual.
- **Editorial:** A/M/C identificados, coleções independentes, consulta antes do completismo e nenhum gate de chefe sobre estilos pacíficos.
- **Visual:** coordenadas finais, tamanho dos ícones, linhas/colisões, primeira tela e leitura no jogo. Preservar a exceção do layout legado compacto de armazenamento.
- **Funcional:** testar objetivos publicados no jogo e as condições relevantes de cooperação/progresso; um arquivo parseável não comprova ação ou obtenção.
- **Recompensas:** não entregar o objetivo seguinte, duplicar claim ou alterar valores históricos sem aceite; projetos manuais não são fazendas de itens valiosos.
- **Fechamento:** listar o que mudou, o que foi testado e o que falta; obter aceite antes de marcar entrega final. Não fazer commit/push por inferência.

## Vocabulário de estado

- **Não iniciada:** nenhum lote desta fase foi executado nesta reformulação.
- **Em execução:** lote autorizado está sendo trabalhado.
- **Parcial:** há lotes entregues e outros ainda pendentes; listar quais.
- **Em espera:** um gate local impede prosseguir; registrar causa e próximo desbloqueio técnico/editorial.
- **Aguardando validação em jogo:** conteúdo e verificações estáticas feitos, sem evidência funcional/visual suficiente.
- **Concluída:** todos os lotes previstos aprovados, verificações relevantes registradas e aceite obtido; não confundir com histórico de quests já existentes.

## Artefatos de passagem por lote

Registrar na ficha do arquivo da fase: escopo/arquivos, mapa de IDs quando aplicável, decisões de detector/alias, catálogo aprovado/rejeitado/pendente, evidência estática e de jogo, problemas abertos e próximo lote seguro. Para coleções grandes, usar lotes com lista fechada de identidades antes de editar, sem fixar quantidade artificial ou prometer o total a partir dos candidatos.

Alterações futuras dos objetivos de capítulo devem ser feitas no arquivo da fase que os possui; atualizar arquitetura/cobertura no plano principal se a mudança afetar a organização. Não manter uma segunda cópia concorrente da especificação original.
