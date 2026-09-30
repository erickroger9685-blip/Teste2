# VFX (código)

> Brief §15. Os **efeitos em si** (partículas, texturas, meshes) estão em [`../../assets/README.md`](../../assets/README.md).

## Veredito

- **Pooling:** resolvido com **Pyseph/ObjectCache** (MIT, `--!strict`, 173 linhas). Ele substitui o PartCache original, que não tem licença declarada.
- **Emissão de efeitos compostos:** **zilibobi/forge-vfx** é o módulo de runtime do plugin VFX Forge. É ativo (138 commits em 12m), mas usa **licença custom VFX-DL-1.1**: só em jogos Roblox, derivados com a mesma licença, uso comercial permitido. Precisa de revisão jurídica.
- **Replicação:** o padrão certo é o do **refx** (MIT, roblox-ts): *o servidor nunca instancia VFX*, só envia um evento e cada cliente toca localmente. Como a lib é TS e está parada desde 2024-12, **reimplementar o padrão** com Blink.

| Projeto | Licença | Decisão |
| --- | --- | --- |
| **Pyseph/ObjectCache** | MIT | ✅ READY |
| zilibobi/forge-vfx | Custom (VFX-DL-1.1) | 🛠️ revisão jurídica e dos submódulos (`kohltastrophe/Z`, `dphfox/tiniest`) |
| wad4444/refx | MIT | 📖 padrão de replicação |
| PartCache (DevForum) | sem licença | ⛔ |
| Yuruzuu's VFX, ImpactVFX, VFX Suite (DevForum) | não verificados | pistas; conferir licença dos **assets** antes de qualquer uso |

## Desenho recomendado: `VfxService` e `VfxPlayer`

```text
Servidor: timeline da habilidade emite VfxCue{ cueId, anchor(instância/posição), seed, t0 } via Blink (unreliable quando possível)
Cliente:  VfxPlayer resolve cueId → preset (dados) → instancia do ObjectCache → emite partículas/beams/trails → devolve ao pool
Orçamento: limite de partículas por cue, LOD por distância, qualidade por dispositivo (mobile), descarte se a fila de cues estourar
Rollback:  cues de habilidade predita tocam na hora no cliente do autor e são desfeitos se a predição falhar (padrão oficial: efeitos via estado em atributos + RenderStepped)
```
