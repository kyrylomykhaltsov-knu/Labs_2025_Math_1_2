a, b, c = [int(d) for d in input().split()]

# condition_1 = a ** 2 + b ** 2 == c ** 2
# condition_2 = a ** 2 + c ** 2 == b ** 2
# condition_3 = c ** 2 + b ** 2 == a ** 2

cond = a ** 2 + b ** 2 + c ** 2 == 2 * max(a, b, c) ** 2

if cond:
    print("YES")
else:
    print("NO")