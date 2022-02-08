"""Script to round the squared result of the input down to one tenth."""

from math import floor

num = float(input("Kommazahl: "))
quad = num ** 2
print("Quadriert:", quad)
print(f"Methode 1: {quad // 1}")
print(f"Methode 1: {float(floor(quad))}")
print(f"Methode 1: {float(int(quad))}")