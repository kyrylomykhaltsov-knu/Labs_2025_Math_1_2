s = input()

count = 0
words = ""

for ch in s:
    if ch.isalnum() or ch.isspace():
        words += ch
correct_words = words.split()


print(len(correct_words))
