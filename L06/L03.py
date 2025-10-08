str = input()
str2 = ""
vowels = "aeiouy" # AEIOUY
for el in str:
    str2 += el
    if el in vowels:
        str2 += el
print(str2)