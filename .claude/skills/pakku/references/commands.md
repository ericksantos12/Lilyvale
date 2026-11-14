# Referência dos comandos Pakku

Resumo das 20 páginas de `.pakku/docs/`. Os caminhos abaixo são relativos à raiz do repositório; abra-os com `read_file`. Não são links relativos a esta pasta. Para execução, use `terminal(command="java -jar pakku.jar <comando> ...")` na raiz ou o binário escolhido no procedimento principal. Consulte `--help` antes de usar valores que as páginas não especificam.

| Comando | Argumentos e opções documentados | Fonte local |
| --- | --- | --- |
| `init` | `--name`, `--version`, `--mc-versions` (`--mc-v`), `--loaders`, `--target`; inicializa pack | `.pakku/docs/pakku-init.md` |
| `import <path>` | `--deps` (`-D`) resolve dependências ao importar | `.pakku/docs/pakku-import.md` |
| `add [<projects>...]` | `--no-deps` (`-D`), `--type` (`-t`) | `.pakku/docs/pakku-add.md` |
| `add prj` | `--curseforge` (`--cf`), `--modrinth` (`--mr`), `--github` (`--gh`), `--type` (`-t`); plataformas aceitam slug/ID ou repositório conforme o help | `.pakku/docs/pakku-add-prj.md` |
| `rm [<projects>...]` | `--all` (`-a`), `--no-deps` (`-D`) | `.pakku/docs/pakku-rm.md` |
| `update [<projects>...]` | `--all` (`-a`) | `.pakku/docs/pakku-update.md` |
| `ls` | `--check-updates` (`-c`), `--name-max-length` | `.pakku/docs/pakku-ls.md` |
| `status` | Consulta o estado do modpack | `.pakku/docs/pakku-status.md` |
| `fetch` | `--retry` (`-r`), quantidade opcional, padrão 2; `--shelve` preserva desconhecidos movendo-os para uma prateleira | `.pakku/docs/pakku-fetch.md` |
| `sync` | `--additions` (`-A`), `--removals` (`-R`), `--updates` (`-U`); sincroniza com arquivos locais | `.pakku/docs/pakku-sync.md` |
| `cfg` | `--name` (`-n`), `--version` (`-v`), `--description` (`-d`), `--author` (`-a`), `--mods-path`, `--resource-packs-path`, `--data-packs-path`, `--worlds-path`, `--shaders-path` | `.pakku/docs/pakku-cfg.md` |
| `cfg prj [<projects>...]` | `--type` (`-t`), `--side` (`-s`), `--update-strategy` (`-u`), `--redistributable` (`-r`), `--subpath` (`-p`), `--alias` (`-a`) | `.pakku/docs/pakku-cfg-prj.md` |
| `set` | `--target` (`-t`), `--mc-versions` (`-v`), `--loaders` (`-l`); altera propriedades do lockfile | `.pakku/docs/pakku-set.md` |
| `link <projectout> <projectin>` | Liga um projeto a outro; as páginas não detalham os efeitos da direção, portanto preserve a ordem e investigue antes de executar | `.pakku/docs/pakku-link.md` |
| `diff <old-lock-file> <current-lock-file>` | `--markdown-diff`, `--markdown`, `--verbose` (`-v`), `--header-size` (`-h`, padrão 2); ajuda somente com `--help` | `.pakku/docs/pakku-diff.md` |
| `export` | `--show-io-errors`; exporta o pack, sem formato/destino configuráveis documentados nessa página | `.pakku/docs/pakku-export.md` |
| `remote [<url>]` | `--branch` (`-b`), `--retry` (`-r`, quantidade opcional, padrão 2), `--server-pack` (`-S`), `--remove` (`--rm`); instala de Git ou remove o remote | `.pakku/docs/pakku-remote.md` |
| `remote update` | Atualiza o pack a partir de seu remote, não apenas os mods individualmente | `.pakku/docs/pakku-remote-update.md` |
| `credentials` | `--delete` apaga todas as credenciais; não executar para inspeção | `.pakku/docs/pakku-credentials.md` |
| `credentials set` | `--curseforge-api-key` (`--cf-api-key`); somente configuração segura pelo usuário, sem expor o valor | `.pakku/docs/pakku-credentials-set.md` |

## Valores confirmados no help do JAR 1.2.1

Reconferir se o executável ou sua versão mudar:

- `cfg prj --type`: `MOD`, `RESOURCE_PACK`, `DATA_PACK`, `WORLD`, `SHADER`.
- `cfg prj --side`: `CLIENT`, `SERVER`, `BOTH`.
- `cfg prj --update-strategy`: `LATEST`, `NONE`.
- `cfg prj --redistributable`: `true`, `false`.
- Opções globais observadas: `--version`, `--working-path=<path>`, `--yes` (`-y`), `--debug`, `--generate-completion=(bash|zsh|fish)`, `--generate-docs`, `--help`.
- Não execute `--generate-docs` sobre as docs existentes como forma de consulta: a tarefa de gerenciar mods não autoriza regenerar documentação.

## Escolha do fluxo

- **Novo mod:** verificar identidade e compatibilidade → `add prj` → revisar dependências/resolução → `fetch --shelve` → conferir JARs → reiniciar e testar.
- **Remover mod:** rastrear dependentes/scripts → `rm <projeto>` → revisar remoções indiretas → materializar se solicitado → conferir instância.
- **Atualizar mod:** conferir escopo → `update <projeto>` → revisar versão e dependências → `fetch --shelve` → testar regressões.
- **Só faltam arquivos:** conferir lockfile existente → `fetch --shelve`; não atualizar as versões para resolver ausência de JARs.
- **Arquivos adicionados manualmente intencionalmente:** revisar todos os candidatos → `sync --additions` → conferir projetos reconhecidos e resoluções; não rodar um sync amplo sobre estado local desconhecido.
- **Distribuir pack:** revisar configuração/overrides e resolução → `export` → abrir artefatos e manifests → informar caminhos reais.
- **Criar/importar/instalar remote:** usar destino isolado ou autorização explícita para alterar a instância atual; consultar páginas e help específicos antes de executar.
