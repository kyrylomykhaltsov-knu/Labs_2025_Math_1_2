n = int(input())
elems = [int(e) for e in input().split()]

#elems.remove(3)

elem_set = set()
for el in elems:
    # elems.remove(el) # Never do this way
    # elem_set.add(el)
    if el in elem_set:
        continue
    if elems.count(el) == 1:
        print(el, end=" ")
    else:
        elem_set.add(el)