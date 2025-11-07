# Тема 9. Концепции и принципы ООП
Отчёт по теме выполнила:
  - Толмачева Татьяна Сергеевна
  - ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + | 
| Задание 3 | + | + | 
| Задание 4 | + | + |
| Задание 5 | + | + | 
| Задание 6 |  |  | 
| Задание 7 |  |  | 
| Задание 8 |  |  | 
| Задание 9 |  |  | 
| Задание 10 |  |  | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа

### №1
Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию init (), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

### Ответ:
```python
class Tanya:
    __slots__ = ['name']

    def __init__(self, name):
        if name == "Таня":
            self.name = f'Да, я {name}'
        else: self.name = f'Я не {name}, а Таня'

person1 = Tanya('Таня')
person2 = Tanya('Марина')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/1.png)
### Вывод: В этом коде создается класс Name с использованием механизма slots. В конструкторе класса происходит проверка имени: если оно равно "Таня", то атрибуту name присваивается строка "Да, я Таня"; иначе — "Нет, я не {имя}, я Таня".

### №2
Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

### Ответ:
```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else: self.ingredient = None

    def composion(self):
        if self.ingredient:
            print(f'Мороженое с {self.ingredient}')
        else: print('Обычное мороженое')

icecream = Icecream()
icecream.composion()
icecream = Icecream("шоколадом")
icecream.composion()
icecream = Icecream(5)
icecream.composion()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/2.png)

### Вывод: Класс IceCream представляет собой модель мороженого, которая может содержать ингредиент или быть обычной. Метод composition() выводит информацию о составе мороженого. 

### №3
Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают.

### Ответ:
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self): return self._value

    def del_value(self): del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/3.png)

### Вывод: В этом коде создается класс MyClass, который имеет приватный атрибут _value для хранения значения. Методы get_value(), set_value() и del_value() используются для получения, установки и удаления этого атрибута соответственно. Эти методы связаны со свойством value через декоратор property.

### №4
Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

### Ответ:
```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    specias = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    specias = 'feline'
    sounds = 'meow'

dog = Dog()
print(f'Dog is {dog.className}, but they say {dog.sounds}')
cat = Cat()
print(f'Cat is {cat.className}, but they say {cat.sounds}')
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/4.png)

### Вывод: В этом коде демонстрируется использование наследования в Python. Класс Mammal является базовым классом для классов Dog и Cat. Оба подкласса наследуют атрибут className, а также определяют свои собственные атрибуты, характеризующие поведение соответствующих животных. В конце кода создаются экземпляры классов Dog и Cat.

### №5
На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self. 

### Ответ:
```python
class Russian:
    @staticmethod
    def greeting(): print("Привет")

class English:
        @staticmethod
        def greeting(): print('Hello')

def greet(lenguage):
    lenguage.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/5.png)

### Вывод: 
В данном коде реализованы два класса Russian и English, каждый из которых содержит статический метод greeting(). Метод greet() принимает объект одного из этих классов и вызывает у него метод greeting(), который выводит соответствующее приветствие на нужном языке.

## Самостоятельная работа

Код представляет собой простую модель выращивания томатов, которая включает три класса: Tomato, TomatoBush и Gardener. Каждый класс отвечает за свою часть процесса:
- Класс Tomato: Представляет отдельный помидор, который может находиться в одном из четырех состояний ('Отсутствует', 'Цветение', 'Зеленый', 'Красный'), где последнее означает созревание. Помидоры могут переходить между состояниями с помощью метода grow.
- Класс TomatoBush: Моделирует куст томатов. Он содержит список объектов Tomato и методы для управления ими: перевод всех томатов на следующий этап роста (grow_all), проверка, все ли помидоры созрели (all_are_ripe) и удаление всех томатов с куста после сбора урожая (give_away_all).
- Класс Gardener: Отвечает за уход за кустом томатов. Включает методы для перевода всех томатов куста на следующий уровень созревания (work) и сбора урожая, если все они созрели (harvest). Также есть статический метод knowledge_base, который выводит информацию о процессе ухода за кустами.
### №1
Вызовите справку по сводоводству 

