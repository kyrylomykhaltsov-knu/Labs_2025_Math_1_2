a, b = map(int, input().split())

# решето простих до b
n = b
is_prime = [False, False] + [True] * (n - 1)  # 0 і 1 не прості
p = 2
while p * p <= n:
    if is_prime[p]:
        q = p * p
        while q <= n:
            is_prime[q] = False
            q += p
    p += 1

# рахуємо "улюблені" (без підрядка "13")
cnt = 0
for x in range(max(2, a), b + 1):
    if is_prime[x] and '13' not in str(x):
        cnt += 1

print(cnt)
