# F01 — Fundação e legado: registro de execução

**Ajuste posterior solicitado pelo usuário:** a orientação inicial foi movida para o capítulo auxiliar **Início**, com quatro checks de leitura sem recompensas, e os hyperlinks foram removidos. Os totais e testes abaixo descrevem a primeira entrega; consulte o [registro do ajuste e validador atual](f01-ajuste-inicio.md) para o estado atualizado.

**Data:** 2026-11-06. **Estado atual:** concluída com validação e aceite informados pelo usuário: “validação realizada, siga para a proxima fase”. **F01.1 aprovado para avançar à F02.** O agente executou as verificações estáticas; não observou o teste no jogo nem recebeu evidências por cenário. As pendências/checklists abaixo são o registro histórico anterior ao aceite, não novas exigências para reiniciar a F01. EQ-01/EQ-02 não foram comprovados por esse relato geral.

Autorização: solicitação explícita do usuário para prosseguir à fase 1, após o encerramento aprovado da F00. Nenhuma fase posterior, commit ou push foi executado.

[Especificação da F01](../01-fundacao-e-legado.md) · [Índice](../README.md) · [Mapa de IDs e evidências estruturadas](f01-mapa-de-ids.json)

## 1. Checkpoint F01.1

- Branch `dev`; o estado real inicial do Git estava limpo, sem alterações preexistentes a sobrescrever. HEAD registrado no JSON.
- Snapshot dos sete SNBT em `build/f01-foundation/20261106-191148/quests/`.
- Snapshot integral dos mundos `Flat` e `New World`, incluindo dados de FTB Quests e FTB Teams, em `build/f01-foundation/20261106-191148/worlds/`. O Minecraft estava fechado durante as cópias.
- Cópias jogáveis preparadas, sem sobrescrever mundos existentes:
  - `saves/Lilyvale-F01-Migracao/`: cópia de `New World`.
  - `saves/Lilyvale-F01-Legado/`: cópia de `Flat`, com cobre/polimento concluídos e recompensas já resgatadas.
- Todas as cópias foram conferidas por SHA-256, arquivo a arquivo. Os dois mundos originais permanecem byte a byte iguais ao snapshot; seus dados de progresso não foram editados.
- Os nomes exibidos pelo jogo continuam os nomes internos originais; conferir o diretório da cópia na seleção de mundos para não abrir o original.

### Inventário real, não contagem presumida

| Objeto | Antes | Depois |
| --- | ---: | ---: |
| Grupos | 8 | 9 |
| Capítulos | 5 | 5 |
| Quests | 290 | 290 |
| Tasks | 339 | 339 |
| Recompensas | 328 | 328 |
| IDs explícitos de conteúdo/grupos | 970 | 971 |

Todos os 970 IDs anteriores foram preservados. O único ID novo é o grupo `6E00000000000003`, **A Jornada até o End**. Nenhuma quest, task ou recompensa foi criada, removida, duplicada ou movida entre arquivos nesta fase. O ID interno `0000000000000001` pertence ao livro, confirmado no construtor `BaseQuestFile` do JAR instalado; não integra o total de IDs explícitos e permanece reservado.

O JSON registra capítulos, quests e IDs de tasks/recompensas, hashes dos payloads, origem/destino atual, dependências antes/depois e arquivos protegidos. Os objetos filhos de uma quest mantêm seu dono e acompanham o destino dela. A divisão de armazenamento entre PD02/PD03 e de Create entre EF01/EF02/EF03 está **pendente da fase responsável**: os candidatos estão registrados, mas nenhum destino específico foi inventado nem aplicado antecipadamente.

### Estrutura e identidade visual

