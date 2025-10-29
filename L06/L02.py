str = input()
counter = 0

for ch in str: # A, E, I, O, U і Y
    if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U" or ch == "Y":
        counter += 1
print(counter)








# for el in str[1:]: # A, E, I, O, U і Y
#     if el == "A" or el == "E" or el == "I" or el == "O" or el == "U" or el == "Y":
#         counter += 1
# print(counter)

#------------------------

#vowels = "AEIOUY"
# for el in str:
#     if el in vowels:
#         counter += 1
# print(counter)