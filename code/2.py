# Класс Car
class Car:
    # Метод инициализации, который вызывается при создании нового экземпляра класса
    def __init__(self, make, model):
        self.make = make# Сохранение марки автомобиля в 'make'
        self.model = model# Сохранение модели автомобиля в 'model'

    # Метод для имитации вождения
    def drive(self):
        print(f"Driving the {self.make} {self.model}")# Вывод сообщения о вождении

# Создание экземпляра класса Car с маркой Toyota и моделью Corolla
my_car = Car("Toyota", "Corolla")# Создание экземпляра класса с маркой Toyota и моделью Corolla
my_car.drive()# Вызов метода drive