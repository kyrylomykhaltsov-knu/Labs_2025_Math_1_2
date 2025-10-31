# Розбір на прикладі (вхід: 42 24)
# a = 42, b = 24, a >= b → a = 42 % 24 = 18
# a = 18, b = 24, b > a → b = 24 % 18 = 6
# a = 18, b = 6, a >= b → a = 18 % 6 = 0
# Зупинка (бо a == 0). Відповідь — a + b = 0 + 6 = 6.

a, b = map(int, input().split())
while a != 0 and b != 0:
    if a >= b:
        a = a - b     # віднімаємо менше з більшого
    else:
        b = b - a
print(a + b)

def gcd(a, b):
    # База: якщо одне з чисел 0 — інше і є НСД
    if b == 0:
        return a
    # Рекурсивний крок: НСД(a, b) = НСД(b, a mod b)
    return gcd(b, a % b)

a, b = map(int, input().split())
print(gcd(a, b))