- Os oito grupos anteriores mantiveram IDs, títulos e ordem; a nona categoria foi acrescentada ao final. Grupos vazios podem ficar ocultos na interface até receberem capítulos.
- Classificação aplicada apenas às 34 quests de PD01/FL01: **23 A, cinco M e seis C**.
- A: círculo e subtítulo azul; M: hexágono e subtítulo dourado; C: quadrado lilás com o texto **Opcional**. A classificação também usa letras e formas, não apenas cor.
- Alguns aprendizados em ramais continuam com `optional: true`: aprender projetos ou fundição não vira pré-requisito da trilha principal.
- Descrições e detalhes das 34 quests ficam explicitamente consultáveis antes de desbloquear/concluir suas tarefas.
- Coordenadas preservadas em todos os capítulos, inclusive o layout compacto de armazenamento. Ajustes de forma/tamanho não alteram tasks ou recompensas.
- `data.snbt`, mods, manifests, receitas e scripts KubeJS não foram alterados. Não foi implementada separação de progresso pessoal/equipe nem aplicado fallback coletivo.

## 2. F01.2 — Primeiros Passos / PD01

Arquivo: `config/ftbquests/quests/chapters/primeiros_passos.snbt`.

- Reutilizadas as nove quests existentes: oito aprendizados e o marco local da picareta de cobre.
- Preservados integralmente os payloads de tasks/recompensas, os IDs, as dependências e as coordenadas.
- Mantida a etapa `79E58B9DB040B4BA` de aquecimento/polimento antes da picareta `3D531CC1B4F13F97`, incluindo a task de grindstone `7520FD53E96DB21B`.
- A orientação **Escolha seu caminho** foi incorporada à descrição inicial, sem nova task ou recompensa. Explica as trilhas e a natureza incremental do livro.
- Três atalhos apontam somente para quests já existentes: armazenamento `6A11000000000007`, Create `6C11000000000001` e instrumentos `6D11000000000001`. Fazenda/exploração recebem orientação textual; não há links para capítulos futuros inexistentes.
- Os textos esclarecem que posse aceita trocas/presentes e não prova autoria. O cobre é final local, não chave universal das demais categorias.

## 3. F01.3 — Fogo, Martelo e Aço / FL01

Arquivo preservado: `config/ftbquests/quests/chapters/overgeared.snbt`; capítulo `6F10000000000001`.

- Título alterado de Overgeared para **Fogo, Martelo e Aço**, sem trocar arquivo ou IDs.
- Mantidas as 25 quests e 42 tasks: 15 aprendizados, quatro marcos e seis desafios/especializações C.
- Preservados os processos existentes de ferro, aço, projetos, moldes, diamante e netherita; nenhuma integração com Advanced Netherite foi iniciada.
- Perfect continua opcional e não desbloqueia nenhum material comum. O texto explicita a conferência do estado/NBT da peça, não de quem a forjou.
- Nenhuma task exige as bigornas Tier A/B desativadas. Estações e peças continuam com tasks nativas de posse/observação.
- Todas as recompensas históricas, inclusive itens, permanecem iguais; a política de XP novo não foi usada para rebalancear o legado.

### Dependências corrigidas após conferir as receitas instaladas

| Quest | Mudança | Evidência/motivo |
| --- | --- | --- |
| `6F11000000000007` — Projetos sobre a mesa | Retirado o requisito do lote de ferro | `drafting_table.json` usa bancada + projeto vazio; o ferro não é necessário para obter essa estação |
| `6F11000000000012` — Um molde encontrado pelo caminho | Retirado o requisito de possuir picareta de aço | A task pede estação/molde encontrado, não a execução da melhoria; a duplicação posterior do molde usa aço, mas não a picareta |
| `6F11000000000013` — Diamante sobre aço | Exige diretamente picareta de aço e estação/molde | O aço é a base da melhoria; transferida a relação para o resultado correto, preservando os ancestrais técnicos do marco |
| `6F11000000000019` — Uma ponta que vale um diamante | Retirado o requisito de colecionar flechas de ferro/aço | `diamond_shard_from_grinding.json`, `diamond_arrow.json` e `diamond_arrow_2.json` permitem a rota de diamante com graveto/pena, inclusive na bancada |

