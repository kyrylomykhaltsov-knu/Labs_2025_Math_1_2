N = int(input())
a = [float(el) for el in input().split()]
sum = 0
counter = 0

# for i in range(N):
#     if (i + 1) % 3 == 0 and a[i] > 0:
#         counter += 1
#         sum += a[i]
# print(counter, "%0.2f" % sum, sep = " ")

for i in range(2, N, 3):
    if a[i] > 0:
        counter += 1
        sum += a[i]

print(counter, "%0.2f" % sum, sep = " ")
