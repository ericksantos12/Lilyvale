---
name: pakku
description: "Use when managing mods with Pakku. Preserve pack state."
version: 0.1.0
author: Erick Santos (ericksantos12), Hermes Agent
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minecraft, modpack, pakku, dependencies]
---

# Pakku — gerenciamento do modpack

Gerencie projetos, dependências, arquivos locais e exportações com o Pakku. A fonte primária deste procedimento é a documentação versionada em `.pakku/docs/`; consulte o `--help` do executável selecionado para resolver lacunas ou diferenças de versão. Não substitua o gerenciador por downloads manuais ou edição especulativa do lockfile.

## Quando usar

- Adicionar, remover, atualizar, listar ou configurar mods e suas dependências.
- Buscar os arquivos resolvidos, incorporar mudanças locais ou diagnosticar divergências entre a instância e o lockfile.
- Configurar o pack, importar/exportar distribuições ou trabalhar com remotes do Pakku.
- Não usar como substituto das skills de KubeJS ou FTB Quests para receitas, scripts ou quests; use-as em conjunto se a mudança envolver esses conteúdos.

## Pré-requisitos e descoberta

1. Leia `AGENTS.md`, confirme a raiz que contém `pakku.json` e `pakku-lock.json` e execute `terminal(command="git status --short && git branch --show-current")`. Registre as alterações preexistentes; não restaure nem sobrescreva esses arquivos para obter um estado limpo.
2. Leia `pakku.json` com `read_file`. Consulte somente as partes relevantes de `pakku-lock.json` com `search_files` e `read_file`, verificando Minecraft, loader, plataforma, projetos e arquivos envolvidos. Não presuma que `pakku.json` seja um catálogo completo: o lockfile contém as resoluções.
3. Descubra o executável antes de qualquer mutação:
   - `terminal(command="pakku --version && pakku --help")`, se estiver disponível no PATH.
   - Havendo `pakku.jar` na raiz, `terminal(command="java -jar pakku.jar --version && java -jar pakku.jar --help")`.
   - Se um falhar, tente o outro separadamente; não instale/atualize o gerenciador sem necessidade e autorização.
4. Escolha um executável e mantenha-o durante toda a operação. Neste repositório foram observados PATH **1.4.0** e JAR **1.2.1**; reconfirme em cada sessão. Prefira o JAR versionado quando compatível com a tarefa e com as docs locais; não misture versões silenciosamente.
5. Leia a página local correspondente ao comando e execute seu `--help` usando o executável escolhido. Enumerações, flags e seletores devem estar confirmados antes do uso. O diretório de trabalho deve ser a raiz do pack; fora dela, confirme a opção global `--working-path` no help e passe um caminho nativo válido.

Critério: raiz, estado inicial, executável, versão e escopo da mudança estão identificados.

## Execução e consulta rápida

Os exemplos abaixo usam o JAR local através de `terminal`; com o binário no PATH escolhido, substitua apenas o prefixo `java -jar pakku.jar` por `pakku`. Substitua os placeholders por identificadores reais previamente verificados; não execute os exemplos literalmente.

| Objetivo | Invocação de `terminal(command=...)` |
| --- | --- |
| Listar projetos | `java -jar pakku.jar ls` |
| Consultar estado | `java -jar pakku.jar status` |
| Consultar atualizações | `java -jar pakku.jar ls --check-updates` |
| Adicionar um projeto preciso | `java -jar pakku.jar add prj --curseforge <slug-ou-id>` |
| Adicionar pelo Modrinth | `java -jar pakku.jar add prj --modrinth <slug-ou-id>` |
| Adicionar pelo GitHub | `java -jar pakku.jar add prj --github <owner/repo>` |
| Adicionar vários projetos | `java -jar pakku.jar add <projeto1> <projeto2>` |
| Remover projeto | `java -jar pakku.jar rm <projeto>` |
| Atualizar somente o alvo | `java -jar pakku.jar update <projeto>` |
| Instalar os arquivos resolvidos preservando desconhecidos | `java -jar pakku.jar fetch --shelve` |
| Fixar estratégia de atualização | `java -jar pakku.jar cfg prj --update-strategy NONE <projeto>` |
| Configurar lado cliente | `java -jar pakku.jar cfg prj --side CLIENT <projeto>` |
| Incorporar somente adições locais | `java -jar pakku.jar sync --additions` |
| Comparar lockfiles | `java -jar pakku.jar diff <lock-anterior> <lock-atual> --verbose` |
| Exportar distribuição | `java -jar pakku.jar export` |

`status` e `ls --check-updates` podem consultar serviços remotos; não prometa execução offline. Para os demais comandos, opções e páginas exatas, leia [a referência de comandos](references/commands.md).

## Procedimento de alteração

