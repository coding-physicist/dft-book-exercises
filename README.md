# DFT Book — Exercises

Working through computational chemistry exercises using **NWChem + ASE**.  
Focus: geometry optimization of small molecules, benchmarking methods against experiment.

---

## Task 1 — Finding the right theory + basis-set for CH₄

### Problem

Before running any serious simulation, you need to pick:
- a **level of theory** — how accurately the electron interactions are modelled
- a **basis set** — how the wavefunctions are represented numerically

Wrong choices → slow, inaccurate, or both.  
This notebook scans both independently and picks the best pair.

---

### Molecule

**Methane (CH₄)** — tetrahedral, 1 carbon + 4 hydrogens.  
Experimental C-H bond length: **1.094 Å** ← used as the reference.

---

### What the notebook does

**Step 1 — Theory scan** (basis fixed to cc-pVTZ)

Runs geometry optimization with BFGS for each theory.  
After optimization, computes the mean C-H bond length from atomic positions and compares to experiment.

| Theory | C-H (Å) | Error (%) |
|---|---|---|
| Hartree-Fock | 1.0820 | 1.10 |
| MP2 | 1.0794 | 1.34 |
| **DFT-B3LYP** | **1.0889** | **0.46** |

→ **DFT-B3LYP wins.** HF neglects electron correlation entirely. MP2 adds it perturbatively but still undershoots. B3LYP's hybrid exchange-correlation handles it better for this molecule.

---

**Step 2 — Basis-set scan** (theory fixed to DFT-B3LYP)

Same process, now varying the basis set.

| Basis set | C-H (Å) | Error (%) |
|---|---|---|
| **STO-3G** | **1.0968** | **0.25** |
| cc-pVDZ | 1.0994 | 0.50 |
| cc-pVTZ | 1.0889 | 0.46 |

→ **STO-3G wins.** Surprisingly, the minimal basis set gives the best match here. STO-3G is also the cheapest computationally — ideal for structure optimization.

---

### Bond length calculation

After optimization, atomic positions are read directly:

```python
coords = methane.get_positions()
bonds  = [np.linalg.norm(coords[0] - coords[i]) for i in range(1, 5)]
mean_bond = np.mean(bonds)
```

`coords[0]` is carbon. `coords[1–4]` are the four hydrogens.  
Mean over all 4 C-H distances → single bond length value.

---

### Final verdict

| Parameter | Choice | Error |
|---|---|---|
| Theory | DFT-B3LYP | 0.46% |
| Basis set | STO-3G | 0.25% |

Best pair for methane geometry optimization: **DFT-B3LYP / STO-3G**

---

### How to run

```bash
pip install ase
jupyter notebook "task 1.ipynb"
```

> NWChem must be installed and on your PATH.