### Ответ:
```python
class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._states = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self): self._states += 1

    # Проверяет созрел ли томат
    def is_ripe(self): return self._states == 3 #

    class TomatoBush:
        def __init__(self, tomato_count):
            self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

        """
        Инициализация объекта TomatoBush.
        tomato_count (int): Количество томатов на кусте.
        tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
        """

        # Переводит все томаты на кусте на слудющую стадию
        def grow_all(self):
            for tomato in self.tomatoes: tomato.grow()

        # Проверяет все ли томаты на кусте созрели
        def all_are_ripe(self):
            return all(tomato.is_ripe() for tomato in self.tomatoes)

        # Собирает урожай с куста
        def give_away_all(self):
            self.tomatoes = []

    class Gardener:
        def __init__(self, name, plant):
            self.name = name
            self._plant = plant

        """
        Инициализация объекта Gardener.
        name (str): Имя садовника.
        plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
        """

        # Садовник работает, переводя томаты на следующую стадию созревания
        def work(self):
            self._plant.grow_all()

        # Проверяет созрели ли все томаты на кусте и собирает, если пора
        def harvaest(self):
            if self._plant.all_are_ripe():
               self._plant.give_away_all()
               print("Урожай собран")
            else: print("Томаты ещё не созрели")

        # Справка о порядке действий по уходу за томатами
        @staticmethod
        def knowledge_base():
            print("Справка по садоводству: \n" 
                  "1. Посадить куст томатов\n"
                  "2. Назначить садовника на куст\n"
                  "3. Ухаживать за кустом\n"
                  "4. Собрать урожай")

    Gardener.knowledge_base()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/6.png)

### Вывод: В этом коде реализована модель выращивания томатов с помощью классов Tomato, TomatoBush и Gardener. Класс Tomato описывает отдельные плоды, их состояния и методы роста. Класс TomatoBush представляет куст томатов, содержащий несколько плодов, и включает методы для управления ими. Класс Gardener моделирует садовника, который ухаживает за кустом и собирает урожай.

### №2 
Создайте объекты классов TomatoBush и Gardener.

### Ответ:
```python
class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self):
        self._state += 1

    # Проверяет созрел ли томат
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

    """
    Инициализация объекта TomatoBush.
    tomato_count (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    # Переводит все томаты на кусте на слудющую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяет все ли томаты на кусте созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Собирает урожай с куста
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
            self.name = name
            self._plant = plant

    """
    Инициализация объекта Gardener.
    name (str): Имя садовника.
    plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
    """

    # Садовник работает, переводя томаты на следующую стадию созревания
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    # Проверяет созрели ли все томаты на кусте и собирает, если пора
    def harvaest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else: print("Томаты ещё не созрели")

    # Справка о порядке действий по уходу за томатами
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: \n" 
                "1. Посадить куст томатов\n"
                "2. Назначить садовника на куст\n"
                "3. Ухаживать за кустом\n"
                "4. Собрать урожай")

a = TomatoBush(5)
b = Gardener("Tanya", a)
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/7.png)

### Вывод: В этом коде реализована модель выращивания томатов с помощью классов Tomato, TomatoBush и Gardener. Класс Tomato описывает отдельные плоды, их состояния и методы роста. Класс TomatoBush представляет куст томатов, содержащий несколько плодов, и включает методы для управления ими. Класс Gardener моделирует садовника, который ухаживает за кустом и собирает урожай.

### №3 
Используя объект класса Gardener, поухаживайте за кустом с помидорами

### Ответ:
```python
class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self):
        self._state += 1

    # Проверяет созрел ли томат
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

    """
    Инициализация объекта TomatoBush.
    tomato_count (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    # Переводит все томаты на кусте на слудющую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяет все ли томаты на кусте созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Собирает урожай с куста
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
            self.name = name
            self._plant = plant

    """
    Инициализация объекта Gardener.
    name (str): Имя садовника.
    plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
    """

    # Садовник работает, переводя томаты на следующую стадию созревания
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    # Проверяет созрели ли все томаты на кусте и собирает, если пора
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else:
            print("Томаты ещё не созрели")

    # Справка о порядке действий по уходу за томатами
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: \n" 
                "1. Посадить куст томатов\n"
                "2. Назначить садовника на куст\n"
                "3. Ухаживать за кустом\n"
                "4. Собрать урожай")

