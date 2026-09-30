# Critérios de avaliação

## Classificação de recomendação (brief §24)

| Classificação | Quando se aplica |
| --- | --- |
| ✅ **READY TO INTEGRATE** | Licença permissiva confirmada (MIT/Apache/BSD/ISC/MPL com uso de arquivo inalterado). Auditoria sem bloqueios (ou ferramenta de build que não entra no jogo). API estável. Não duplica responsabilidade de outro componente do stack. Entra atrás de um *adapter* fino com pouca ou nenhuma modificação. |
| 🛠️ **REQUIRES ADAPTATION** | Licença ok, mas é preciso mudar código ou arquitetura antes de usar. Motivos típicos: loop próprio que conflita com o Server Authority, dependência não oficial, achado de segurança corrigível, beta oficial, licença custom a revisar. |
| 📖 **USE AS REFERENCE ONLY** | Útil como **design/ideia**. Não deve entrar no jogo, por um destes motivos: parado ou arquivado, pilha tecnológica incompatível (TypeScript/Flamework), duplica outro componente escolhido, escopo errado, ou só binário. Consultar é permitido quando a licença deixa; **copiar trechos só com licença permissiva e atribuição**. |
| ⛔ **DO NOT USE** | Sem licença (**"NÃO CONFIRMADO — NÃO USAR ATÉ VERIFICAR"**), proprietário, copyleft incompatível (GPL/LGPL no runtime do jogo), arquivado com sucessor oficial, autor desaconselha produção, repositório vazio, ou achado de segurança sem mitigação. |

## Dimensões avaliadas (brief §23)

Em cada candidato da shortlist:

| Dimensão | Evidência objetiva usada |
| --- | --- |
| **Arquitetura** | Separação client/server/shared nas pastas, APIs públicas, dependências declaradas e vendorizadas, pressupostos (Humanoid, Tools, Character). |
| **Código** | Arquivos `--!strict` sobre o total, LOC, testes, CI (workflows), docs (site/Moonwave/README). |
| **Segurança** | Resultado do grep ([checklist](security-checklist.md)), leitura dos remotes (validação, rate limit, confiança no cliente). |
| **Performance** | Conexões por instância versus loop central, criação de instâncias no servidor, retransmissão `FireAllClients` sem limite, uso de Parallel Luau. |
| **Integração** | `wally.toml`, `default.project.json`, formato de distribuição (Wally, `.rbxm` ou Creator Store), dependências que conflitam com o stack. |
| **Maturidade** | Data do último commit, commits nos últimos 12 meses, número de autores, tags/releases, arquivamento, avisos do próprio autor. **Stars não entram como qualidade.** |

## Critérios objetivos para Top Candidates (brief §28)

Não há nota numérica arbitrária. Cada categoria compara os candidatos nestes eixos, e cada afirmação cita a evidência:

1. **Compatibilidade arquitetural:** funciona com Server Authority, `BindToSimulation`, IAS e StreamingEnabled; não traz rede ou loop próprio concorrente.
2. **Maturidade:** commits, autores, tags, idade, atividade recente e uso em produção declarado.
3. **Documentação:** site de docs dedicado, README com API ou só post no DevForum.
4. **Esforço de integração:** número de dependências, necessidade de fork e tamanho da adaptação estimada em arquivos.
5. **Segurança:** resultado da auditoria.
6. **Cobertura funcional:** quantos requisitos do brief o componente cobre.

Em empate técnico, vale a regra **"um componente por responsabilidade"**: escolhe-se o que exige menos código de cola dentro do stack já escolhido.
