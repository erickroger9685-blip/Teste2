# Tooling de desenvolvimento

> Brief §19: Luau, Roblox Studio, Rojo, Wally, Selene, StyLua, Lune, Git, VS Code.

## Veredito

É a categoria **mais madura e menos arriscada**. Todas as ferramentas escolhidas têm licença permissiva (MIT ou MPL-2.0), estão ativas em 2026 e **não entram no runtime do jogo**. Por isso a MPL não gera obrigação sobre o código do Genesis.

| Função | Escolha | Licença | Atividade (último push) | Alternativas descartadas | Motivo da escolha |
| --- | --- | --- | --- | --- | --- |
| Sync filesystem ↔ Studio | **Rojo** | MPL-2.0 | 2026-07-06 | Argon (Apache-2.0), Lync (LGPL) | Padrão de fato (1.758 stars ao vivo em 2026-09-30); rbx-dom e ecossistema de tipos giram em torno dele |
| Toolchain | **Rokit** | MIT | 2026-05-09 | Aftman, Foreman (gerenciadores anteriores) | Mantido no org rojo-rbx ('next-generation toolchain manager'); instala Rojo, Wally, Selene etc. com versões fixas |
| Pacotes | **Wally** | MPL-2.0 | 2026-09-26 | pesde | Maior catálogo; a maioria dos candidatos escolhidos publica no Wally. Exceções sem `wally.toml` no repositório oficial: SimplePath, spr, RbxCameraShaker e RagdollService, que devem ser vendorizados com o LICENSE. **Fixar escopos oficiais.** |
| Lint | **Selene** | MPL-2.0 | 2026-05-21 | — | Padrão |
| Formatação | **StyLua** | MPL-2.0 | 2026-09-13 | — | Padrão |
| Language server / typecheck | **luau-lsp** | MIT | 2026-09-27 | — | Typecheck `--!strict` no editor e no CI |
| Runtime de scripts e testes offline | **Lune** | MPL-2.0 | 2026-07-03 | — | Validar dados de conteúdo (JSON/Luau), migrações, geração de código |
| Testes | **Jest-Lua** | MIT | 2024-12-23 | TestEZ (arquivado) | Porte do Jest mantido pela org jsdotlua; o TestEZ está arquivado. Pouco movimento desde 2024-12 |
| Tipos de pacotes | **wally-package-types** | MIT | 2026-07-05 | — | Necessário para `--!strict` com `Packages/` |
| Networking codegen | **Blink** | MIT | 2026-09-19 | Zap | Ver [rede](../networking-security/README.md) |
| Assets como arquivos | **Asphalt** | MIT | 2026-07-28 | Tarmac (último push 2024-03) | Upload de imagens e sons por CLI com IDs versionados no repo |
| Deploy/ambientes (opcional) | **Mantle** | MIT | 2026-05-28 | — | IaC para places, badges e produtos (dev/staging/prod) |
| Docs (opcional) | **Moonwave** | MPL-2.0 | 2026-06-02 | — | Docs de API a partir de comentários |
| Integração com IA | **MCP embutido no Studio** | Termos Roblox | anúncio 2026-03-05 | studio-rust-mcp-server (arquivado) | Claude Code listado oficialmente; ver [plano](../../implementation-plan.md) |

## Estrutura de projeto recomendada

```text
genesis-realms/
├── rokit.toml            # rojo, wally, selene, stylua, lune, luau-lsp, blink, asphalt (versões fixas)
├── wally.toml / wally.lock
├── default.project.json  # Rojo
├── selene.toml / stylua.toml / .luaurc ("languageMode": "strict")
├── net/*.blink           # contratos de rede (IDL)
├── content/              # dados de jogo (raças, bloodlines, genes, habilidades, itens, quests, NPCs, regiões)
├── src/
│   ├── client/
│   ├── server/
│   └── shared/
├── tests/                # Jest-Lua (Lune + Studio)
├── lune/                 # scripts: validar content, gerar tabelas, migrar dados
└── THIRD_PARTY.md        # pacote, escopo, versão, licença, commit, link da auditoria
```

## Riscos

- **Supply chain do Wally:** o registro tem muitos re-uploads (ver [checklist §C](../../00-methodology/security-checklist.md)). Mitigação: `wally.lock` commitado, versões exatas e revisão de diff a cada atualização.
- **Mistura de ferramentas:** não usar Rojo junto com Argon/Lync, nem Wally junto com pesde, no mesmo projeto.
