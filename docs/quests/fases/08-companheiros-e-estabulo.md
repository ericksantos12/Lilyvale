# F08 — Companheiros e estábulo

**Estado: não iniciada.** Este documento autoriza apenas o planejamento; implementar esta fase exige solicitação explícita do usuário.

[Índice de execução](README.md) · [Regras e arquitetura do plano](../planejamento.md) · [Catálogos candidatos](../catalogos-candidatos.md)

## Entrega incremental

Capítulos sob responsabilidade desta fase: **CC01, CC02**. Executar um lote coerente, validar e registrar o resultado antes de ampliar o escopo.

## Entrada e bloqueios locais

- F00 aceita e F01.1 aprovado.
- Espécie/variante sem fonte ou identificação confiável fica fora da coleção publicada.
- Doma, reprodução e passeio só usam evento se testado; observação não comprova vínculo e checkmark deve ser explícito.

## Checklist de execução futura

- [ ] Auditar quais espécies permitem encontro, vínculo, cuidado e reprodução na versão instalada.
- [ ] Entregar cartões de cuidado e projetos de habitat sem exigir capturar toda a fauna.
- [ ] Montar galeria seletiva de encontros e o álbum de raças com um contrato consistente de observação ou doma.
- [ ] Aplicar os limites da blacklist de Carry On como informação; não modificar o comportamento do mod para contornar uma quest.

## Fora do escopo

- Não implementar fases não solicitadas, mudar mods/receitas ou iniciar integrações de detecção não aprovadas.
- Não apagar progresso, duplicar IDs/recompensas, commitar configs pessoais ou tocar no estado de outras tarefas.
- Não converter a ordem de trabalho em dependências obrigatórias de gameplay.

## Validação e aceite

- [ ] Testar uma espécie por comportamento publicado, não apenas spawn eggs.
- [ ] Conferir que não há morte de pets, dano proposital ou pedigree perfeito como requisito.
- [ ] Validar cuidado/cavalo em equipe e em jogador solo conforme política aprovada.

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

### CC01 — Pequenos e Grandes Companheiros

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | Encontrar não é domesticar — nota de bem-estar e diferença entre animal selvagem, criável e pet; D/P | Não assumir que todo Naturalist é domesticável |
| A2 | Uma casa do tamanho certo — roda/túnel de hamster e recinto; I/O, depois P do espaço | Não usar Carry On com animais bloqueados |
| A3 | Aprender uma interação — cuidado/alimentação específica de uma espécie realmente suportada; E/P | Uma dica por mecânica distinta, não uma por mob |
| M1 | Um companheiro acolhido — estabelecer vínculo/cuidado de uma espécie válida; E/P | Observação simples não comprova vínculo |
| C1 | Quintal vivo — habitat/abrigo para uma escolha de animais; P | Não obrigar capturar toda a fauna |
| C2 | Pequenos vizinhos — projeto com hamsters e enriquecimento; P | Não transformar o hamster em coleção de drops |
| Q1 | Encontro registrado: `<espécie>` — O/E para fauna selecionada de Critters and Companions e Naturalist | Observar, não matar nem entregar spawn eggs |
| Q2 | Companheiro conhecido: `<variante>` — variantes de hamster somente se distinguíveis legitimamente | Não comparar NBT arbitrário sem inspeção |

Somente animais com reprodução confirmada recebem desafios de criar filhotes. Não transformar Critters and Companions em uma coleção de itens obtidos matando os próprios companheiros.

### CC02 — Vida no Estábulo

| Nó | Proposta e conclusão | Relação |
| --- | --- | --- |
| A1 | O primeiro vínculo — domar um cavalo válido; E | Posse de sela não prova doma |
| A2 | Conhecer seu parceiro — equipamento/sela que permite a interação instalada; I + nota de estatísticas | Não inferir raças de cavalo vanilla |
| A3 | Cuidar antes da viagem — cuidado e uma peça de equipamento adequada; I/E/P | Não pedir ferir o animal para demonstrar cura |
| A4 | Trabalho ou passeio — introduzir carroça e função útil confirmada; I/O | Alternativa de uso, sem exigir todos os acessórios |
| M1 | Uma volta juntos — passeio com o cavalo cuidado; P/E | Sem distância falsa por item |
| C1 | Um estábulo acolhedor — projeto com espaço, comida e acesso; P | Criar não equivale a confinar todas as raças |
| C2 | Uma nova geração — reprodução legítima; E após verificar espécie/condições | Não exigir pedigree perfeito |
| Q1 | Raça conhecida: `<raça>` — observação ou doma; escolher o mesmo contrato em todo o álbum | As 15 raças registradas são candidatas, não 15 animais a manter presos |

Equipamentos especiais e desafios de estatísticas ficam em consulta/C. Sem sorte extrema de reprodução como degrau de progressão.
