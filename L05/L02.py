N = int(input())
a = [int(el) for el in input().split()]

for i in range(N):
    if a[i] >= 0:
        print(a[i] + 2, end = " ")
    else:
        print(a[i], end=" ")


















# for e in a:
#     if e >= 0:
#         print(e + 2, end = " ")
#     else:
#         print(e, end = " ")


# for i in range(N):
#     if a[i] >= 0:
#         a[i] += 2
#     else:
#         a[i] = a[i]
#
# print(*a)
