# 📖 Lesson Plan — Build-A-PC

> **Chain K — Hardware & Systems Foundations** | Assemble a desktop PC from parts: compatibility, assembly, BIOS/UEFI, and OS install.

## What This Project Is

Select compatible parts, assemble a working desktop, configure firmware, and install an operating system — turning the computer into an object you understand.

## Learning Objectives

By the end I can:

1. Verify CPU/socket, RAM, PSU, and form-factor compatibility before buying.
2. Assemble safely, managing static and cable routing.
3. Navigate BIOS/UEFI: boot order, XMP, and firmware settings.
4. Install an OS from bootable media and partition sensibly.
5. Explain airflow and why thermals throttle performance.
6. Diagnose a machine that will not POST.

## Software You Will Use

- PCPartPicker for compatibility checking.
- A bootable USB (Ventoy or Rufus).
- An anti-static strap and basic tools.

## Build Order

1. Choose parts and verify every compatibility constraint.
2. Test-boot outside the case before final assembly.
3. Assemble and route cables.
   - 🎥 [How to build a PC, the last guide you'll ever need! (Linus Tech Tips)](https://www.youtube.com/watch?v=BL4DCEp7blY) — watch the physical seating/cabling steps before doing them on real hardware.
4. Enter UEFI; set boot order and enable XMP.
5. Install the OS and drivers.
6. Stress-test and monitor temperatures.

## Common Mistakes to Avoid

- RAM not fully seated — the most common no-POST cause.
- Forgetting the CPU power connector.
- Over-tightening the cooler or applying far too much thermal paste.
- Buying a PSU on price alone.
- Ignoring case airflow and then wondering about throttling.

## Check Your Understanding

The quiz covers compatibility checks, POST troubleshooting order, XMP, and thermal behaviour.

## Why This Matters (Industry Application)

Hardware literacy pays off in unexpected places: sizing cloud instances sensibly, diagnosing whether a
problem is code or capacity, and talking credibly with infrastructure teams. It also removes a category of
intimidation — machines stop being magic.

## Reflection Questions

- Which part would you spend more on next time, and what evidence changed your mind?
- How does building this change how you read cloud instance specifications?
