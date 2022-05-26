"""This script squares a number and then rounds it off 3 different ways."""

from math import floor

usrinp = float(input("Kommazahl: "))
quad = usrinp ** 2
print(f"Quadriert: {quad}")
print(f"Methode 1: {quad//1}")
print(f"Methode 2: {float(int(quad))}")
print(f"Methode 3: {float(floor(quad))}")