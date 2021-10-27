"""Takes a number, squares it, rounds it down 3 times, 3 ways."""

from math import floor

usrinpt = float(input("Kommazahl: "))
usrinpt_sq = usrinpt ** 2
print("Quadriert:", usrinpt_sq)
print("Methode 1:", float(floor(usrinpt_sq)))
print("Methode 2:", float(int(usrinpt_sq)))
print("Methode 3:", usrinpt_sq // 1)
