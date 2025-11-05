s = input()
char_set = set(s)
# print(char_set)
freq = {c: s.count(c) for c in char_set}
# print(freq)

max_char = max(freq)
print(max_char, freq[max_char])