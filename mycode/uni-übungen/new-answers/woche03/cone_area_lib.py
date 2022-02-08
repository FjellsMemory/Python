"""This is the library for a func caluclating the linear area of a cone."""

from math import pi, sqrt


def cone_area(radius: float, height: float):
    """Calculate the linear area of a cone."""
    return round(float((pi * radius) * sqrt(radius ** 2 + height ** 2)), 2)