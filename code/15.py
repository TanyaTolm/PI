def change(lst):
    index = 0
    while index < len(lst):
        a = lst.count(lst[index])
        if a > 1:
            lst[index] = str(lst[index]) * a
        index += 1
    return set(lst)
list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(change(list1))
print(change(list2))
print(change(list3))