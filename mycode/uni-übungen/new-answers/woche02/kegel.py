"""Calculate the surface area of a cone."""
from math import pi, sqrt

radius = float(input("Radius: "))
height = float(input("Höhe: "))

area = (pi * radius) * sqrt(radius ** 2 + height ** 2)
print("Mantelfläche:", round(area, 2))