<h1 align="center">Plai Hackpad</h1>

<p align="center">
  A 3×3 key macropad with a rotary encoder and OLED display, running KMK firmware.
</p>

<p align="center">
  <img src="https://github.com/Romanhery/Plai/raw/main/Images/RENDERING.png" alt="Plai render" width="65%" />
</p>

Built to learn PCB design, CAD, and firmware programming — and it's taught me a lot along the way.

## Features

- 128×32 OLED display for status messages
- EC11 rotary encoder for volume control
- 9 keys for shortcuts and media control

## PCB

<p align="center">
  <img src="https://github.com/Romanhery/Plai/raw/main/Images/schematic.png" alt="Schematic" width="65%" /><br/>
  <sub>Schematic</sub>
</p>

<p align="center">
  <img src="https://github.com/Romanhery/Plai/raw/main/Images/PCB.png" alt="PCB routing" width="65%" /><br/>
  <sub>PCB routing</sub>
</p>

Designed in [KiCad](https://www.kicad.org/).

## CAD

Held together with 5× M3 bolts and heat-set inserts, with two printed pieces housing the electronics.

Designed in Fusion 360.

<p align="center">
  <img src="https://github.com/Romanhery/Plai/raw/main/Images/Cad_img.png" alt="Plai CAD render" width="65%" />
</p>

## Firmware

Built with [KMK](https://github.com/KMKfw/kmk_firmware).

- Volume control via the rotary encoder — twist to adjust, press to mute
- OLED displays a status message
- Fully remappable macros (currently set up for my own shortcuts)

<p align="center">
  <img src="https://github.com/Romanhery/Plai/raw/main/Images/RENDERING.png" alt="Key mapout and display" width="65%" />
</p>

## BOM

| Qty | Part |
|---|---|
| 9× | Cherry MX switches |
| 9× | DSA keycaps |
| 9× | 1N4148 DO-35 diodes |
| 5× | M3×5×4 heat-set inserts |
| 4× | M3×16mm SHCS bolts |
| 1× | 0.91" OLED display |
| 1× | EC11 rotary encoder |
| 1× | Seeed XIAO RP2040 |
| 1× | Case (2 printed parts) |

📋 [Full BOM with purchase links](https://docs.google.com/spreadsheets/d/1uIeMTGPOrdSAiFDxR4G393WpXhlTQVRrd_AwqsaPwl4/edit?usp=sharing)

## Acknowledgements

- [Orpheuspad](https://github.com/hackclub/hackpad/tree/clean/extras/orpheuspad)
- [Keybie](https://github.com/Mirai-09/Keybie-Hackpads)

## Authors

- [@Romanhery](https://github.com/Romanhery)
