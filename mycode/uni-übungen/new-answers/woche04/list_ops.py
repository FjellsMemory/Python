"""This is the script list_ops for week 4."""

from math import isclose
from platform import release


def average(mylist: list) -> float:
    """Return average value of a list of numbers."""
    num_items = len(mylist)
    if num_items == 0:
        return 0.0
    total = 0
    for x in mylist:
        total = total + x
    aver = total / num_items  # watch division by zero
    return aver


def reverse(mylist: list) -> list:
    """Reverse the items in a list."""
    newlist = []
    x = len(mylist) - 1
    while x >= 0:  # this while loops makes new list beginning at last index
        newlist = newlist + [mylist[x]]  # of initial list
        x -= 1
    return newlist


def only_positive(mylist: list) -> list:
    """Return the items in a list which are positive in new list."""
    newlist = []
    x = len(mylist)
    y = 0  # y is index 0, x is where to stop
    while y < x:
        if mylist[y] > 0:
            newlist = newlist + [mylist[y]]  # double square brackets!!
        y += 1
    return newlist


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(average([]), 0.0, rel_tol=eps)  # dividing by zero
    assert isclose(average([1.0]), 1.0, rel_tol=eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)

    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]