# Рекурсивне обчислення Фібоначчі з мемоізацією.
# F(1) = F(2) = 1, F(n) = F(n-1) + F(n-2)

t = int(input().strip())
qs = [int(input().strip()) for _ in range(t)]

max_n = 0
for x in qs:
    if x > max_n:
        max_n = x

# Масив для запам'ятовування результатів: F[i] = i-те число Фібоначчі
# 0 означає "ще не обчислювали"
F = [0] * (max_n + 1)

def fib(n):
    # База
    if n <= 2:
        return 1
    # Якщо вже рахували — віддаємо з пам'яті
    if F[n] != 0:
        return F[n]
    # Інакше рахуємо рекурсивно, зберігаємо і повертаємо
    F[n] = fib(n - 1) + fib(n - 2)
    return F[n]

for n in qs:
    print(fib(n))
