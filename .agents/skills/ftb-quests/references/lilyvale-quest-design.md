# Lilyvale: jornadas independentes e atividades opcionais

## Diretriz editorial

Organize o livro por experiências do jogador, não por uma sequência obrigatória de mods. Quem só quer cuidar da fazenda deve ter aprendizado, conquistas e desafios próprios sem precisar derrotar chefes, explorar dimensões ou terminar tecnologia. A ordem das categorias é navegação, não uma cadeia de desbloqueios.

## Categorias e fronteiras

O plano versionado e os contratos da F00 prevalecem sobre a organização histórica. Preserve os IDs existentes e esta ordem em `chapter_groups.snbt`; a F01 acrescenta a nona categoria sem antecipar seus capítulos:

| Categoria | ID | Conteúdo e fronteira |
| --- | --- | --- |
| Primeiros Dias | `048ED71F33A9801E` | Orientação inicial curta, sobrevivência básica e descoberta das trilhas; não exigir concluir tudo para abrir o livro. |
| Vida no campo | `2F3E0F43CC0404AB` | Cultivo, criação rural, cozinha e produção artesanal; deve sustentar uma jornada completa sem combate obrigatório. |
| engenhos e ferrovias | `6F00000000000001` | Create, automação, logística, trens e redes ferroviárias. |
| O mundo lá fora | `2E622CDAB0B6B1F2` | Expedições, biomas, estruturas e descobertas no mundo principal; utilidades portáteis podem ser apresentadas aqui. |
| Além do horizonte | `6E00000000000001` | Outras dimensões, exploração espacial, oxigênio e expedições além do mundo principal, quando houver conteúdo confirmado no pack. |
| Forja e legado | `6E00000000000002` | Overgeared, metalurgia, equipamentos e feitos de combate. Marcos de expedição permanecem na categoria da expedição para evitar duplicação. |
| Companheiros e coleções | `4DFBF6E45E6929B8` | Pets, instrumentos, pelúcias, artefatos e outras coleções; animais de produção pertencem principalmente a Vida no campo. |
| Criando seu Lar | `1DA3993DEE28D0C0` | Construção, decoração, conforto e organização da casa/depósito. |
| A Jornada até o End | `6E00000000000003` | Olhos do Mundo, O Último Voo e Ilhas do Vazio nas fases responsáveis; não é chave de desbloqueio para fazenda/casa. |

Economia é transversal: trate vendas e produção na trilha correspondente, sem recriar uma categoria separada. Um mod pode aparecer em mais de um tema quando as atividades forem distintas; evite duplicar a mesma task de obtenção.

## Três tipos de atividade

Os tipos abaixo são conceitos editoriais, não novos valores de `type` no SNBT. Tasks continuam usando os tipos reais suportados pela versão instalada. Não acrescente campos de classificação presumidos sem verificar o suporte.

### Aprendizado

- Ensine uma primeira interação útil, com texto curto e uma tarefa representativa: primeira mochila, refeição, engrenagem, trem ou preparação de oxigênio.
- Deixe detalhes e variações no EMI, Ponder ou descrição de consulta. Não transforme cada receita, bloco, tier e upgrade em etapa obrigatória.
- Se a task só detecta posse de item, não diga que ela comprova cozinhar, automatizar ou montar uma estrutura funcional.

### Marco de progressão

- Reconheça um resultado significativo dentro da trilha: produção automatizada, uma viagem, a Lua, uma masmorra do Aether ou o Ender Dragon.
- Os exemplos são propostas de conteúdo, não quests já implementadas ou prova de compatibilidade. Confirme mods, receitas e gatilhos antes de criar.
- Não aceite um bloco de máquina no inventário como prova de fábrica funcional. Verifique ações por mecanismos realmente disponíveis; sem detector real, mantenha orientação em texto, sem task de checkmark de gameplay.
- Dê à fazenda, à casa e às ferrovias marcos próprios; não apresente chefes como única forma de progredir.

### Desafio ou coleção opcional

