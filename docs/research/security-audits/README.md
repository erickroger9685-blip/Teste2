# Auditorias de segurança da shortlist

Foram clonados 49 repositórios no scratchpad (fora deste repo). Nenhum código de terceiros foi copiado para cá. Em cada um rodou uma varredura estática (ver [checklist](../00-methodology/security-checklist.md)) e, nos candidatos a integração, houve leitura manual das fronteiras de confiança (`OnServerEvent`/`OnServerInvoke`).

Os arquivos binários `.rbxm`/`.rbxl` não podem ser auditados por texto. Por isso os scripts foram **extraídos com um parser mínimo do formato binário** (LZ4/zstd, chunks INST/PROP, propriedade `Source`) e passaram pelo mesmo grep.

## Resumo

| Repositório | Commit | Status manual | Veredito |
| --- | --- | --- | --- |
| [1Axen/blink](1Axen__blink.md) | `86b04ef50101` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [1Axen/Secure-Cast](1Axen__Secure-Cast.md) | `fe3c585d5803` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [1ForeverHD/TopbarPlus](1ForeverHD__TopbarPlus.md) | `f44992bf0299` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [1ForeverHD/ZonePlus](1ForeverHD__ZonePlus.md) | `3bb4bdb5eb0b` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [anthony0br/DocumentService](anthony0br__DocumentService.md) | `9984256b7e35` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Asiandayboy/InventoryMaker](Asiandayboy__InventoryMaker.md) | `abe56671cc41` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Brawldude2/RagdollService](Brawldude2__RagdollService.md) | `c9a7b61c7459` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [CatSushi/MuchachoHitbox](CatSushi__MuchachoHitbox.md) | `cbbeb393e13f` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [centau/vide](centau__vide.md) | `b010497a0161` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Defaultio/BehaviorTree3](Defaultio__BehaviorTree3.md) | `c0430ad861e3` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [dphfox/Fusion](dphfox__Fusion.md) | `2790f7b6272b` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [easy-games/chickynoid](easy-games__chickynoid.md) | `8c3b643526f2` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [EgoMoose/rbx-wallstick](EgoMoose__rbx-wallstick.md) | `02793758b912` | ATENÇÃO | ⚠️ Usar com mitigação |
| [evaera/Cmdr](evaera__Cmdr.md) | `338c0e9a28b4` | OK (seguro por padrão, com ressalvas) | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [evaera/roblox-lua-promise](evaera__roblox-lua-promise.md) | `031d429c82ee` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [ffrostfall/ByteNet](ffrostfall__ByteNet.md) | `fbdb156b6daf` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Fraktality/spr](Fraktality__spr.md) | `665be1721c2a` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [grayzcale/simplepath](grayzcale__simplepath.md) | `f072cb39630c` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Gzeu/roblox-procedural-worlds](Gzeu__roblox-procedural-worlds.md) | `304ae16b814f` | OK (escopo amplo) | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [hatmatty/AMS](hatmatty__AMS.md) | `7d4869bce678` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [howmanysmall/Janitor](howmanysmall__Janitor.md) | `47acf39d7b26` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [littensy/charm](littensy__charm.md) | `b05f3a9de6fc` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [MadStudioRoblox/ProfileStore](MadStudioRoblox__ProfileStore.md) | `45c9847cbcf1` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [MadStudioRoblox/Replica](MadStudioRoblox__Replica.md) | `9cae236aee84` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [MaximumADHD/Character-Realism](MaximumADHD__Character-Realism.md) | `79502561998a` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [michaelvqq/RollbackHitbox](michaelvqq__RollbackHitbox.md) | `11ceb4b531c3` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [nezuo/lapis](nezuo__lapis.md) | `e217a2244f9c` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [osyrisrblx/t](osyrisrblx__t.md) | `1dbfccc182d5` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [paradoxum-games/lyra](paradoxum-games__lyra.md) | `e8927a9daa7c` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [prooheckcp/RobloxStateMachine](prooheckcp__RobloxStateMachine.md) | `2f7113a1e774` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [prooheckcp/RoQuest](prooheckcp__RoQuest.md) | `ab9fff87b846` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Pyseph/ClientCast](Pyseph__ClientCast.md) | `3e3c0bd7b329` | ATENÇÃO (confiança no cliente) | ⚠️ Usar com mitigação |
| [Pyseph/ObjectCache](Pyseph__ObjectCache.md) | `5775fc7a9272` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [red-blox/zap](red-blox__zap.md) | `8cd17ab78192` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [ryanlua/satchel](ryanlua__satchel.md) | `f95bc61aef18` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [SirMallard/Iris](SirMallard__Iris.md) | `801973f1c3e0` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Sleitnick/RbxCameraShaker](Sleitnick__RbxCameraShaker.md) | `15412099389d` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Sleitnick/RbxUtil](Sleitnick__RbxUtil.md) | `31f9120fca02` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Swordphin/raycastHitboxRbxl](Swordphin__raycastHitboxRbxl.md) | `ed076f39a30b` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [TeamSwordphin/ShapecastHitbox](TeamSwordphin__ShapecastHitbox.md) | `ac5c0e0a9fe7` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [text21/Rewind](text21__Rewind.md) | `1bb0703f20d3` | OK (mas sem licença) | ⛔ Bloqueado por licença |
| [Ukendio/jecs](Ukendio__jecs.md) | `0ca7a3b54a06` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [wad4444/refx](wad4444__refx.md) | `fd1631088d4a` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [wad4444/WCS](wad4444__WCS.md) | `091a53e2e82b` | OK com ressalvas | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [weenachuangkud/FastCast2](weenachuangkud__FastCast2.md) | `5dc4503f2071` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [wrello/Animations](wrello__Animations.md) | `6263dc7bd13d` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [YetAnotherClown/planck](YetAnotherClown__planck.md) | `c0c61804f7b2` | OK | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [zilibobi/forge-vfx](zilibobi__forge-vfx.md) | `f3faf4f42ce4` | OK (licença custom) | ✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo) |
| [Zyn-ic/Stoway](Zyn-ic__Stoway.md) | `ed64b7e46df8` | ACHADO CRÍTICO | ⛔ Bloqueado até correção |

## Principais achados

1. **Stoway: debug aberto em produção.** Qualquer jogador pode usar `/add <item> <qtd>` no chat (commit `ed64b7e46df8`). Também depende de um fork não oficial do Fusion (`acecateer/fusion`).
2. **ClientCast: confiança no cliente.** O servidor aceita o resultado do raycast do cliente sem validação geométrica.
3. **Wallstick e Character-Realism: remotes de retransmissão sem rate limit.** Wallstick também não valida tipos.
4. **Nenhum backdoor clássico encontrado:** nenhum `require(assetId)`, nenhum `loadstring` fora de libs de teste, nenhum webhook. A única chamada HTTP de saída é o comando admin `fetch` do Cmdr, bloqueado por padrão sem hook `BeforeRun`.
5. **Supply chain no Wally.** Há dezenas de re-uploads e forks de pacotes populares com escopos de terceiros (ex.: 24 escopos distintos publicam um pacote chamado `profilestore`). Fixe sempre o escopo do autor original e a versão exata.
6. **Repositórios vazios aparecem nas buscas.** `aziz8235/roblox-luau-game-framework` e `KURVOX/roblox-ai-npc` só têm README e LICENSE.
