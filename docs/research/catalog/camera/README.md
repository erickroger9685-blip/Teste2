# Câmera

> Brief §13: terceira pessoa, câmera de combate, lock-on, câmera de alvo, FOV dinâmico, shake, smoothing, cinemáticas, câmera de habilidade e de chefe.

## Veredito

Existem **peças** boas (shake e springs). Não existe **câmera de combate** reutilizável com licença. Os PlayerScripts padrão foram convertidos para o IAS em junho de 2026, e o CCL está melhorando o Shift-Lock nativo. A câmera própria precisa **coexistir** com o `PlayerModule`, não substituí-lo às cegas.

| Peça | Escolha | Licença | Evidência | Decisão |
| --- | --- | --- | --- | --- |
| Camera shake | **Sleitnick/RbxCameraShaker** | MIT | port do EZ Camera Shake, 478 linhas, estável (último commit 2019-12) | ✅ READY (o repo não tem `wally.toml`: vendorizar o fonte com o LICENSE; evitar re-uploads de terceiros no Wally) |
| Springs (smoothing, FOV, offsets) | **Fraktality/spr** | MIT | arquivo único, 84 commits, 4 autores | ✅ READY |
| Câmera customizada | LugicalDev/CameraService | MIT | visões customizadas | 📖 referência |
| 3ª pessoa | Yiannis123Git/ShiftUnlocked | MIT | push 2024-05 | 📖 |
| Gravidade custom | EgoMoose/gravity-camera | MIT | acompanha wallstick | 📖 |
| Lock-on | EzLockOn | sem licença | — | ⛔ |
| Pilha de câmeras | Nevermore `CameraStackService` (`src/camera`) | MIT | parte do monorepo Nevermore | 📖 referência de arquitetura (pilha de câmeras com prioridade) |

## Desenho recomendado (construir): `CameraDirector`

```text
CameraDirector (cliente)
  pilha de "modos" com prioridade: Exploration < Combat < LockOn < AbilityCinematic < BossIntro
  cada modo produz um CFrame alvo + FOV → suavizado com spr
  pós-processamento: shake (RbxCameraShaker) + hitstop (congela o offset por N ms) + FOV kick
  lock-on: TargetingService (servidor valida o alvo) → LockOnMode (orbita/enquadra atacante+alvo)
  acessibilidade: intensidade de shake e FOV configuráveis (mobile/console)
```

A câmera é **só cliente e cosmética**. Não participa da simulação autoritativa (a documentação do Server Authority manda efeitos para `RenderStepped`).
