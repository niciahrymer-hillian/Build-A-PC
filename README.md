# Build-A-PC

### Assemble a desktop PC from parts: compatibility, assembly, BIOS/UEFI, and OS install.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**.

## What this is

We're building a desktop computer from individual parts — not because it's cheaper than buying one
prebuilt (it often isn't), but because choosing genuinely compatible parts, assembling them without
breaking anything, and diagnosing a machine that won't turn on afterward turns "the computer" from a
sealed appliance into an object with parts you can name. The four lessons follow the real cost order of
mistakes: get compatibility right before buying anything (cheapest mistake to avoid), assemble carefully
(moderate cost to redo), configure firmware correctly (cheap to fix, easy to miss), and know how to
diagnose a dead build systematically instead of guessing (the skill that actually matters when something
inevitably doesn't work the first time). Practice that last part risk-free in the **POST Troubleshooting
Simulator** tab before a real board won't boot on you.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| Nothing else required to start | Real PC parts only needed for the hardware appendix — see below before buying anything |

## Items Needed

Covered in the [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below and
the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#build-a-pc) (this one's priced as a
whole-build budget rather than a per-part table, since parts interact):

- [ ] CPU + matching motherboard (verify socket + confirm firmware supports your CPU generation)
- [ ] RAM matching the motherboard's supported generation, ideally from its QVL
- [ ] NVMe SSD storage
- [ ] PSU sized with headroom (not the bare minimum) for your components
- [ ] Case with a coherent airflow path (intake + exhaust, not just fans pointed randomly)
- [ ] CPU cooler + a pea-sized amount of thermal paste (most coolers include enough pre-applied)
- [ ] Anti-static wrist strap
- [ ] A USB drive (8GB+) for bootable installation media
- [ ] GPU only if your workload actually needs one

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Compatibility) first**, then do the practice exercise: verify a hypothetical
   CPU/motherboard/RAM combination using the manufacturer's own documentation, not a retailer listing.
3. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 11 failing tests. Open `exercises/compatibility_checker.py` and implement the four
   functions — full instructions in [`exercises/README.md`](exercises/README.md).
4. **Work Lesson 2 (Assembly)**, then open the **POST Troubleshooting Simulator** tab and work through
   Scenario 1.
   > ⚠️ **You may get stuck here:** the simulator lets you check items in any order on purpose — real
   > troubleshooting isn't rigidly linear. Notice how many checks it takes you versus the systematic
   > order Lesson 4 describes.
5. **Work Lesson 3 (BIOS/UEFI)** and Lesson 4 (OS install, thermals, troubleshooting), working through
   Scenarios 2 and 3 in the simulator as you go.
6. **Then the Quiz**, then Flashcards/Match/Pop Quiz for review.
7. **When building for real:** follow `docs/LESSON_PLAN.md`'s Build Order, which links a real assembly
   walkthrough video at the cabling/seating step.
8. **Check the Report Card tab** any time — it shows your best (fewest-checks) run per POST scenario.
   Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Hands-on |
|---|---|---|---|
| 1 | Compatibility | Socket, RAM generation, QVL, PSU headroom | `exercises/compatibility_checker.py` |
| 2 | Assembly | ESD safety, test-boot order, the most-forgotten cable | POST Troubleshooting Simulator: Scenario 1 |
| 3 | BIOS/UEFI | Boot order, XMP, thermal paste application | *(hardware appendix)* |
| 4 | OS install, thermals & troubleshooting | Bootable media, airflow, systematic no-POST order | POST Troubleshooting Simulator: Scenarios 2 & 3 |

**Learning path:**
```
Lesson 1 (compatibility)  →  Lesson 2 (assembly)  →  Lesson 3 (BIOS/UEFI)  →  Lesson 4 (OS/thermals)
        ↓                           ↓                                                ↓
exercises/ (compatibility_checker.py)                          POST Troubleshooting Simulator (all 3 scenarios)
        ↓
   Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide (what to look for & red flags)

**Parts list:** CPU, motherboard (matching socket + chipset), RAM (matching DDR generation and speed the
board supports), storage (NVMe SSD), PSU, case, and cooling. GPU only if the workload needs one.

**What to look for:** verify CPU-socket and RAM-generation compatibility on the board's official QVL
before buying anything. Size the PSU with headroom (a quality 550–650W unit covers most non-GPU builds)
and prefer 80+ Bronze or better from a known brand — the PSU is the one part whose failure can damage
everything else.

**Red flags:** unbranded or wildly cheap PSUs, "OEM" CPUs from marketplace sellers with no packaging,
RAM priced far below market, and sealed-box listings with stock photos only. Counterfeit and relabelled
storage is common — check the drive's real capacity and speed after install rather than trusting the
label.

**Common failure points:** RAM not fully seated (the usual cause of a no-POST), forgetting the CPU power
cable, over-tightened cooler mounts, and a case with insufficient airflow that throttles under load.

## Why This Matters (Industry Application)

Hardware literacy pays off in unexpected places: sizing cloud instances sensibly, diagnosing whether a
problem is code or capacity, and talking credibly with infrastructure teams. It also removes a category
of intimidation — machines stop being magic.

## How This Connects

Chain K (Hardware & Systems Foundations). Applies **Machine-Under-The-Hood**; the resulting machine
hosts **Linux-On-Old-Hardware** experiments.

## Project Layout

```
Build-A-PC/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, POST sim, report card
│   ├── LESSON_PLAN.md           # short build-plan reference, with a step-specific assembly video
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page rule recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── compatibility_checker.py # skeleton — implement the 4 functions
│   ├── test_compatibility_checker.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
