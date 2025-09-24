n = int(input())

counter = 0
if n == 1:
    #Кількість двозначних чисел зі спадними цифрами
    for i in range(10, 100):
        if i // 10 > i % 10:
            counter += 1
print(counter)


