# Підрахунок "дзеркально простих" на відрізку [a, b]

def sieve(limit):
    is_prime = [False, False] + [True] * (limit - 1)  # 0 і 1 — не прості
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            q = p * p
            while q <= limit:
                is_prime[q] = False
                q += p
        p += 1
    return is_prime

def reverse_num(x):
    # дзеркальне число без рядків
    r = 0
    while x > 0:
        r = r * 10 + (x % 10)
        x //= 10
    return r

def count_mirror_primes(a, b):
    LIMIT = 10000  # за умовою b ≤ 10000; дзеркало теж ≤ 10000
    is_prime = sieve(LIMIT)
    cnt = 0
    n = a
    while n <= b:
        if is_prime[n]:
            rn = reverse_num(n)
            if is_prime[rn]:
                cnt += 1
        n += 1
    return cnt

a, b = map(int, input().split())
print(count_mirror_primes(a, b))
