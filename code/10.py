def minmax(tuple):
    if tuple == ():
        return tuple
    minn = min(tuple)
    maxx = max(tuple)
    return (minn, maxx)

print(minmax((1, 2, 3, 4, 5, 55, -1, 0)))
print(minmax(()))