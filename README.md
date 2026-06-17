# CS2 Recoil Control Practice Tool

<div align="center">

**English** | [**中文**](README_CN.md)

</div>

## Overview

A comprehensive recoil control training tool for Counter-Strike 2 (CS2). This tool helps players practice and master weapon spray patterns through automated input assistance, allowing you to focus on crosshair placement and game sense while learning proper recoil control mechanics.

## Features

- **Multi-weapon Support**: Practice with AK47, M4A1, M4A4, Galil, SG553, FAMAS, AUG, and more
- **Sensitivity Calibration**: Pre-configured scripts for in-game sensitivities from 0.8 to 3.1
- **SMG Training**: Includes MP9, MAC10, UMP45, MP7, MP5SD, Bizon, P90
- **Pistol Practice**: CZ75 and other secondary weapons
- **Customizable Controls**: Assign weapon switches to your preferred mouse buttons

## Quick Start

### Prerequisites

1. **Install Logitech G HUB**
   - Run `lghub_installer.exe` to install the software
   - Restart your computer after installation

2. **Check Your Mouse Model**
   - Refer to [`Button Reference Guide`](【必看按键图】.md) for button numbering
   - Identify which buttons correspond to weapon selections

### Setup Instructions

1. **Select Your Sensitivity Script**
   - Choose the `.lua` file matching your in-game sensitivity
   - Example: For sensitivity 2.5, use `游戏内灵敏度2.5.lua`

2. **Import to Logitech G HUB**
   - Open Logitech G HUB
   - Select your mouse device
   - Navigate to "Scripts" or "Macro" settings
   - Import the selected `.lua` file

3. **Configure Button Bindings**
   - Assign weapon switches to mouse buttons
   - Default configuration:
     - Single click side button: Primary weapon (AK47/M4A4)
     - Double click side button: Secondary weapon
     - Ctrl + side button: Other weapons

4. **Activate and Test**
   - Enable the script in G HUB
   - Enter CS2 and test in practice mode

## File Structure

```
CS2 Practice Gun Takedown/
├── Scripts/                        # Recoil control scripts
│   ├── Sensitivity 0.8.lua        # For 0.8 sensitivity
│   ├── Sensitivity 1.0.lua        # For 1.0 sensitivity
│   ├── ...                         # Other sensitivities (0.8-3.1)
│   └── Sensitivity 3.1.lua        # For 3.1 sensitivity
├── Button Reference/               # Mouse button diagrams
│   └── 【必看按键图】.md            # Button numbering guide
├── Documentation/
│   ├── 使用说明.md                  # Detailed instructions
│   └── 5E无法使用教程.md            # 5E platform troubleshooting
├── Video Tutorial.mp4              # Video walkthrough
├── lghub_installer.exe             # Logitech G HUB installer
└── README.md                       # This file
```

## Training Tips

- **Start Slow**: Begin with single-shot weapons to understand basic patterns
- **Focus on Patterns**: Each weapon has a unique spray pattern - learn them one at a time
- **Use Practice Mode**: Test in CS2's practice mode before competitive matches
- **DPI Matters**: Ensure your mouse DPI is consistent for accurate calibration

## Troubleshooting

### Script Not Working
1. Verify Logitech G HUB is running
2. Check script is properly imported and enabled
3. Confirm correct sensitivity file is selected
4. Verify mouse button bindings

### Recoil Control Inconsistent
1. Match in-game sensitivity exactly to script filename
2. Check for conflicting key bindings
3. Ensure mouse DPI is stable

### 5E Platform Issues
Refer to [`5E Platform Guide`](5E无法使用教程.md) for specific solutions.

## Advanced Usage

The tool supports fine-tuning of recoil parameters including:
- X/Y coordinate offsets for horizontal/vertical control
- Timing delays between shots
- Weapon-specific spray patterns
- Burst fire optimization

## Disclaimer

This tool is designed for practice and training purposes only. Users are responsible for ensuring compliance with their platform's terms of service. Use in competitive environments may violate game policies.

## Support

- Read [`使用说明.md`](使用说明.md) for detailed documentation
- Watch `Video Tutorial.mp4` for visual instructions
- Check [`Button Reference`](【必看按键图】.md) for mouse button layouts

---

**Note**: This tool provides input automation to help learn recoil patterns. For competitive integrity, always verify your platform's rules regarding automated inputs.