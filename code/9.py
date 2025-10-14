def poisk(tupl, elem):
    if elem in tupl:
        my_tuple = list(tupl)
        if tupl.count(elem) == 1:
            index = tupl.index(elem)
            return my_tuple[index:]
        return my_tuple[tupl.index(elem):tupl.index(elem, tupl.index(elem) + 1 +1)]
    else:
        return tuple()

print(poisk((1, 2, 3), 8))
print(poisk((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(poisk((1, 2, 8, 5, 1, 2, 9), 8))