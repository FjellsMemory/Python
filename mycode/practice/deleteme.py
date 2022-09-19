"""Another in a long line of deletable scratches - yet they're all cool."""
from numbers import Number
from typing import Sequence


def product(xs: Sequence) -> Number:
    """Eff yer mom."""
    result = 1
    for x in xs:
        result = result * x
    return result


def fact(n: int) -> Number:
    """Get bent."""
    return product(range(1, n + 1))


def Dondlsfact(n: int) -> int:
    """
    Recurse the EFF out of n, mult-ing it by n-1 in recursive calls.
    If something gets in your way... turn = once you hit n-1 = 0, return 1.
    """
    if n == 0:
        return 1
    else:
        return n * Dondlsfact(n - 1)

# RECURRSIVE FUNCTIONS are the silent partners of for loops, or even while loops.
# and they are sexy as fuuuuuuuuck
