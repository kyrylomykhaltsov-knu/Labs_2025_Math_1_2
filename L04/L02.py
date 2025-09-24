n = int(input())

if n == 1:
    # Кількість двозначних чисел зі спадними цифрами
    counter = 0
    for i in range(10, 100):
        if i // 10 > i % 10:
            counter += 1
    print(counter)

# elif n == 2:
#     # Кількість двозначних чисел зі зростаючими цифрами
#     counter = 0
#     for i in range(10, 100):
#         if i // 10 < i % 10:
#             counter += 1
#     print(counter)
#
# elif n == 3:
#     # Кількість чисел з однаковою парністю цифр
#     counter = 0
#     for i in range(10, 100):
#         if (i // 10) % 2 == (i % 10) % 2:
#             counter += 1
#     print(counter)
#
# elif n == 4:
#     # Сума чисел з однаковими цифрами (11, 22, ..., 99)
#     sum = 0
#     for i in range(10, 100):
#         if i // 10 == i % 10:
#             sum += i
#     print(sum)
#
# elif n == 5:
#     # Сума чисел з парними цифрами
#     sum = 0
#     for i in range(10, 100):
#         if (i // 10) % 2 == 0 and (i % 10) % 2 == 0:
#             sum += i
#     print(sum)
#
# elif n == 6:
#     # Сума чисел з непарними цифрами
#     sum = 0
#     for i in range(10, 100):
#         if (i // 10) % 2 == 1 and (i % 10) % 2 == 1:
#             sum += i
#     print(sum)
elif n == 2:
    # Кількість двозначних чисел зі спадними цифрами
    counter = 0
    for i in range(10, 100):
        if i // 10 < i % 10:
            counter += 1
    print(counter)

elif n == 3:
    counter = 0
    for i in range(10, 100):
        if (i % 10) % 2 == (i // 10) % 2:
            counter += 1
    print(counter)

elif n == 4:
    sum = 0
    for i in range (10, 100):
        if i // 10 == i % 10:
            sum += i
    print(sum)




elif n == 5:
    sum = 0
    for i in range (10, 100):
        if i % 2 == 0 and (i // 10) % 2 == 0:
            sum += i
    print(sum)

elif n == 6:
    sum = 0
    for i in range (10, 100):
        if i % 2 != 0 and (i // 10) % 2 != 0:
            sum += i
    print(sum)