a = TomatoBush(6)
b = Gardener("Tanya", a)
b.work()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/8.png)
### Вывод: В этом коде реализована модель выращивания томатов с помощью классов Tomato, TomatoBush и Gardener. Класс Tomato описывает отдельные плоды, их состояния и методы роста. Класс TomatoBush представляет куст томатов, содержащий несколько плодов, и включает методы для управления ими. Класс Gardener моделирует садовника, который ухаживает за кустом и собирает урожай.

### №4
Попробуйте собрать урожаев, когда томаты еще не дозрели. Продолжайте ухаживать за ними

### Ответ:
```python
class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self):
        self._state += 1

    # Проверяет созрел ли томат
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

    """
    Инициализация объекта TomatoBush.
    tomato_count (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    # Переводит все томаты на кусте на слудющую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяет все ли томаты на кусте созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Собирает урожай с куста
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
            self.name = name
            self._plant = plant

    """
    Инициализация объекта Gardener.
    name (str): Имя садовника.
    plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
    """

    # Садовник работает, переводя томаты на следующую стадию созревания
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    # Проверяет созрели ли все томаты на кусте и собирает, если пора
    def harvaest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else: print("Томаты ещё не созрели")

    # Справка о порядке действий по уходу за томатами
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: \n" 
                "1. Посадить куст томатов\n"
                "2. Назначить садовника на куст\n"
                "3. Ухаживать за кустом\n"
                "4. Собрать урожай")

a = TomatoBush(5)
b = Gardener("Tanya", a)
b.work()
b.harvaest()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/9.png)

### Вывод: В этом коде реализована модель выращивания томатов с помощью классов Tomato, TomatoBush и Gardener. Класс Tomato описывает отдельные плоды, их состояния и методы роста. Класс TomatoBush представляет куст томатов, содержащий несколько плодов, и включает методы для управления ими. Класс Gardener моделирует садовника, который ухаживает за кустом и собирает урожай.

### №5 
Соберите урожай.

### Ответ:
```python
class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self):
        self._state += 1

    # Проверяет созрел ли томат
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

    """
    Инициализация объекта TomatoBush.
    tomato_count (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    # Переводит все томаты на кусте на слудющую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяет все ли томаты на кусте созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Собирает урожай с куста
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
            self.name = name
            self._plant = plant

    """
    Инициализация объекта Gardener.
    name (str): Имя садовника.
    plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
    """

    # Садовник работает, переводя томаты на следующую стадию созревания
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    # Проверяет созрели ли все томаты на кусте и собирает, если пора
    def harvaest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else: print("Томаты ещё не созрели")

    # Справка о порядке действий по уходу за томатами
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: \n" 
                "1. Посадить куст томатов\n"
                "2. Назначить садовника на куст\n"
                "3. Ухаживать за кустом\n"
                "4. Собрать урожай")

a = TomatoBush(5)
b = Gardener("Tanya", a)
b.work()
b.work()
b.work()
b.harvaest()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme9/pic/10.png)

### Вывод: В этом коде реализована модель выращивания томатов с помощью классов Tomato, TomatoBush и Gardener. Класс Tomato описывает отдельные плоды, их состояния и методы роста. Класс TomatoBush представляет куст томатов, содержащий несколько плодов, и включает методы для управления ими. Класс Gardener моделирует садовника, который ухаживает за кустом и собирает урожай.

### Общий вывод по теме:
Тема 9 посвящена основам объектно-ориентированного программирования на Python. Рассматриваются такие важные концепции, как классы, методы, экземпляры классов, инкапсуляция, наследование, ассоциация и полиморфизм. Подробно описываются способы создания классов, работа с атрибутами и методами, динамические изменения экземпляров, а также применение статических и классовых методов. 
