"""A mishmash of the universe, right here."""
from dataclasses import dataclass


"""
list = [2, 3, 4, 5]
newlist = list[:]
list.reverse()
print(list)
print(newlist)
print("tadaaaaa!!!")
list.remove(3)
print(list)


var = "homeboi is a {}"
print(var.format("king"))
"""
'''
def strictly_positive(x):
    """Bitch, i'm a bus, comparing x to zero."""
    if x > 0 and x < 100:
        print(inp, "is strictly positive AND less than 100")


if __name__ == "__main__":
    inp = input("enter a number:  ")
    strictly_positive(float(inp))
'''


def check_for_3(tup: tuple) -> tuple:
    """Take tuple and return tuple only with mod 3 values."""
    tup_of_3s = []
    for n in tup:
        if n % 3 == 0:
            tup_of_3s = tup_of_3s + [n]
    return tuple(tup_of_3s)


def poly_add(p: list, q: list) -> list:
    """Eff yo mama."""
    maxlen = max(len(p), len(q))
    result = []
    for i in range(maxlen):
        result = result + [safe_index(p, i, 0) + safe_index(q, i, 0)]
    return result


def safe_index(p: list, i: int, d: int) -> int:
    """Eff yo mama."""
    return p[i] if i < len(p) else d


assert (poly_add([], []) == [])
assert (poly_add([42], []) == [42])
assert (poly_add([], [11]) == [11])
assert (poly_add([1, 2, 3], [4, 3, 2, 5]) == [5, 5, 5, 5])

@dataclass
class Article:
    """Class should represent a supermarket article with name and price."""

    name: str
    price: float
