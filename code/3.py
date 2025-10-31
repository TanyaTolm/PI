# Класс Car, который представляет автомобиль
class Car:
    # Метод инициализации экземпляра класса Car
    def __init__(self, make, model):
        self.make = make# Сохранение марки автомобиля в 'make'
        self.model = model# Сохранение модели автомобиля в 'model'
    def drive(self):# Метод для управления автомобилем
        print(f"Driving the {self.make} {self.model}")# Вывод сообщения о вождении

# Класс ElectricCar, наследующий от класса Car
class ElectricCar(Car):
    # Метод инициализации экземпляра класса ElectricCar
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)# Вызов метода инициализации родительского класса Car
        self.battery_capacity = battery_capacity# Сохранение емкости батареи в 'battery_capacity'
    # Метод зарядки электромобиля
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")# Вывод сообщения о зарядке

# Создание экземпляра класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 100)
my_electric_car.drive()# Вызов метода вождения
my_electric_car.charge()# Вызов метода зарядки