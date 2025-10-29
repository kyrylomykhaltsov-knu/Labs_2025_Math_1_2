str = input()
counter = 0
for ch in str[1:]:
    if ch == "+" or ch == "-" or ch == "*":
        counter += 1

print(counter)



#
#
# for el in str[1:]:
#     if el == "+" or el == "-" or el == "*":
#         counter += 1
# print(counter)