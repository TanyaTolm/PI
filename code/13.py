import math

def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area)

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [2, 21, 37, 56, 84]

def find_maxmin(lst):
    return max(lst), min(lst)

maxone, minone = find_maxmin(one)
maxtwo, mintwo = find_maxmin(two)
maxthree, minthree = find_maxmin(three)

s1 = heron_area(maxone, maxtwo, maxthree)
s2 = heron_area(minone, mintwo, minthree)

print("Площадь первого треугольника:", s1)
print("Площадь второго треугольника:", s2)