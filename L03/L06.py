# n = int(input())
# while n > 0:
#     print(n % 10, end = '')
#     n = n // 10

n = input().strip()       # зчитуємо число як рядок
print(n[::-1])            # виводимо у зворотному порядку
