# Определение класса геометрических фигур
class Shape:
    # Абстрактный метод для вычисления площади фигуры
    def area(self):
        pass

# Класс прямоугольника, наследующий от класса Shape
class Rectangle(Shape):
    # Конструктор класса, принимающий ширину и высоту прямоугольника
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Метод для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height# Возвращает произведение ширины и высоты

# Класс круга, также наследующий от класса Shape
class Circle(Shape):
    # Конструктор класса, принимающий радиус круга
    def __init__(self, radius):
        self.radius = radius
    # Метод для вычисления площади круга
    def area(self):
        return 3.14 * self.radius ** 2# Возвращает площадь круга по формуле π * r^2

shapes = [Rectangle(4, 5), Circle(5)]# Создание списка объектов фигур
for shape in shapes:# Проход по всем фигурам в списке и вывод их площадей
    print(f"Площадь: {shape.area()}")# Вывод строки с площадью