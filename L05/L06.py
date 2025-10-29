#n = int(input())

# 0 1 2 3 4 5 6 7 8 9
# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0] * 10

# while n > 0:
#     last = n % 10
#     n = n // 10
#     a[last] += 1
# print(*a)


n = input().strip()   # читаємо як строку
a = [0] * 10
for digit in n:
    a[int(digit)] += 1
print(*a)

