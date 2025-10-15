n = int(input())
ans = 0

# допоміжна перевірка простоти (лінійно)
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# перебираємо всі трійки
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            if is_prime(a + b + c):
                ans += 1

print(ans)
