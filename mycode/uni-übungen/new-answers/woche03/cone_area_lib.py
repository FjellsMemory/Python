"""This script contains the library of cone_area."""

from math import pi, sqrt


def cone_area(radius: float, height: float) -> float:
    """Take height and radius and calculate Mantelfläche."""
    r = radius
    h = height
    s2 = r * r + h * h  # calculating sloping side length of cone via Pythagoras
    s = sqrt(s2)  # square root that side for its real length
    return round(pi * r * s, 2)