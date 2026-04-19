# Electron-Phonon Commutators for Sum Rules

This mini-workflow gives you a starting point to derive sum-rule moments from an electron-phonon Hamiltonian.

## 1) Install dependency

```bash
python -m pip install sympy
```

## 2) Run the example

```bash
python elph_sum_rules.py
```

The script defines:

- `nested_commutator(O, H, order)`: computes repeated commutators with `H`.
- `holstein_site_hamiltonian(...)`: single-site Holstein model building block.

You can swap in your own `H` and operator `O` for specific sum rules (density, current, Green's-function moments, etc.).

## 3) Extend to momentum-space models

For lattice/momentum models, define one operator per mode and build

\[
H = \sum_k \epsilon_k c_k^\dagger c_k + \sum_q \omega_q b_q^\dagger b_q + \sum_{k,q} g_q c_{k+q}^\dagger c_k (b_q + b_{-q}^\dagger).
\]

Then run `nested_commutator(O_k, H, n)` for the moment order you need.

## 4) Start a new repo/branch/project for this work

### New branch in current repo

```bash
git checkout -b feat/elph-sum-rules
```

### New repo from scratch

```bash
mkdir elph-sum-rules && cd elph-sum-rules
git init
git checkout -b main
cp /path/to/elph_sum_rules.py .
cp /path/to/COMMUTATOR_WORKFLOW.md .
git add .
git commit -m "Initial el-ph commutator utilities"
```

### Existing remote repo

```bash
git clone <remote-url>
cd <repo-name>
git checkout -b feat/elph-sum-rules
```

If you want, we can next adapt the script to **your exact Hamiltonian and target sum rule**.
