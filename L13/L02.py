def sumElements(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        print(elements)
        return sum(elements)

def countNegElements(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        print(elements)
        counter = 0
        for el in elements:
            if el < 0:
                counter += 1
        return counter


def lastElement(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        return elements[-1]


def minEvenElement(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        minElement = 0
        for el in elements[2::2]:
            if el < minElement:
                minElement = el
        return minElement

def sum_MinMaxEvenElement(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        minElement = 0
        maxElement = 0
        for el in elements:
            if el < minElement:
                minElement = el
        for el in elements:
            if el > maxElement:
                maxElement = el
        return minElement+maxElement

def FirstLast_diff(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        return elements[0]-elements[-1]

def countLessAverage(file):
    with open(file) as f:
        elements = [float(el) for el in f.read().split()]
        average = sum(elements) / len(elements)
        print(average)
        counter = 0
        for el in elements:
            if el < average:
                counter += 1
        return counter

# print(sumElements("numbers.txt"))
# print(countNegElements("numbers.txt"))
# print(lastElement("numbers.txt"))
# print(minEvenElement("numbers.txt"))
# print(sum_MinMaxEvenElement("numbers.txt"))
# print(FirstLast_diff("numbers.txt"))
print(countLessAverage("numbers.txt"))