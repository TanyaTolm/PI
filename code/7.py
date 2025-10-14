def delete(tupl, elem):
    if elem in tupl:
        my_tuple = list(tupl)
        index = my_tuple.index(elem)
        del my_tuple[index]
        return tuple(my_tuple)
    else: return tuple(tupl)

print(delete((1, 2, 3), 1))
print(delete((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(delete((2, 4, 6, 6, 4, 2), 9))