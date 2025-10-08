s = input()

s2 = ""
for el in s:
    if not el.isspace():
        s2 += el
    else:
        if len(s2) > 0 and s2[-1] != " ":
            s2 += " "

if s2[0].isspace():
    s2 = s2[1:]

if s2[-1].isspace():
    s2 = s2[:-1]

# s2 = s2.strip()

print(s2)







# s = input()
# print(' '.join(s.split()))
