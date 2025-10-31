class Car:  # Класс 'Car'
    def __init__(self, make, model):  # Конструктор класса, вызывается при создании экземпляра
        self._make = make  # Присваивание значения аргумента 'make' переменной экземпляра '_make'
        self.__model = model  # Присваивание значения аргумента 'model' переменной экземпляра '__model'
    def drive(self):  # Метод класса, который выводит сообщение о вождении
        print(f"Driving the {self._make} {self.__model}")  # Вывод строки с маркой и моделью автомобиля

# Создание экземпляра класса 'Car' с параметрами
my_car = Car("Toyota", "Corolla")
print(my_car._make)# Доступ к переменной '_make' через экземпляр 'my_car'
my_car.drive()# Вызов метода 'drive'