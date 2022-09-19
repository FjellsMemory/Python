"""Script to calculate pi using a single inputed number."""

from math import isclose
from math import sqrt


def calculate_pi(n: int) -> float:
    """Take inputed number, jam it into Euler's formula, return approx pi."""
    pi = 0.0
    if n <= 0:
        return pi
    acc = 0
    for i in range(1, n + 1):
        acc = acc + (1 / i ** 2)
    acc = acc * 6
    pi = sqrt(acc)
    return pi


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(calculate_pi(1), 2.44948, rel_tol=eps)
    assert isclose(calculate_pi(7), 3.01177, rel_tol=eps)
    assert isclose(calculate_pi(1000), 3.14063, rel_tol=eps)
    assert isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
