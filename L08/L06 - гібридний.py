t = int(input().strip())
qs = [int(input().strip()) for _ in range(t)]

max_n = 0
for x in qs:
    if x > max_n:
        max_n = x

F = [0] * (max_n + 1)
if max_n >= 1: F[1] = 1
if max_n >= 2: F[2] = 1

SAFE_DEPTH = 900  # умовно безпечна межа для стандартних налаштувань Python

def fib_rec(n):
    if n <= 2:
        return 1
    if F[n] != 0:
        return F[n]
    F[n] = fib_rec(n - 1) + fib_rec(n - 2)
    return F[n]

def fib_hybrid(n):
    # якщо n не надто велике — використовуємо рекурсію
    if n <= SAFE_DEPTH:
        return fib_rec(n)
    # інакше — ітеративно (щоб не впасти по глибині рекурсії)
    a, b = 1, 1  # F(1), F(2)
    i = 3
    while i <= n:
        a, b = b, a + b
        i += 1
    return b if n >= 2 else 1

for n in qs:
    print(fib_hybrid(n))
