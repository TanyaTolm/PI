class Type_Check:
    # Конструктор класса. Устанавливает атрибут func
    def __init__(self, func):
        self.func = func

    # Метод __call__ позволяет объекту класса вести себя как функция.
    def __call__(self, *args, **kwargs):
        all_types = self.func.__annotations__  # annotations - словарь, который содержит аннотации типов для аргументов функции.
        for i, arg in enumerate(args):  # Проходимся по каждому элементу из кортежа
            if i < len(all_types):
                expected_type = list(all_types.values())[i]  # Получаем ожидаемый тип аргумента из словаря
                if expected_type and not isinstance(arg, expected_type):  # Проверяем на соответствие типа
                    print(f"Предупреждение: аргумент {i+1} должен быть типа {expected_type}, но получен тип {type(arg)}")
        return self.func(*args, **kwargs)  # Возвращаем обёрнутую функцию.

# Пример использования
@Type_Check
def greet(name: str, age: int):
    return f"Hello, {name}! You are {age} years old."

@Type_Check
def calculate(a: int, b: int):
    return a + b

print(greet("Alice", 25))
print(greet("Bob", "30"))
print(calculate(3, 4))