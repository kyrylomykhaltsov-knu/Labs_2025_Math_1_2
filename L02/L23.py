#x, y = [int(d) for d in input().split()]
x, y = map(float,input("введіть значення x i y: ").split())

# if -1 <= x <= 1 and 0 <= y <= 1 and y <= 1 - abs(x):
#     print("точка належить...")
# else:
#     print("точка не належить...")

# if x ** 2 + y ** 2 <= 4 and x <= 0:
#     print("точка належить...")
# elif x >= 0 and x - 2 <= y <= -x + 2:
#     print("точка належить...")
# else:
#     print("точка не належить...")

# if (abs(x) + abs(y) >= 2) and x ** 2 + y ** 2 <= 4:
#     print("точка належить...")
# else:
#     print("точка не належить...")

if -2 <= x <= 2 and -2 <= y <= 2 and x ** 2 + y ** 2 >= 4 and (x + y) <= 0:
    print("точка належить...")
else:
    print("точка не належить...")