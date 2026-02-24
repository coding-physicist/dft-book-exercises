# DFT Book — Exercises

Working through computational chemistry exercises using **NWChem + ASE**.

---

## Task 1 — Theory and Basis-Set Scan for Methane

Goal: find the right theory + basis-set pair for geometry optimization of CH₄.

**What's done:**
- Scanned 3 levels of theory: Hartree-Fock, MP2, DFT-B3LYP
- Scanned 3 basis-sets: STO-3G, cc-pVDZ, cc-pVTZ
- Compared optimized C-H bond length against experimental value (1.094 Å)

**Result:**

| Step | Best choice | Error |
|------|-------------|-------|
| Theory | DFT-B3LYP | 0.46% |
| Basis set | STO-3G | 0.25% |

---

## Stack

- Python + ASE (Atomic Simulation Environment)
- NWChem (quantum chemistry engine)
- BFGS geometry optimizer

---

## How to run

```bash
# install dependencies
pip install ase

# open the notebook
jupyter notebook "task 1.ipynb"
```

> NWChem must be installed and accessible on your PATH.