- Reserve diversidade, completismo e projetos pessoais para objetivos independentes: criação de animais diferentes, receitas, decoração, redes ferroviárias, artefatos e pelúcias.
- Nunca use completar um catálogo ou desafio opcional para desbloquear aprendizado essencial, outra categoria ou uma melhoria de qualidade de vida geral.
- Uma coleção pode ter etapas internas, mas sua conclusão não deve se tornar pré-requisito externo. Identifique a natureza opcional no texto; usar o campo `optional` isoladamente não remove dependências já existentes.

## Dependências e recompensas

- Priorize pré-requisitos reais na mesma trilha. A pedido do usuário, aceite também ordem didática de uso dentro do mesmo sistema, documentando que não representa ingredientes da receita; preserve alternativas e não conecte sistemas/categorias independentes.
- Permita descobertas e consulta antes de completar objetivos sempre que o formato instalado oferecer isso. Não mude globalmente `progression_mode` sem avaliar as consequências para todas as trilhas.
- Recompense o estilo de jogo escolhido. Não esconda mochila básica, armazenamento ou decoração atrás de chefes ou exploração espacial por decisões do livro.
- As receitas do pack podem ter exigências próprias. Não afirme independência mecânica total apenas porque removeu dependências das quests; confira receitas antes de fazer essa promessa.
- Preserve IDs de capítulos, quests, tasks e recompensas em reorganizações. Não apague conteúdo existente ou progresso para reduzir completismo sem um escopo de migração aprovado.

## Aplicação aos capítulos existentes

- Primeiros Passos permanece em Primeiros Dias.
- Create está dividido em Oficina de Engenhos, Logística em Movimento e Estações e Ferrovias, em Engenhos e Ferrovias.
- Overgeared passa para Forja e legado.
- Immersive Melodies virou Música para Lilyvale, em Companheiros e coleções, com as 11 folhas como C.
- Na revisão F02, somente `mochila_e_organizacao.snbt` permanece, com sete aquisições e três ramais compactos: mochila → coleta; baú ou barril → aplicador; conector Tom’s → terminal. Caderno de Melhorias e seus 203 objetivos foram retirados explicitamente pelo usuário, assim como os quatro checks de gameplay. Consulte `docs/quests/fases/registros/f02-simplificacao.md` antes de restaurar qualquer material histórico.
- As nove categorias têm capítulos (30 no total, gerados por `build/quest-book/gen.py`); veja `docs/quests/planejamento.md`, seção 14. O conteúdo gerado passou só na validação estática.
- A reorganização de categorias não classifica automaticamente cada quest nos três tipos. Faça a revisão editorial por capítulo, preservando progresso e validando os gatilhos propostos.
- A F01 classifica PD01 e FL01; Overgeared conserva o arquivo e os IDs, com título Fogo, Martelo e Aço. A revisão F02 mantém somente PD02. Os capítulos gerados já trazem subtítulo, forma e recompensa A/M/C; o Create dividido ainda não teve os títulos revisados. Consulte os registros de cada fase para o estado de validação; não deduza conclusão de gameplay a partir da classificação.

## Checks e capítulos informativos

- Checkmarks são permitidos somente para informação/leitura, como os quatro cartões de Início. Não implemente propostas antigas P/autodeclaradas para gameplay; use detector real ou deixe a sugestão na descrição.
- Ao retirar conteúdo por solicitação do usuário, capture snapshot e registre IDs removidos. Preserve os payloads dos objetivos mantidos, sem prometer retenção do progresso dos descartados após um reload.

## Critérios de revisão

- Todos os capítulos apontam para grupos existentes, na ordem temática solicitada.
- IDs preservados e novos IDs dentro de `0000000000000001` a `7FFFFFFFFFFFFFFF`, sem colisões.
- Nenhuma trilha rural/doméstica depende artificialmente de um chefe ou dimensão.
- Todo marco detecta o resultado que promete, ou declara explicitamente os limites da detecção.
- Desafios/coleções não bloqueiam outras trilhas; o aprendizado não vira checklist completo de receitas.
- Valide SNBT, referências, ciclos e preservação do conteúdo antes do `/ftbquests reload`; confirme aparência e navegação no jogo separadamente.
