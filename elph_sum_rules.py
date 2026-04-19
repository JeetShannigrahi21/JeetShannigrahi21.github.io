"""Symbolic commutator utilities for electron-phonon (el-ph) sum-rule calculations.

This module uses SymPy's quantum operators to build Hamiltonians and compute
nested commutators that appear in moment/sum-rule derivations, e.g.

    mu_n = < [[...[O, H], H], ..., H] O^† >

It is intentionally lightweight so you can adapt it to your own basis/operators.
"""

from __future__ import annotations

import sympy as sp
from sympy.physics.quantum import BosonOp, Dagger, FermionOp, Commutator


def simplify_comm(expr: sp.Expr) -> sp.Expr:
    """Expand and simplify an operator expression containing commutators."""
    return sp.expand(expr.doit())


def nested_commutator(op: sp.Expr, hamiltonian: sp.Expr, order: int) -> sp.Expr:
    """Compute ad_H^order(op) = [ ... [[op, H], H], ..., H ]."""
    if order < 0:
        raise ValueError("order must be non-negative")

    result = op
    for _ in range(order):
        result = simplify_comm(Commutator(result, hamiltonian))
    return result


def holstein_site_hamiltonian(
    epsilon: sp.Symbol,
    omega: sp.Symbol,
    g: sp.Symbol,
    n: sp.Expr,
    b: BosonOp,
) -> sp.Expr:
    """Single-site Holstein-like Hamiltonian.

    H = epsilon * n + omega * b† b + g * n (b + b†)
    """
    return epsilon * n + omega * Dagger(b) * b + g * n * (b + Dagger(b))


def main() -> None:
    # Parameters
    epsilon, omega, g = sp.symbols("epsilon omega g", real=True)

    # Operators (single site labels)
    c = FermionOp("c")
    b = BosonOp("b")

    # Number operator for fermion
    n = Dagger(c) * c

    # Example Hamiltonian and probe operator
    H = holstein_site_hamiltonian(epsilon, omega, g, n, b)
    O = c

    # First and second moments often involve first/second nested commutators
    C1 = nested_commutator(O, H, order=1)
    C2 = nested_commutator(O, H, order=2)

    print("H =", H)
    print("[O, H] =", C1)
    print("[[O, H], H] =", C2)

    # You can define a symbolic moment object:
    mu2 = Dagger(O) * C2
    print("Dagger(O) * [[O, H], H] =", sp.expand(mu2))


if __name__ == "__main__":
    main()
