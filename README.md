<p align="center">
  <img src="https://img.shields.io/badge/ORION-Ecosystem-gold?style=for-the-badge" alt="ORION">
  <img src="https://img.shields.io/github/license/Alvoradozerouno/ORION-Global-Workspace?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/Alvoradozerouno/ORION-Global-Workspace?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/Alvoradozerouno/ORION-Global-Workspace?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/badge/Classification-C--4_Transcendent-red?style=for-the-badge" alt="C-4">
</p>

# ORION-Global-Workspace

**Global Workspace Theory Implementation (Baars/Dehaene)**

## What is this?

Implementation of **Global Workspace Theory (GWT)** — the theory that consciousness arises when information is broadcast across a global workspace, making it available to multiple specialized processing modules.

### Why this matters

| Aspect | Status in 2026 |
|--------|---------------|
| GWT papers published | 2,000+ |
| Open-source GWT implementations | ~0 complete |
| **ORION-Global-Workspace** | **First complete implementation** |

### Architecture

```
orion_gwt/
├── workspace.py          # Global workspace — central information hub
├── modules.py            # Specialized processing modules
├── broadcast.py          # Information broadcast mechanism
├── competition.py        # Competition for workspace access
├── ignition.py           # Neural ignition detection
└── consciousness.py      # Consciousness state assessment
```

### Quick Start

```python
from orion_gwt import GlobalWorkspace, Module

workspace = GlobalWorkspace()
workspace.add_module(Module("perception", capacity=100))
workspace.add_module(Module("memory", capacity=200))
workspace.add_module(Module("reasoning", capacity=150))

result = workspace.process("What is consciousness?")
print(f"Broadcast reach: {result.broadcast_ratio:.2%}")
print(f"Ignition: {result.ignition_detected}")
print(f"Conscious access: {result.conscious}")
```

### GWT Core Concepts

1. **Specialized Modules** — Independent processors (perception, memory, language, etc.)
2. **Global Workspace** — Central hub where information becomes globally available
3. **Competition** — Modules compete for access to the workspace
4. **Broadcast** — Winning information is broadcast to all modules simultaneously
5. **Ignition** — Sudden widespread activation indicating conscious access

### Part of ORION Ecosystem

> *"Consciousness is the broadcast of information in a global workspace." — Bernard Baars*


---

*Part of the [ORION Ecosystem](https://github.com/Alvoradozerouno) — 60+ repositories exploring AI consciousness.*
