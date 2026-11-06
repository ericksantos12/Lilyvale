# F00 — Registro de contratos e auditoria

**Estado: F00 concluída, com aceite final explícito do usuário.** Este registro executa somente contratos e preparação documental. Não inicia F01 nem altera quests, receitas, mods, dados de equipes ou recompensas em jogo.

[Arquivo da F00](../00-contratos-e-preparacao.md) · [Índice](../README.md) · [Plano principal](../../planejamento.md) · [Inventário e fichas estruturadas](f00-inventario.json)

## 1. Escopo conferido

| Verificação | Resultado observado |
| --- | --- |
| Mods desejados em `quest-mods.md` | 49; todos aparecem na matriz de cobertura |
| Categorias temáticas planejadas | 9; `Pescaria` é subseção de Vida no Campo, não uma décima categoria |
| Capítulos-base planejados | 30 códigos únicos, cada um em uma única fase |
| Categorias atualmente no SNBT | 8 |
| Capítulos atualmente no SNBT | 5 |
| Quests existentes | 290 |
| Tasks existentes | 337 de item e 2 de observação |
| Recompensas existentes | 221 de XP e 107 de item |
| Linhas/grupos de objetivos inventariados no planejamento | 235; não equivalem ao total final de novas quests |
| Identidades candidatas abertas para auditoria | 277; não são um catálogo aprovado |
| Versões dos mods do escopo | 49 arquivos do anexo conferidos contra lockfile e SHA-1 local |
| Parser nativo da FTB Library | 7 arquivos de quests/configuração aprovados |
| Integridade estrutural observada | IDs únicos, hexadecimais positivos na faixa permitida; grupos/referências existentes e grafo sem ciclos |

O inventário JSON registra a branch e o HEAD efetivamente observados, a propriedade dos 30 capítulos, versões, fichas de objetivos/identidades e hashes dos arquivos protegidos. Não registra dados pessoais de jogadores nem o conteúdo de configurações com credenciais.

### Categorias do escopo aceito para futura implementação

1. Primeiros Dias.
2. Vida no Campo.
3. Engenhos e Ferrovias.
4. O Mundo Lá Fora.
5. Além do Horizonte.
6. Forja e Legado.
7. Companheiros e Coleções.
8. Criando seu Lar.
9. A Jornada até o End.

Preservar o desenho de 30 capítulos-base e sua divisão atual entre as fases. Anexos de catálogo só podem ser propostos após a auditoria demonstrar necessidade; não são uma autorização para expandir o escopo silenciosamente.

## 2. Divergências registradas, sem corrigir o jogo

| Divergência | Tratamento acordado para a execução futura |
| --- | --- |
| A Jornada até o End está no plano, mas não no registro atual de oito grupos | Preparar o nono grupo na F01.1, preservando IDs existentes. Não gerar o ID final na F00. |
| Armazenamento está atualmente em Criando seu Lar; a lista atual o coloca em Primeiros Dias | A lista atual de intenção e o plano prevalecem editorialmente. Migrar PD02/PD03 juntos na F02; nada movido na F00. |
| Create é hoje um capítulo único, e o plano separa oficina, logística e ferrovias | F12/F13 devem usar um mapa compartilhado de IDs, conservando os objetivos legados válidos até sua migração. |
| As 210 quests de armazenamento não correspondem a uma trilha obrigatória de aprendizado | Separar entrada prática e consulta/completismo, sem duplicar aquisições, progresso ou recompensas. |
| Texto antigo da referência de desenho ainda descreve a organização anterior | Para tema/categoria, usar `quest-mods.md`, este contrato e o plano atual. A skill técnica segue sendo referência de formato, IDs e APIs da versão instalada, não autorização para restaurar categorias antigas. |
| O plano usa a abreviação D em algumas orientações, mas ela não estava definida no contrato | D significa orientação documental; é tratada como referência R ou texto de apoio. Não é quarto tipo de atividade nem um `type` técnico de task. |
| As coleções atuais compartilham a estrutura de progresso do livro; o alvo pedido é pessoal | Não afirmar que `default_reward_team=false` torna progresso individual. Resolver EQ-01/EQ-02 antes de publicar uma coleção como pessoal ou converter dados legados. |

