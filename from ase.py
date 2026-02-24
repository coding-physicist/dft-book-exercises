import os
import numpy as np
from ase.build import molecule
from ase.calculators.nwchem import NWChem
from ase.optimize import BFGS       # ← geometry optimiser

# Setup: space-free working directory
sim_path = os.path.expanduser('~/QE/theory_scan')
relax_dir = os.path.join(sim_path, 'relax_scf_cc_pvdz')
os.makedirs(relax_dir, exist_ok=True)

# Build methane
methane = molecule('CH4')

# Attach calculator
methane.calc = NWChem(
    label  = os.path.join(relax_dir, 'calc'),
    theory = 'scf',
    basis  = 'cc-pvdz',
)

# ── Print initial geometry ────────────────────────────────────
print("=== Before Relaxation ===")
print(f"Energy : {methane.get_potential_energy():.4f} eV")
pos = methane.get_positions()
bonds = [np.linalg.norm(pos[i] - pos[0]) for i in range(1, 5)]
print(f"C–H    : {np.mean(bonds):.4f} Å\n")

# ── Relax the structure ───────────────────────────────────────
optimizer = BFGS(
    methane,
    logfile    = os.path.join(relax_dir, 'opt.log'),
    trajectory = os.path.join(relax_dir, 'opt.traj'),
)

print("=== Running Geometry Relaxation (fmax = 0.05 eV/Å) ===")
optimizer.run(fmax=0.05)   # keeps calling NWChem until forces are small enough

# ── Print relaxed geometry ────────────────────────────────────
print("\n=== After Relaxation ===")
print(f"Energy : {methane.get_potential_energy():.4f} eV")
pos = methane.get_positions()
bonds = [np.linalg.norm(pos[i] - pos[0]) for i in range(1, 5)]
print(f"C–H    : {np.mean(bonds):.4f} Å  (ref 1.087 Å)")
