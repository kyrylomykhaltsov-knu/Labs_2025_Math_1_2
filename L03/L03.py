# n, m = map(float,input("введіть значення x i y: ").split())

n = int(input())
k = 0
#n = 4
# 4! = 1 * 1 * 2 * 3 * 4
# 4! = 3! * 4
# 3! = 2! * 3
# 2! = 1! * 2
# 1! = 0! * 1
# 0! = 1
factorial = 1
while k < n:
    k += 1
    factorial *= k
print(factorial)