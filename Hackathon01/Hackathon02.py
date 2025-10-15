# Компакт-диски

n = int(input())
min_cost = 10**9   # дуже велике число

for x in range(n // 100 + 2):
    for y in range(n // 20 + 2):
        z = max(0, n - (100 * x + 20 * y))
        cost = 100 * x + 30 * y + 2 * z
        if cost < min_cost:
            min_cost = cost

print(min_cost)
