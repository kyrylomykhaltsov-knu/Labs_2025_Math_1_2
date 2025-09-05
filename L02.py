# Складіть програму взаємного обміну значень цілих змінних x та y.
import math
x1, y1, x2, y2, x3, y3 =  [float(d) for d in input().split()]

AB = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
BC = ((x2-x3) ** 2 + (y2-y3) ** 2) ** 0.5
AC = ((x3-x1) ** 2 + (y3-y1) ** 2) ** 0.5

P = (AB + BC + AC)
p = P / 2

s = (p * (p - AB) * (p - BC) * (p - AC)) ** 0.5



print("%0.4f" % P, "%0.4f" % s)
