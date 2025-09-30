n = int(input())

a = [0] * 10

while n > 0:
    last = n % 10
    n = n // 10
    a[last] += 1
print(*a)


# n = input().strip()
#
# a = [0] * 10
# for i in n:             # проходимо по всіх цифрах
#     a[ord(i) - 48] += 1
#
# print(*a)
