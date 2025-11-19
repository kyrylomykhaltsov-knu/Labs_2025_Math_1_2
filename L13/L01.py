# def print_all_lines(lines):
#     for line in lines:
#         print(len(line))
#     print()

# file = open(r"file01.txt", "rt", encoding="utf-8")

def print_all_lines(file):
    with open(file, "rt", encoding="utf-8") as f:
        for line in f:
            print(len(line.rstrip("\n")))

def print_60plus_lines(file):
    with open(file, "rt", encoding="utf-8") as f:
        for line in f:
            if len(line.rstrip("\n")) > 60:
                print(line)

def print_empty_lines(file):
    with open(file, "rt", encoding="utf-8") as f:
        counter = 0
        for line in f:
            line = line.strip()
            if len(line) <= 0:
                counter += 1
        print(counter)


def print_longest_lines(file):
    with open(file, "rt", encoding="utf-8") as f:
        longest = 0
        for line in f:
            line = line.strip()
            if len(line) > longest:
                longest = len(line)
        print(longest)

# print_all_lines("file01.txt")
print_60plus_lines("file01.txt")
# print_empty_lines("file01.txt")
# print_longest_lines("file01.txt")