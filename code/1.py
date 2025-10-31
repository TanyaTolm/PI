class Car:  # Класс 'Car'
    def __init__(self, make, model):  # Метод экземпляра класса
        self.make = make  # Присваивание значения 'make' атрибуту 'make' объекта
        self.model = model  # Присваивание значения 'model' атрибуту 'model' объекта

# Создание экземпляра класса 'Car' с параметрами 'Toyota' и 'Corolla'
my_car = Car("Toyota", "Corolla")
print(f"Бренд: {my_car.make}, Модель: {my_car.model}") # Вывод информации об автомобиле