N = int(input())

a = [int(el) for el in input().split()]

maximum = a[0]
for e in a:
    if maximum < e:
        maximum = e

print(maximum)
