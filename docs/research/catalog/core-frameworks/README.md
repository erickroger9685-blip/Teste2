# Core / frameworks / utilitários

## Veredito

**Não adotar framework de terceiros como "espinha dorsal".** O Knit, principal referência histórica, foi **arquivado em 2024-07-31**. O sucessor comunitário mais citado (Prvd 'M Wrong) diz no README: *"unfinished. Do not use … for production"*. Flamework exige TypeScript. O Nevermore é excelente, mas é um ecossistema inteiro com loader próprio, o que traz lock-in.

**Decisão:** escrever um **bootstrap próprio e fino** (~150–300 linhas: registro de serviços e controllers com `Init`/`Start`, injeção explícita) e **reutilizar utilitários pontuais e bem mantidos**.

| Necessidade | Escolha | Licença | Evidência | Decisão |
| --- | --- | --- | --- | --- |
| Signal, Trove (cleanup), TableUtil, Timer | **Sleitnick/RbxUtil** (só os módulos usados, via Wally `sleitnick/*`) | MIT | 534 commits, 33 autores, 14 testes, commit 2026-07-27 | ✅ READY |
| Cleanup (alternativa) | howmanysmall/Janitor | MIT | strict no projeto, 29 tags | 📖 (escolher um: Trove **ou** Janitor) |
| Promises | evaera/roblox-lua-promise | MIT | 211 commits; último 2023-10 | ✅ só se uma dependência exigir; no código próprio usar `task.*` |
| Estado do cliente + replicação | **littensy/charm** + charm-sync | MIT | 129 commits, 30 testes, strict no projeto, 33 tags | ✅ READY |
| ECS (escala) | **Ukendio/jecs** | MIT | 860 commits, 54 autores, 92 commits em 12m | 🛠️ avaliar na Fase 5/10 |
| Console dev/admin | **evaera/Cmdr** | MIT | push 2026-08-14 | ✅ com permissões restritas no servidor |
| Framework | Knit / AeroGameFramework | MIT | arquivados | ⛔ |
| Framework | Prvd 'M Wrong | MPL-2.0 | autor desaconselha produção | ⛔ |
| Framework | Flamework | MIT | requer roblox-ts | 📖 |
| Framework/libs | Nevermore | MIT | monorepo com loader próprio | 📖 (consultar Octree, Spring, CameraStack) |

## Contrato do bootstrap próprio (resumo)

```lua
-- src/shared/Core/Types.luau
export type Service = {
	Name: string,
	Dependencies: { string }?,        -- ordem de Init resolvida por nome
	Init: ((self: Service) -> ())?,   -- sem yield; só wiring
	Start: ((self: Service) -> ())?,  -- pode spawnar loops
}
```

Regras: um serviço por responsabilidade; serviços **não** acessam remotes diretamente (usam o módulo `Net` gerado pelo Blink); todo loop recorrente passa pelo `Scheduler` central (budget por frame).