1. **Delimite o pedido.** No Lilyvale, preserve Minecraft 1.20.1 e Forge salvo pedido explícito. Inspecione IDs, versões, plataforma, lado e dependências do alvo, incluindo configurações ou scripts que dependam dele. Identifique se o objetivo é mudar a resolução ou apenas baixar o que já está resolvido.
2. **Preserve o estado inicial.** Antes de comandos que alteram arquivos, copie os manifests atuais para o diretório scratch da sessão com Python pela ferramenta `terminal`, se precisar comparar ou recuperar. A cópia deve incluir mudanças preexistentes; não use `git show HEAD` como substituto do estado inicial. Não guarde backups em diretórios de conteúdo do pack.
3. **Aplique somente a operação solicitada.** Use `add`, `rm`, `update` ou `cfg prj` com alvos explícitos. Prefira `add prj` para evitar ambiguidade entre plataformas. Deixe a resolução de dependências ativa; `--no-deps` exige justificativa técnica e validação manual das dependências. Revise dependências removidas ou adicionadas automaticamente.
4. **Revise antes de materializar.** Leia os manifests resultantes e compare com o estado inicial. Preserve as configurações de `pakku.json` e resoluções de `pakku-lock.json` coerentes, sem exigir que ambos tenham um diff quando o comando só precisa alterar um deles. Se a resolução mudar projetos fora do escopo, investigue antes de continuar; não desfaça alterações preexistentes.
5. **Materialize se o pedido envolver a instância.** Execute `fetch --shelve`, com timeout apropriado para downloads. A documentação informa que `--shelve` move arquivos desconhecidos para uma prateleira em vez de apagá-los. Inspecione os arquivos afetados: preservar um JAR na prateleira não significa que ele continue carregando no jogo. Não execute `sync` para corrigir um download incompleto: ele incorpora o estado local ao gerenciamento, em vez de buscar a resolução desejada.
6. **Valide o resultado.** Execute a seção de verificação abaixo. Informe alterações, testes reais e pendências de jogo. Não faça commit, push ou atualização de todos os mods sem solicitação explícita.

Critério: todos os alvos solicitados e mudanças indiretas de dependências estão contabilizados; não há mutações alheias ao pedido.

## Armadilhas e limites

- `fetch` baixa arquivos; `sync` sincroniza o gerenciamento com arquivos locais; `update` muda versões de projetos. Não são operações intercambiáveis.
- Não use `update --all`, `rm --all`, `init`, `import`, `set`, `remote` ou `remote update` como tentativa genérica de reparo. São operações amplas, algumas capazes de mudar a base do pack; execute somente no escopo autorizado e após ler a documentação específica.
- Não acrescente `--yes` global por padrão. Ele responde afirmativamente a todos os prompts e pode aprovar efeitos não revisados.
- `cfg --version` muda a versão do modpack; `set --mc-versions` muda Minecraft. `cfg prj --update-strategy NONE` controla a estratégia, não seleciona sozinho um arquivo específico. As docs locais não documentam um seletor para fixar uma versão exata de projeto: consulte o help antes de prometer esse fluxo.
- Use `--help`, especialmente em `diff`: nesse comando `-h` é `--header-size`, não ajuda. `-D` é `--no-deps` em `add`/`rm`, mas `--deps` em `import`.
- Os documentos locais contêm tags XML de templates não expandidos; não as copie como comandos. Valores e semântica ausentes (por exemplo, detalhes de `link`) exigem ajuda adicional, não suposições.
- O binário 1.4.0 observado expõe `insp`; as docs locais e o JAR 1.2.1 não o documentam. Consulte o help desse binário antes de usá-lo; não trate a disponibilidade como universal.
- Não leia, imprima ou grave credenciais em manifests, comandos registrados ou arquivos da skill. Para erros de autenticação, leia apenas as páginas de ajuda de `credentials`; peça configuração segura pelo usuário, sem solicitar chaves no chat. `credentials --delete` apaga todas as credenciais e não é diagnóstico.
- Em Windows/Git Bash, use caminhos nativos com barras `/` para Java e outros programas nativos. Não presuma que `/c/...` será traduzido para eles.
- JARs novos não entram em uma sessão do Minecraft já iniciada. Reinicie a instância para testar novos mods; `/reload` ou `/ftbquests reload` não carregam novos JARs.

## Verificação

- Confirme código de saída e leia a saída real de cada comando; falha de rede ou download não é sucesso parcial silencioso.
- Valide os dois JSONs com o parser JSON de Python via `terminal`; compare campos e projetos afetados com o snapshot inicial, não só com HEAD.
- Execute `ls` pelo mesmo executável para conferir os projetos. Use `status` se precisar verificar o estado remoto; uma lista de atualizações disponíveis não autoriza aplicá-las.
- Após `fetch`, confira os arquivos reais nos diretórios configurados em `pakku.json`, comparando nomes/versões com o lockfile. Se houver hashes no lockfile, confira-os com Python sem inventar seu algoritmo. Verifique duplicatas de versões e os arquivos movidos para a prateleira.
- Após `export`, localize o artefato indicado pela saída e abra o ZIP/manifest com Python para conferir formato, versão, projetos e overrides. Não declare exportação válida apenas pelo código de saída.
- Revise `git diff --check`, `git diff --stat` e `git status --short`, separando os diffs desta tarefa dos preexistentes. Não inclua saves, logs, mods, build ou configurações pessoais em commits.
- Para mudança de mods, a validação funcional requer iniciar o pack no Prism e conferir logs, dependências e comportamento afetado. Se não foi executada, declare explicitamente a pendência; validação estática não comprova funcionamento no jogo.
