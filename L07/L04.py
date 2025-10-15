# n    m    k
# 12   15
# 15 % 12 = 3
# 12 %  3 = 0
#  3 %  0 ...

def nsd(n, m):
    if n < m:
        n,m = m, n

    while m > 0:
        k = n % m
        n, m = m, n % m
    return int(n)




######## Main ########

a, b = [float(el) for el in input().split()]
print(nsd(a, b))



