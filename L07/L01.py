def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True

######## main ########

n = int(input())
for i in range (n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i +2)