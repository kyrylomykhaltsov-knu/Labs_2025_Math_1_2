N = int(input())
a = []

for i in range(N):
    el = int(input())
    a.append(el)

#print(*a[::-1])


for j in range(N // 2):
    # a[i] <-> a[N - 1 - i]
    tmp = a[j]
    a[j] = a[N - 1 - j]
    a[N - 1 - j] = tmp

print(*a)