# a) повними квадратами;
def is_square(n):
    # n_2 = int(n **  0.5)
    # n_2_square = n_2 ** 2
    # return n_2_square == n
    return int(n ** 0.5) ** 2== n

# b) степенями п’ятірки;
def is_pow5(n):
    while n > 1:
        if n % 5 != 0:
            return False
        n = n // 5
    return True

# c) простими числами.
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


################ Main ################
n = int(input())
numbers = [int(el) for el in input().split()]
primes =[]
pow5s = []
squares =[]
for n in numbers:
    if is_prime(n):
        primes.append(n)
    if is_pow5(n):
        pow5s.append(n)
    if is_square(n):
        squares.append(n)

print("Прості числа: ", primes)
print("Повні квадрати: ", squares)
print("Степені 5: ", pow5s)