s = input()

s2 = ""
for i in range(0, len(s)):
    if s[i] != s[i - 1]:
        s2 += s[i]

print(s2)






