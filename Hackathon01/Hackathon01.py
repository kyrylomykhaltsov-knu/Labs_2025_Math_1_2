#Олімпіада

# зчитуємо час початку
h1, m1, s1 = map(int, input().split())
# зчитуємо час закінчення
h2, m2, s2 = map(int, input().split())

# переводимо обидва моменти часу у секунди від початку доби
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

# різниця в секундах
diff = t2 - t1

# переводимо назад у год, хв, сек
hours = diff // 3600
diff %= 3600
minutes = diff // 60
seconds = diff % 60

print(hours, minutes, seconds)
