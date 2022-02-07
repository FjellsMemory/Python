"""Library of function definition cone_area()."""
from math import pi, sqrt


def cone_area(rad: float, ht: float) -> float:
    """Calculate surface area via radius, height."""
    mf = round(pi * rad * sqrt(ht ** 2 + rad ** 2), 2)
    assert type(mf) == float
    return mf
