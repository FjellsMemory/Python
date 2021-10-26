from math import log2
resa = int(log2(64)) + 2 ** abs(1+1j)
print(f"res(a) ist {type(resa)}")

from math import sqrt, floor, ceil
resb = floor(2.3 * 7) * ceil(2 ** 3 + 7.1)
print(f"res(b) ist {type(resb)}")

from math import pi, sin, cos, radians
resc = cos(pi/4)**2 + sin(radians(45))**2j
print(f"res(c) ist {type(resc)}")

resd = 6 * round(2.1, 1) // 1
print(f"res(d) ist {type(resd)}")

res = input("do it: ")
print(type(res))