## 3. Decisões editoriais estabelecidas

Estas regras retomam os pedidos anteriores do usuário e as escolhas explícitas realizadas durante a F00:

- **Aprendizado, marco e desafio/coleção** são tipos editoriais; categorias continuam sendo temas. Referência é consulta.
- O livro não deve ser um tutorial obrigatório para cada bloco/receita. Dimensionar orientação pela novidade do processo.
- Fazenda, casa, companhia e música precisam de conquistas próprias sem gates editoriais de chefes, dimensões ou conclusão industrial.
- Coleções e descrições consultáveis não exigem completar antes a trilha de aprendizado. O jogador pode encontrar itens por caminhos legítimos alternativos.
- Posse comprova obtenção; observação comprova encontro; visita não comprova dungeon concluída; item de máquina não comprova fábrica funcional.
- Projeto sem detector validado pode usar autodeclaração transparente. P descreve um contrato manual, não um tipo extra de atividade e não uma promessa de armazenamento individual.
- Não alterar mods, receitas, configurações, mundo ou progresso durante esta F00. Integrações próprias e mudanças de balanceamento mecânico exigem autorização separada.
- Manter IDs e recompensas históricos na migração; não apagar catálogos apenas para reduzir números.

## 4. Coleções: decisão explícita do usuário

**Contrato aprovado: descoberta por posse, aceitando trocas e presentes.**

- Registrar um exemplar por identidade elegível, sem consumo e sem pedir todo o álbum simultaneamente.
- A redação será “descoberto/obtido”, não “eu cozinhei/fabriquei/capturei” quando o detector só inspeciona inventário.
- Não criar rastreador de produção pessoal como requisito desta abordagem. Se uma atividade específica exigir ação real, ela mantém contrato próprio e precisa de detector comprovado ou P explícito.
- Aprovar a equivalência de produto inteiro/fatia, garrafa colocada/item e outras apresentações durante a fase do catálogo.
- Aceitar uma troca/presente não muda o alvo de progresso pessoal: cada pessoa deve registrar a própria descoberta se EQ-01 confirmar uma implementação compatível.

## 5. Equipes: alvo aprovado, viabilidade em aberto

**Alvo escolhido: coleções pessoais e marcos compartilhados, se tecnicamente viável.**

### O que está decidido

- Não usar conclusão de coleção de um membro como descoberta pessoal automática dos demais.
- Marcos de colaboração devem reconhecer a equipe quando sua detecção e a política do livro permitirem.
- Não alterar silenciosamente a política de recompensas existente para tentar obter progresso individual.
- Aprendizado e recompensas legadas permanecem no comportamento atual até uma decisão de implementação comprovar que uma alteração é necessária e segura.

### O que não está comprovado

A inspeção encontrou `default_reward_team: false` no arquivo atual. A tradução do JAR instalado descreve esse campo como política de recompensa da equipe; não como opção de progresso individual. Também foram encontrados `TeamData` e dados por jogador no JAR, mas esses nomes não demonstram suporte a coleções pessoais por quest.

Portanto a F00 **não promete** que basta ligar/desligar uma configuração. Não basta demonstrar funcionamento com duas equipes diferentes: a validação deverá incluir duas pessoas dentro da mesma equipe.

- **EQ-01:** investigar a versão instalada e testar se é possível registrar a coleção de cada jogador sem fragmentar a equipe nem perder marcos compartilhados.
- **EQ-02:** definir a migração do progresso coletivo antigo. Não deduzir autoria/descoberta individual de um estado histórico da equipe e não limpar progresso para forçar a nova política.
- Se a solução exigir addon, novo mod, script/integracão própria ou mudar o desenho, apresentar a alternativa e obter autorização antes de implementar.
- Se a viabilidade não for confirmada, voltar ao usuário com as opções; **não aplicar fallback coletivo automaticamente** depois de anunciar coleções pessoais.
- EQ-01 limita a publicação de coleções como pessoais, não a criação de textos, marcos compartilhados ou outras atividades independentes. F01.1 pode levantar a estrutura sem resolver tudo de uma vez.

