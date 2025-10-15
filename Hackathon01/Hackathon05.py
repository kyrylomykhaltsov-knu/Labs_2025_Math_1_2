x1, x2, x3 = map(int, input().split())
S = x1 + x2 + x3
T = S // 2                      # цільова сума для кожного

# 1) можна без різання?
if (x1 == T or x2 == T or x3 == T or
    x1 + x2 == T or x1 + x3 == T or x2 + x3 == T):
    print(0)
else:
    done = False

    # 2) пробуємо різати 1-й злиток
    for Sfix in (0, x2, x3, x2 + x3):
        p = T - Sfix
        if 1 <= p <= x1 - 1:
            print(1)
            print(p, x1 - p)
            done = True
            break

    # 3) якщо не вийшло — ріжемо 2-й
    if not done:
        for Sfix in (0, x1, x3, x1 + x3):
            p = T - Sfix
            if 1 <= p <= x2 - 1:
                print(2)
                print(p, x2 - p)
                done = True
                break

    # 4) якщо не вийшло — ріжемо 3-й
    if not done:
        for Sfix in (0, x1, x2, x1 + x2):
            p = T - Sfix
            if 1 <= p <= x3 - 1:
                print(3)
                print(p, x3 - p)
                done = True
                break

    # 5) жодного варіанту
    if not done:
        print(-1)
