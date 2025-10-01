N = int(input())
a = [int(el)
 for el in input().split()]

maximum = a[0]

for i in a:
    maximum = max(maximum, i)

print(maximum)
























# N = int(input())
#
# a = [int(el) for el in input().split()]
#
# maximum = a[0]
# for e in a:
#     if maximum < e:
#         maximum = e
#
# print(maximum)