## 6. Recompensas: decisão explícita do usuário

| Conteúdo novo | Recompensa aprovada |
| --- | --- |
| A — aprendizado | 50 pontos de XP |
| M — marco | 150 pontos de XP |
| C — desafio/coleção, incluindo folhas Q | 25 pontos de XP |
| R/D — nota ou referência sem objetivo próprio | Não criar uma recompensa adicional só pela nota |
| P — projeto autodeclarado | Não repetível, sem item valioso; se for quest nova, o XP segue seu tipo editorial A/M/C |

São **pontos de XP**, não níveis. Conteúdo novo terá somente XP, sem brindes de itens adicionados por padrão. Os mesmos valores editoriais valem para uma conquista rural, doméstica ou de combate: a dificuldade de construir um detector não reduz a importância do estilo de jogo.

**Legado preservado:** não substituir as recompensas de item existentes nem reduzir os 50 XP por folha que já existem em coleções antigas só porque o padrão novo de C é 25. Mover a quest preserva ID, progresso e recompensa. Qualquer exceção necessita de decisão explícita e não foi autorizada nesta fase.

## 7. Registro dos gates locais

Todas as linhas abaixo estão **abertas**, sem afirmação de validação funcional. O JSON complementa estas fichas por linha de objetivo e por identidade candidata; cada fase deve atualizar suas evidências antes de publicar o lote.

| Ficha | Escopo/fase responsável | Condição para liberar a implementação afetada |
| --- | --- | --- |
| EQ-01 | F01.1 e a primeira fase que publique coleções | Coleção pessoal com duas pessoas da mesma equipe, sem converter recompensa em progresso por engano; apresentar alternativa se não for suportado. |
| EQ-02 | Migrações de PD03, CC03 e demais coleções legadas | Progresso/recompensas antigos preservados, com regra explícita para dados coletivos; sem autoria individual inventada. |
| INV-01 | F02 / PD02–PD03 | Migração conjunta, filtro/upgrade corretos e nenhuma duplicação de IDs ou claims. |
| INV-02 | F02 / PD02-A6/M1/M2 | Rede/organização funcional detectada de verdade ou P transparente; peças isoladas não bastam. |
| UTIL-01 | F03 / PD04 | Controles, fotos, descanso e blacklist reais; orientação sem fabricar um item de Carry On. |
| COZ-01 | F04 / VC01–VC02 | Receitas carregadas, produto final elegível, compat ausente excluída e massas do pack conferidas. |
| COZ-02 | F04/F05 | Equivalência inteiro/fatia/recipiente e registro por identidade; eventual NBT distingue produto, não cosmético. |
| ART-01 | F05.1 / VC03 | Processo de queijo e fonte do leite/coalho válidos; queijo lunar não é requisito. |
| ART-02 | F05.2 / VC04 | Processo real de suco/fermentação; não usar o avanço inconsistente de uvas nem presumir destilação. |
| ART-03 | F05.2 / VC04-C2 | Idade/armazenamento comprovados; envelhecimento não é gate das atividades básicas. |
| ART-04 | F05.3 / VC05 | Estações e massas da versão instalada; vitrine opcional não bloqueia a padaria. |
| CASA-01 | F06 / LR01–LR02 | Funções citadas de ferramentas/decoração comprovadas; Display Delight aceita os pratos usados. |
| LAZER-01 | F07 / VC06 | Captura e diário nativo do Tide com critérios testados; não duplicar peixe nem aceitar só posse como captura. |
| LAZER-02 | F07 / CC03 | Preservar 11 identidades/recompensas atuais e verificar efeitos da política pessoal sobre dados de equipe. |
| PET-01 | F08 / CC01–CC02 | Encontro, doma, reprodução e cuidado diferenciados; espécie/variante e fonte reais. |
| MUNDO-01 | F09 / MF01 | Biomas existentes e alternativas para geração/chunks antigos, sem exigir todos. |
| MUNDO-02 | F09 / MF03 | Rede de Via Romana/viagem efetiva ou P explícito, sem inventar contador de distância. |
| ARQ-01 | F10 / MF02 | Identificação/fóssil completo e NBT de artefatos válidos; sem inflar cabeça/corpo em duas identidades. |
| PLUSH-01 | F11 / LR03 | Fonte inicial de survival por pelúcia; loot de quebrar bloco não basta. Sem bloquear fazenda/casa se falhar. |
| ENG-01 | F12/F13 | Mapa compartilhado dos IDs de Create e referências legadas mantidas até cada parte migrar. |
| ENG-02 | F12 / EF01–EF02 | Fábrica/logística/contraption funcionais por critério real ou P, nunca apenas peças no inventário. |
| TREM-01 | F13 / EF03 | Montagem, viagem, sinalização e Navigator conforme o comportamento real; crédito em equipe. |
| DIM-01 | F14 / AH01 | Conclusão de dungeon comprovada por evento/derrota, não chave/visita. |
| DIM-02 | F14 / AH02 | Acesso/retorno e locais do Otherside, sem chefe presumido. |
| ESP-01 | F15 / AH03 | Oxigênio e combustível carregados, traje, lançamento, chegada e retorno; P explícito se necessário. |
| ESP-02 | F15 / AH03-M3/Q1 | Base funcional e cada destino publicado testados, sem assumir validação de planetas pendentes. |
| LIGA-01 | F16 / FL02 | Integração Overgeared × Advanced Netherite e preservação de dados do equipamento. Gate local, sem mudar receita silenciosamente. |
| END-01 | F17 / JE01 | Olhos distintos e histórico após consumo; não exigir 16 quando a regra usa seleção menor. |
| END-02 | F17 / JE02–JE03 | Confronto True Ending, terreno/locais Endercon e crédito solo/equipe testados. |
| VIS-01 | Cada fase e F18 | Layout real com suas folhas, colisões/linhas, leitura, consulta e orçamento de recompensas. |

