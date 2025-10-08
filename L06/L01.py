str = input()
counter = 0
for el in str[1:]:
    if el == "+" or el == "-" or el == "*":
        counter += 1
print(counter)