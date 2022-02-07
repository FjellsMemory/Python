"""Just another in a long line of deletable scratches - yet they're all cool."""
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
    """Recurse the EFF out of n, mult-ing it by n-1 in recursive calls.

    Go deeper and deeper... once you hit n-1 = 0, start returning with 1.

    """
    if n == 1:
        return 1
    else:
        return n * Dondlsfact(n - 1)


def mySum(
    n: int,  # stop index
    k: int   # start index
) -> int:
    """Sum up a series through recursion.

    Writing this function was FUN and educational.  The big lesson here was to
    write a recursive function BACKWARDS.  Have it's first calculation be the
    LAST term you need, and then send it backwards down the line to your first
    term.
    """
    if n == k:  # hitting the base case
        return n  # the base case, clearly defined
    else:
        return n * mySum(n - 1, k)  # all other cases, via base case


mySum(5, 3)


def mySum2(
    n: int,  # stop index
    k: int   # start index
) -> int:
    """Sum up a series through list comprehension.

    Also fun to rewrite the same function using list comprehension!!!  Learning
    a lot as I go, here.  :D
    """
    calclist = [x for x in range(k, n + 1)]
    myacc = 1  # if you're multiplying, gotta have this at 1, adding?  0
    for x in calclist:
        myacc *= x
    print(calclist)
    return myacc
