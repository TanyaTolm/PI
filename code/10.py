class InvalidInputError(Exception):
    # Исключение, которое возникает при некорректных входных данных.
    pass
# Функция check_age принимает число age, где проверяет корректность введеного возраста
def check_age(age):
    if age < 0:
        raise InvalidInputError("Возраст не может быть отрицательным") # Реализуется исключение, если возраст не подходит по данным параметрам
    elif age > 150:
        raise InvalidInputError("Возраст не может быть больше 150")
    return f"Ваш возраст: {age}" # Если входные данные корректны, функция возвращает строку с подтверждением возраста.
# Функция check_password принимает строку password.
# Проверяется длина пароля: если строка короче 8 символов — вызывается исключение с сообщением.
def check_password(password):
    if len(password) < 8:
        raise InvalidInputError("Пароль должен быть не менее 8 символов")
    return "Пароль принят" # Если условие выполнено, возвращается сообщение об успешном приеме пароля.

# Ввод данных и обработка исключений
try:
    age = int(input("Введите ваш возраст: ")) # Преобразование в целое число, если строка является не целым числом, то используется5 ValueError
    print(check_age(age))
except InvalidInputError as e:
    print(f"Ошибка: {e}")
except ValueError:
    print("Ошибка: Введите корректное число")

try:
    password = input("Введите пароль: ")
    print(check_password(password))
except InvalidInputError as e:
    print(f"Ошибка: {e}")