# F00 — Contratos e preparação

**Estado: concluída — escopo e contratos aprovados explicitamente pelo usuário.** O aceite encerra somente F00; nenhuma F01 ou implementação de capítulos foi iniciada.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Preparar decisões e evidências que permitem iniciar entregas de conteúdo; não implementar capítulos nesta fase.

## Entrada e bloqueios locais

- Nenhuma aprovação do planejamento anterior é presumida por este desmembramento.
- Pendências de Perfect Plushies, Advanced Netherite e dimensões são locais: podem continuar pendentes sem bloquear fazenda/casa.

## Checklist de execução

- [x] Confirmar o escopo de 49 mods, nove categorias e 30 capítulos-base contra os arquivos atuais; registrar divergências sem alterar o jogo.
- [x] Obter aceite final consolidado das regras editoriais e do escopo. O usuário aprovou encerrar F00 sem iniciar F01, incluindo A/M/C, consulta R, distinção posse/ação, projetos autodeclarados e descoberta por posse.
- [x] Registrar idioma português, alvo de coleções pessoais/marcos compartilhados condicionado à viabilidade, XP novo 50/150/25 e preservação das recompensas históricas.
- [x] Abrir fichas de auditoria para 235 linhas/grupos de objetivos e 277 identidades candidatas, sem promovê-las a aprovadas.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [x] Conferir que cada capítulo tem uma única fase responsável e que não existem mods esquecidos.
- [x] Registrar decisões aceitas, pendências e o que exige autorização separada, especialmente scripts de detecção e alterações de receitas.

- [x] Aplicar o protocolo pertinente ao lote documental: cobertura, propriedade dos capítulos, fontes locais, IDs/referências e parser nativo. Testes visuais/de gameplay de novos conteúdos não se aplicam porque não houve implementação.
- [x] Registrar verificações executadas, limites e o aceite final explícito do usuário.
- [x] Encerrar a F00 após o aceite final. Gates de viabilidade das futuras fases permanecem abertos sem impedir o fechamento dos contratos da F00.

## Como encerrar ou retomar

Atualizar a linha desta fase no índice e preencher a ficha de passagem abaixo. Um bloqueio local deve identificar o nó/lote afetado e os itens que ainda podem ser entregues com segurança. Não substituir o gate por uma detecção falsa.

| Registro | Preencher durante a execução |
| --- | --- |
| Lote executado | F00 — contratos, conferência de escopo e abertura de fichas |
| Arquivos e IDs envolvidos | Apenas documentos; livro existente inspecionado sem alocar ou alterar IDs |
| Decisões e fontes conferidas | `quest-mods.md`, plano/fases, lockfile, JARs e configurações de quests; ver registro detalhado |
| Testes estáticos | 49 mods e versões, nove categorias planejadas, 30 capítulos com dono único; livro atual com 290 quests, IDs/referências válidos e parser nativo em sete arquivos |
| Testes no jogo / evidência | Não executados; nenhum conteúdo de gameplay foi implementado nesta fase |
| Pendências e bloqueios locais | EQ-01/EQ-02 para coleções pessoais/migração de equipe e gates próprios de cada sistema; são pendências das próximas fases, não falta de aceite da F00 |
| Próximo lote seguro | Solicitar F01.1 após aceite, sem iniciá-la automaticamente |
| Aceite do usuário | Aprovar e encerrar F00, sem iniciar F01; políticas e escopo consolidados aprovados explicitamente |

## Registros produzidos

- [Contratos, divergências, testes e gates locais](registros/f00-contratos-e-auditoria.md).
- [Inventário versionado e fichas por objetivo/identidade](registros/f00-inventario.json).
