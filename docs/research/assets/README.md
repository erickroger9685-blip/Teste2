# Seção F.2 — ASSETS (regime de licença separado do código)

> Modelos, mapas, construções, ambientes, terreno, cavernas, texturas, VFX, animações e sons.
> **Código** é avaliado em [`../catalog/`](../catalog/). Aqui, só **conteúdo**. Uma licença de código (MIT etc.) **não cobre** os assets que vêm dentro de um `.rbxl`/`.rbxm`.

## Regra da IP original (brief §1)

Nenhum asset, nome, logo, música, animação proprietária ou modelo que imite Naruto, Dragon Ball, Bleach, One Piece, Jujutsu Kaisen ou outra franquia. A Roblox trata infração de IP como violação dos Termos de Uso, com remoção de conteúdo e da conta ([IP licensing](https://create.roblox.com/docs/ip-licensing/creators)). Inspirações de gênero e mecânica são permitidas. A **execução visual e sonora precisa ser original**.

## Fontes e regimes de licença

| Fonte | O que oferece | Licença (verificada) | Pode usar no Genesis? | Observações |
| --- | --- | --- | --- | --- |
| **Roblox Creator Store** (modelos, meshes, decals, áudio, plugins) | tudo | Termos do Creator Store: licença para usar o asset **no Roblox Studio e em experiências Roblox**, conforme os Termos de Uso ([Creator Store Terms](https://en.help.roblox.com/hc/en-us/articles/21308223046932-Creator-Store-Terms)) | ✅ dentro do Roblox, **após auditoria** | Não garante que quem publicou tinha os direitos. Modelos podem conter scripts maliciosos. **Nunca escolher por número de avaliações** ([checklist §D](../00-methodology/security-checklist.md)). |
| **Assets e templates da própria Roblox** (templates Laser Tag, Platformer, bibliotecas oficiais) | kits, ambientes, código de exemplo | [Limited Use License](https://create.roblox.com/docs/resources/limited-use-license): uso **somente na plataforma Roblox**, manter atribuições, revogável | ✅ como base de protótipo | Proibido usar em serviço concorrente ou fora do Roblox. |
| **Música licenciada da Roblox** (catálogo APM e outros) | trilhas | Uso livre **dentro** de experiências Roblox, até 250 faixas licenciadas por experiência; **não exportar** para fora da plataforma ([Using Licensed Music](https://en.help.roblox.com/hc/en-us/articles/360000927163-Using-Licensed-Music-on-Roblox)) | ✅ só in-game | Trailers fora da plataforma precisam de outra licença ([Licensed Music in Videos](https://en.help.roblox.com/hc/en-us/articles/360038525351-Using-Licensed-Music-in-Videos)). |
| **Áudio próprio enviado** | SFX e música | O uploader concede à Roblox uma licença ampla ([Audio Upload License Agreement](https://en.help.roblox.com/hc/en-us/articles/23359485439124-Audio-Upload-License-Agreement)) | ✅ | Só enviar áudio que o estúdio **possui** ou tem licença para sublicenciar. |
| **Quaternius** (Universal Animation Library 1/2, Universal Base Characters) | 120–130+ animações humanoides (locomoção, combate), personagens | **CC0** ([UAL](https://quaternius.com/packs/universalanimationlibrary.html)) | ✅ | Precisa de **retarget para R15** (Blender). Ótima base para placeholder e locomoção. |
| **Kenney** | modelos 3D, texturas, UI, áudio | **CC0** ([suporte Kenney](https://kenney.nl/support)) | ✅ | Estilo low-poly; bom para protótipo. |
| **Poly Haven** | HDRIs, texturas PBR, modelos | **CC0** ([licença](https://polyhaven.com/license)) | ✅ | Texturas para SurfaceAppearance/MaterialVariant. |
| **ambientCG** | materiais PBR, HDRIs | **CC0 1.0** ([licença](https://docs.ambientcg.com/license/)) | ✅ | Idem. |
| **Mixamo (Adobe)** | animações e personagens rigados | Uso royalty-free em projetos comerciais, **inclusive jogos**. Proibido redistribuir os arquivos brutos como pacote ou template ([Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)) | ⚠️ sim, embutido no jogo | **Não publicar** as animações Mixamo como assets públicos/distribuídos no Creator Store (seria redistribuição). Manter privadas no grupo do jogo. Retarget para R15. |
| **Sonniss GDC Game Audio Bundle** | milhares de SFX | Royalty-free, uso comercial, sem atribuição; proíbe vender sons isolados e usar para treinar IA ([licença](https://sonniss.com/gdc-bundle-license/)) | ✅ | Guardar cópia da licença do ano do bundle. |
| **freesound e similares** | SFX | CC0, CC-BY ou CC-BY-NC, **por arquivo** | ⚠️ só CC0 e CC-BY (com crédito) | Rejeitar NC (não comercial). |
| **Roblox/cube (Cube3D)** | modelo de IA de geração 3D | **"CUBE3D RESEARCH-ONLY RAIL-MS LICENSE"** | ⛔ para produção | Licença de pesquisa. As ferramentas de IA **dentro do Studio** têm termos próprios. |
| **Arte do FastCast2** | logos e ícones | **CC BY-NC-ND 4.0** | ⛔ | O código é MIT; a arte não. |
| **Places "uncopylocked" e `.rbxl` de repositórios** | mapas, animações, modelos | Deixar um place copiável **não concede licença** sobre o conteúdo | ⛔ sem licença explícita | Ex.: o `.rbxl` do MaxDevLol Parkour contém ~186 KeyframeSequences de proveniência não documentada. |

## Mapas, cidades, construções, terreno, cavernas

- **Não foi encontrado** mapa ou cidade open source com licença clara e qualidade de produção para um RPG de mundo aberto. O que existe são places de exemplo sem licença, packs genéricos do Creator Store (sujeitos a auditoria) e geradores procedurais (ver [código de mundo](../catalog/world-map/README.md)).
- **Recomendação:** construir o mundo com **kits modulares próprios** (peças de construção, props e materiais) sobre texturas CC0 (Poly Haven, ambientCG) e terreno oficial. Para placeholders, usar Kenney/Quaternius (CC0) e templates oficiais da Roblox (Limited Use License).

## VFX (assets)

- Partículas, texturas de flipbook, beams e trails **próprios** ou CC0. Texturas de VFX do Creator Store só após auditoria e checagem de autoria. Evitar efeitos que reproduzam técnicas icônicas de franquias.
- O plugin VFX Forge (ferramenta) e o módulo `forge-vfx` (runtime, licença custom) estão avaliados em [VFX (código)](../catalog/vfx/README.md).

## Animações

- **Locomoção e placeholders:** Quaternius UAL (CC0), com retarget para R15.
- **Combate com identidade:** animação **própria** (Moon Animator 2, Blender), porque é o coração do "game feel". Mixamo serve para protótipo interno, respeitando a regra de não redistribuir.
- **Roblox Animation Packs / emotes do catálogo:** podem ser usados em experiências conforme os termos do Marketplace. Conferir caso a caso.

## O que auditar em qualquer asset

1. **Autoria e licença** registradas num `ASSETS_LEDGER` (fonte, URL, licença, data, quem aprovou).
2. **Scripts embutidos** em modelos (ver checklist §D).
3. **Referências externas:** `rbxassetid://` de terceiros, que podem ser removidos ou ficar privados.
4. **IP:** semelhança com personagens ou símbolos de franquias.
5. **Performance:** triângulos, texturas 1024+ e número de partes (mobile).
