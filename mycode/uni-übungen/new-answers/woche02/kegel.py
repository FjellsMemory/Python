"""This script outputs the upper surface area of a cone."""

from math import pi, sqrt
r = float(input("Radius: "))
h = float(input("Höhe: "))
s2 = r * r + h * h  # calculating sloping side length of cone via Pythagoras
s = sqrt(s2)  # square root that side for its real length
print(f"Mantelfläche: {round(pi * r * s, 2)}")