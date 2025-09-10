# Складіть програму взаємного обміну значень цілих змінних x та y.

x = int(input())
y = int(input())
# y = 32

tmp = x
x = y
y = tmp

print(x, y)