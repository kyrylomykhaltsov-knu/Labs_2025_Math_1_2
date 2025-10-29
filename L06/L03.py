str = input()
str2 = ""
vowels = "aeiouy"
for ch in str:
    str2 += ch
    if ch in vowels:
        str2 += ch
print(str2)
# for ch in str:
#     str2 += ch
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "y":
#         str2 += ch
# print(str2)













# str2 = ""
# vowels = "aeiouy" # AEIOUY
# for el in str:
#     str2 += el
#     if el in vowels:
#         str2 += el
# print(str2)