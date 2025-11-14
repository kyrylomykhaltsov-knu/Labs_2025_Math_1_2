# 1. Зчитуємо розмір матриці A
n_a, m_a = map(int, input().split())

# 2. Зчитуємо матрицю A як список списків
A = []
for _ in range(n_a):
    row = list(map(int, input().split()))
    A.append(row)

# 3. Зчитуємо розмір матриці B
n_b, m_b = map(int, input().split())

# 4. Зчитуємо матрицю B
B = []
for _ in range(n_b):
    row = list(map(int, input().split()))
    B.append(row)

# 5. Перевіряємо, чи можна множити (кількість стовпців A = кількість рядків B)
if m_a != n_b:
    # Розміри неузгоджені, множення неможливе
    print(-1)
else:
    # 6. Розмір матриці C
    n_c = n_a
    m_c = m_b

    # 7. Створюємо матрицю C з нулів (двовимірний масив)
    C = []
    for i in range(n_c):
        row = []
        for j in range(m_c):
            row.append(0)
        C.append(row)

    # 8. Виконуємо множення матриць
    # Для кожного елемента C[i][j] рахуємо суму a[i][k] * b[k][j]
    for i in range(n_c):          # по рядках A (і C)
        for j in range(m_c):      # по стовпцях B (і C)
            s = 0                 # тут накопичуємо суму добутків
            for k in range(m_a):  # або range(n_b), це одне й те саме
                s += A[i][k] * B[k][j]
            C[i][j] = s           # записуємо результат у матрицю C

    # 9. Виводимо результат
    # Спочатку розмір матриці C
    print(n_c, m_c)

    # Потім саму матрицю C по рядках
    for i in range(n_c):
        for j in range(m_c):
            # Виводимо елементи в одному рядку через пробіл
            if j > 0:
                print(' ', end='')
            print(C[i][j], end='')
        print()  # перехід на новий рядок після кожного рядка матриці
