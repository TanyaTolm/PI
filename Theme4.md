# Тема 4. Функции и модули
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
| Задание 6 | + |  | 
| Задание 7 | + |  | 
| Задание 8 | + |  | 
| Задание 9 | + |  | 
| Задание 10 | + |  | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа

### №1
### 

### Ответ:
```python
def main(): print(2+2)

if __name__ == "__main__":
    main()
```
![Меню]()

### Вывод: 


### №2
### 

### Ответ:
```python
def main():
    result = (2+2)
    return result

if __name__ == "__main__":
    answer = main()
    print(answer)
```
![Меню]()

### Вывод: 

### №3
### 

### Ответ:
```python
def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)
```
![Меню]()

### Вывод: 

### №4
### 

### Ответ:
```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))

if __name__ == "__main__":
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")
```
![Меню]()

### Вывод: 

### №5
### 

### Ответ:
```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs: print(f"{key} = {kwargs[key]}")

if __name__ == "__main__":
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()

    main(**{"x": [1, 2, 3], "y": [3, 3, 0]})
```
![Меню]()

### Вывод: 

### №6
### 

### Ответ:
```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data): return sum(data)/float(len(data))

if __name__ == "__main__":
    main(x=[1, 2, 3], y=[3, 3, 0])
```
![Меню]()

### Вывод: 

### №7
### 

### Ответ:
```python
from Fil import say_hello

if __name__ == "__main__":
    say_hello()


def say_hello():
    print("Hello students!")
```
![Меню]()

### Вывод: 

### №8
### 

### Ответ:
```python
from math import *

def main():
    value = int(input("Введите значение: "))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == "__main__": main()
```
![Меню]()

```python
from math import sqrt, sin, cos

def main():
    value = int(input("Введите значение: "))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == "__main__": main()
```
![Меню]()

```python
import math

def main():
    value = int(input("Введите значение: "))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == "__main__": main()
```
![Меню]()

### Вывод: 

### №9
### 

### Ответ:
```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == "__main__": main()
```
![Меню]()

### Вывод: 

### №10
### 

### Ответ:
```python
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
```
![Меню]()

### Вывод: 

## Самостоятельная работа

### №1
### 

### Ответ:
```python
from datetime import datetime # Импортируем модуль для работы с датами и временем
from math import sqrt # Импортируем модуль для вычисления квадратного корня

def main(**kwargs):
    """ Определяем функцию main, принимающую параметры через словарь kwargs
    """
    for key in kwargs.items(): # Перебираем все ключи и значения в kwargs
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # Вычисляем расстояние
        print(result) # Выводим расстояние

if __name__ == '__main__': # Запускаем программу только если она используется как основной скрипт
    start_time = datetime.now() # Начальное время выполнения программы
    main( # Вызываем функцию main с конкретными параметрами
        one=[10, 3], # присваеваем список чисел для one
        two=[5, 4], # присваеваем список чисел для two
        three=[15, 13], # присваеваем список чисел для three
        four=[93, 53], # присваеваем список чисел для four
        five=[133, 15] # присваеваем список чисел для five
    )
    time_costs = datetime.now() - start_time  # Присваиваем переменной время выполнения программы
    print(f"Время выполнения программы - {time_costs}") # Выводим время выполнения программы
```
![Меню]()

### Вывод:

### №2 
### 

### Ответ:
```python
import random

def random_chiclo():
    kost = random.randint(1, 6)

    if kost == 5 or kost == 6: print("Вы победили")
    elif kost == 3 or kost == 4: return random_chiclo()
    else: print("Вы проиграли")

    print(f"Текущее значение кости равно: {kost}")

if __name__ == "__main__": random_chiclo()
```
![Меню]()

### Вывод: 

### №3 
### 

### Ответ:
```python
import datetime
from time import sleep

def main():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    for i in range(5):
        print(current_time)
        sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__': main()
```
![Меню]()

### Вывод: 

### №4
### 

### Ответ:
```python
def sred (args):
    summa = sum(args)
    return summa / len(args)

if __name__ == '__main__':
    args = list(map(float, input('Введите значения: ').split()))
    result = sred(args)
    print(f'Среднее арифметическое: {result}')
```
![Меню]()

### Вывод: 

### №5 
### 

### Ответ:
```python
from Fil import heron

a = float(input("Введите первую сторону треугольника: "))
b = float(input("Введите вторую сторону треугольника: "))
c = float(input("Введите третью сторону треугольника: "))

plo = heron(a, b, c)
if __name__ == '__main__':
    print(f"Площадь треугольника равна {plo}")
```
![Меню]()

```python
from math import sqrt

def heron(a, b, c):
    s = (a + b + c) / 2
    result = sqrt(s * (s - a) * (s - b) * (s - c))
    return result
```
![Меню]()

### Вывод: 

### Общий вывод по теме:
