n = 12345

counter = 1

# while n >= 10:
#     n = n // 10
#     counter += 1
#
# print(counter)

counter = 0 if n > 0 else 1

while n > 0:
    n = n // 10
    counter += 1

print(counter)


