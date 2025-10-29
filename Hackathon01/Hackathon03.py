n = int(input())

# 1) будуємо масив простих до 3n (решето)
limit = 3 * n
is_prime = [True] * (limit + 1)
is_prime[0] = False
is_prime[1] = False

p = 2
while p * p <= limit:
    if is_prime[p]:
        q = p * p
        while q <= limit:
            is_prime[q] = False
            q += p
    p += 1

# 2) рахуємо кількість трійок
m = n - 1               # бо працюємо з x=a-1, y=b-1, z=c-1 у межах [0..m]
ans = 0
s = 3
while s <= 3 * n:
    if is_prime[s]:
        k = s - 3       # x + y + z = k, 0<=x,y,z<=m

        # C2(t) = t*(t-1)//2 для t>=2, інакше 0
        if k <= m:
            t = k + 2
            cnt = 0 if t < 2 else t * (t - 1) // 2
        elif k <= 2 * m:
            t1 = k + 2
            c1 = 0 if t1 < 2 else t1 * (t1 - 1) // 2
            t2 = k - m + 1
            c2 = 0 if t2 < 2 else t2 * (t2 - 1) // 2
            cnt = c1 - 3 * c2
        else:  # 2m < k <= 3m
            t = 3 * m - k + 2
            cnt = 0 if t < 2 else t * (t - 1) // 2

        ans += cnt
    s += 1

print(ans)
