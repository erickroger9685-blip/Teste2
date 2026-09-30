# Animação (código)

> Brief §14. Os **arquivos de animação** (assets) estão em [`../../assets/README.md`](../../assets/README.md).

## Veredito

A base é a API oficial (`Animator`, `AnimationTrack`, markers/`KeyframeReached`, `IKControl`). O único utilitário maduro e ativo é **wrello/Animations**. Controladores de combo e blending avançado **não existem prontos** com licença, então viram parte do `AbilityRuntime` (a timeline dispara animações).

**Regra do Server Authority** ([técnicas oficiais](https://create.roblox.com/docs/projects/server-authority/techniques)): **não cachear objetos `AnimationTrack`**. O estado de animação é rebobinado no rollback. Guardar IDs e consultar o Animator com `Animator:GetTrackByAnimationId()` / `GetPlayingAnimationTracks()`.

| Projeto | Licença | Evidência | Decisão |
| --- | --- | --- | --- |
| **wrello/Animations** | MIT | 171 commits, 15 tags, último 2026-02-22; preload/play por rig; Wally e pesde | 🛠️ adaptar (remover cache de tracks; instalar via Wally, não via `InsertService:LoadAsset` como o README sugere) |
| evaera/roblox-animation-transfer | MIT (arquivado) | ferramenta para transferir a posse de animações | 📖 ferramenta |
| michaeldougal/AnimNation | MIT | utilitário de springs e tweens | 📖 |
| Khaomi/Animator | MIT (arquivado) | — | 📖 |
| wes-BAN/crux-animation | MIT | push 2016 | 📖 abandonado |
| Moon Animator 2 | plugin (termos do autor) | ferramenta de autoria amplamente usada | ferramenta (não entra no jogo) |
| Animation Tree, IK procedural, afterimages (DevForum) | não verificados | pistas do gist | — |

## Desenho recomendado

- `AnimationCatalog` (dados): id lógico (`"Combo.Fist.1"`) → asset ID por tipo de rig, com prioridade e *markers* esperados (`Hit`, `CancelWindow`, `ComboWindow`).
- A timeline da habilidade usa **markers** para abrir as janelas de cancel e combo, e o tempo autoritativo da simulação para o hit.
- Procedural (IK de pés, olhar): `IKControl` oficial + Character-Realism (opcional).