As linhas de entrada do marco de diamante foram ocultadas para não atravessarem o ícone intermediário no layout legado; as dependências continuam presentes. Nenhuma dependência nova foi criada para outra categoria.

## 4. Verificações executadas

- Parser **nativo da FTB Library** nos sete SNBT, antes e depois das alterações: passou.
- Roundtrip nativo dos sete arquivos, usando `CheckOvergeared.java`: passou, sem diferença nos dados relidos.
- Formato hexadecimal, faixa positiva assinada, unicidade, referências e ausência de ciclos: passaram; nenhum ID reutiliza o ID interno do livro.
- Comparação com o snapshot: todos os payloads de tasks/recompensas e todas as coordenadas preservados; somente quatro listas de dependências foram revisadas, conforme a tabela.
- Comparação SHA-256 dos arquivos protegidos: somente os três SNBT autorizados foram alterados; armazenamento, Create, instrumentos, configuração global, manifests, catálogo e scripts ficaram iguais.
- Casos nativos de comparação NBT: polimento, Perfect, tipo de molde/projeto, dados adicionais e rejeições passaram no comparador instalado. Isso não substitui o teste da task dentro do jogo.
- Referências dos três atalhos e JSON dos componentes: válidos. `TextUtils.parseRawText` aceita JSON bruto; o registro de `open_book` não exige permissão editorial. Clique/renderização continuam pendentes no jogo.
- Modelo geométrico circular `size/2` das 34 quests: zero sobreposições e zero segmentos visíveis atravessando os círculos de outros ícones. O modelo não reproduz os contornos reais do renderer; a validação visual permanece obrigatória.
- Dados reais salvos: `Flat` tem 37 entradas em `completed` e 16 em `claimed_rewards` — entradas de objetos, **não 37 quests**. Seus 55 IDs explícitos referenciados continuam existentes. `New World` referencia cinco. O ID adicional do livro foi identificado separadamente; nenhum ID salvo ficou sem correspondência.
- `git diff --check`: passou. Revisão local de configurações/documentação; sem aprovação de revisão independente alegada. ESLint não se aplica: nenhum JavaScript foi alterado.

Ferramentas locais, ignoradas pelo Git: `build/f01-foundation/verify_phase.py`, `before.json`, `after.json` e `checkpoint.json`. Validação repetível: `python build/f01-foundation/verify_phase.py --after`. Os preparadores de snapshot/publicação são de execução única e não devem ser repetidos para substituir o checkpoint.

## 5. Gates ainda abertos — não encerrar a fase

O jogo não foi iniciado nesta execução. O `PreLaunchCommand` original da instância executa `java -jar pakku.jar fetch` antes do lançamento; dispará-lo automaticamente poderia alterar/downloadar mods fora do escopo. O hook e a configuração da instância original foram preservados. Para automatizar o teste, preparar uma instância isolada sem esse pré-lançamento, ou obter autorização específica para executá-lo.

- [ ] Abrir a cópia **Lilyvale-F01-Legado**, conferir que cobre/polimento continuam concluídos e recompensas resgatadas não reaparecem.
- [ ] Conferir ferro/aço em uma cópia de teste, aquisição/observação, NBT de polimento e a ramificação Perfect opcional.
- [ ] Validar novo mundo, leitura dos detalhes bloqueados, formas, subtítulos, tamanhos e os três atalhos de navegação.
- [ ] Conferir o comportamento de equipe sem confundir recompensa individual com progresso individual; EQ-01/EQ-02 continuam pendentes.
- [ ] Aprovar a migração de F01.1 e obter aceite de PD01/FL01 antes de encerrar F01.

**Próximo passo seguro:** validar a F01 nas cópias e fechar seu checkpoint estrutural. F02–F18 não foram iniciadas. Nenhum commit/push foi feito.
