from math import sqrt

def heron(a, b, c):
    s = (a + b + c) / 2
    result = sqrt(s * (s - a) * (s - b) * (s - c))
    return result