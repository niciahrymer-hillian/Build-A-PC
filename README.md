# Build-A-PC

### Assemble a desktop PC from parts: compatibility, assembly, BIOS/UEFI, and OS install.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md) · [🎮 Interactive Tour](docs/interactive/index.html)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content to be built. Real-hardware build with an emulation/planning-first path. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

I wanted to stop treating the computer as a sealed appliance. Choosing parts that are actually compatible,
assembling them without breaking anything, getting into BIOS/UEFI, and installing an OS from scratch turns
an abstraction into an object with parts I can name.

It's also the cheapest way to understand the tradeoffs I read about constantly — why more RAM helps some
workloads and not others, what a faster SSD actually changes, and where the money goes.

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** CPU, motherboard (matching socket + chipset), RAM (matching DDR generation and speed the
board supports), storage (NVMe SSD), PSU, case, and cooling. GPU only if the workload needs one.

**What to look for:** verify CPU-socket and RAM-generation compatibility on the board's official QVL before
buying anything. Size the PSU with headroom (a quality 550–650W unit covers most non-GPU builds) and prefer
80+ Bronze or better from a known brand — the PSU is the one part whose failure can damage everything else.

**Red flags:** unbranded or wildly cheap PSUs, "OEM" CPUs from marketplace sellers with no packaging, RAM
priced far below market, and sealed-box listings with stock photos only. Counterfeit and relabelled storage
is common — check the drive's real capacity and speed after install rather than trusting the label.

**Common failure points:** RAM not fully seated (the usual cause of a no-POST), forgetting the CPU power
cable, over-tightened cooler mounts, and a case with insufficient airflow that throttles under load.

## Why This Matters (Industry Application)

Hardware literacy pays off in unexpected places: sizing cloud instances sensibly, diagnosing whether a
problem is code or capacity, and talking credibly with infrastructure teams. It also removes a category of
intimidation — machines stop being magic.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| Compatibility | CPU/socket, RAM type, PSU wattage, and form factor |
| Assembly | Static safety, seating components, and cable management |
| BIOS/UEFI | Boot order, XMP profiles, and firmware settings |
| OS install | Bootable media, partitioning, and drivers |
| Thermals | Airflow, cooling, and why heat throttles performance |
| Troubleshooting | Diagnosing a machine that won't POST |

## How This Connects

Chain K (Hardware & Systems Foundations). Applies **Machine-Under-The-Hood**; the resulting machine hosts **Linux-On-Old-Hardware** experiments.

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
