global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def tringle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1 - прмояугольник, 2 - треугольник: ")

if figure == "1": rectangle()
elif figure == "2": tringle()

print(f"Площадь: {result}")