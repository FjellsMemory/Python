"""
from math import log2
resa = int(log2(64)) + 2 ** abs(1+1j)
print(f"check me out!: {(abs(1+1j))}")
print(f"res(a) ist {type(resa)}")

from math import sqrt, floor, ceil
resb = floor(2.3 * 7) * ceil(2 ** 3 + 7.1)
print(f"check me out!: {floor(2.3 * 7), ceil(2 ** 3 + 7.1)}")
print(f"res(b) ist {type(resb)}")

from math import pi, sin, cos, radians
resc = cos(pi/4)**2 + sin(radians(45))**2j
print(f"check me out!: {cos(pi/4)**2, sin(radians(45))**2j}")
print(f"res(c) ist {type(resc)}")

resd = 6 * round(2.1, 1) // 1
print(f"check me out!: {6 * round(2.1, 1) // 1}")
print(f"res(d) ist {type(resd)}")
"""

usrinp = input("Type anything: ")
try:
    float(usrinp)
except:
    print("You didn't type a number... bitch.")