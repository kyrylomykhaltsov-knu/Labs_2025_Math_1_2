a, b, c = [float(a) for a in input(). split()]

try:
    assert a + b > c and a + c > b and b + c > a, "Такого трикутника не існує"
    assert a + b > c and a + c > b and b + c > a, "Такого трикутника не існує"
    assert a + b > c and a + c > b and b + c > a, "Такого трикутника не існує"
    assert a + b > c and a + c > b and b + c > a, "Такого трикутника не існує"

# print(a, b, c)
# 3 4 5  // 3 4 55
    p = (a + b + c) / 2.0
    s = p * (p - a) * (p - b) * (p - c)
    s = s ** 0.5
    print(f"Площа трикутника зі сторонами {a}, {b}, {c} = {s}")

except AssertionError as as_err:
    print(as_err)


# if a + b > c and a + c > b and b + c > a:
#     p = (a + b + c) / 2.0
#     s = p * (p - a) * (p - b) * (p - c)
#     s = s ** 0.5
#     print(f"Площа трикутника зі сторонами {a}, {b}, {c} = {s}")
# else:
#     print("Такого трикутника не існує")