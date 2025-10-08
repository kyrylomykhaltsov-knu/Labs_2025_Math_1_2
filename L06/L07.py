text = ""
while True:
    try:
        text += input() + " "
    except EOFError:
        break

words = text.split()
for w in words:
    print(len(w), end=' ')
