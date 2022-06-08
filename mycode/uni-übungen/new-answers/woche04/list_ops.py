"""This is the script list_ops for week 4."""

from math import isclose
from platform import release


def average(mylist: list) -> float:
    """Return average value of a list of numbers."""
    num_items = len(mylist)
    total = 0
    for x in mylist:
        total = total + x
    aver = total / num_items  # watch division by zero
    return aver


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(average([]), 0.0, rel_tol=eps)  # dividing by zero