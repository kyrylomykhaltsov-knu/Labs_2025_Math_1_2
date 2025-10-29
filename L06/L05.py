str = input()

prev = None
result = ''
for w in str:
  if w != prev:
    result += w
    prev = w
print(result)







# s2 = ""
# for i in range(0, len(s)):
#     if s[i] != s[i - 1]:
#         s2 += s[i]
#
# print(s2)
#
#
#
#
#
#