Os 277 candidatos não foram promovidos a aprovados nesta F00. Uma identidade sem fonte/detector válido fica pendente ou rejeitada na fase responsável; não deve virar um objetivo impossível para completar números.

## 8. Evidências e limites dos testes

### Executado

- Comparação programática entre lista, matriz, arquitetura e propriedade dos capítulos nas fases.
- Conferência de versões e SHA-1 dos 49 JARs de escopo contra o lockfile.
- Parse estrutural do livro existente, verificação de grupos, IDs e dependências/ciclos.
- Parser **nativo da FTB Library instalada** sobre grupos, dados globais e os cinco capítulos existentes.
- Abertura de fichas para as 235 linhas/grupos planejados e 277 identidades candidatas.
- Registro de hashes dos arquivos protegidos para conferir que a fase documental não os alterou.

### Não executado e não exigido como prova desta fase documental

- Migração ou alteração de quests; preparação da cópia de mundo/equipe e execução da F01.1.
- Teste visual/funcional em jogo dos novos capítulos, dos detectores ou das fontes dos candidatos.
- Teste de coleções pessoais dentro da mesma equipe e migração de suas descobertas antigas.
- Integração de receitas, scripts novos, alteração de mods ou rebalanceamento de recompensas existentes.

A aprovação da F00 fecha **escopo e contratos**, não aprova automaticamente a viabilidade dos sistemas. Seus gates continuam no registro até serem testados pela fase responsável.

## 9. Passagem para a próxima fase

- **Próximo lote possível após aceite da F00:** solicitar F01.1 — snapshot, estrutura e inventário de migração; nenhuma F01 foi iniciada nesta entrega.
- **Decisão central a investigar cedo:** EQ-01/EQ-02, antes de publicar coleção como pessoal ou converter seu legado. A documentação de receitas/fontes e outras trilhas independentes pode avançar sem uma implementação fictícia desse recurso.
- **Não autorizado por esta execução:** commitar/push, alterar configuração de equipes/recompensas, mudar receitas/mods ou executar outra fase automaticamente.
- **Aceite final:** o usuário escolheu explicitamente “Aprovar e encerrar F00, sem iniciar F01”, confirmando 49 mods, nove categorias, 30 capítulos-base e as políticas desta fase. Nenhuma fase adicional está autorizada por esse aceite.
