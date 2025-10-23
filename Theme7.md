# Тема 7. Работа с файлами (ввод, вывод)
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
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Ответ:
Текст внутри файла:
```
Тhe best and most beautiful things in the world can't be seen or even touched. They must be felt with the heart.
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/1.png)

### №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

### Ответ:
```python
f = open("text.txt", 'r')
print(f.readline())
f.close()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/2.png)

### Вывод:
Данный код открывает файл text.txt для чтения, с помощью метода readline() читает первую строку, затем закрывает файл с помощью метода close().

### №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open(/)/close().

### Ответ:
```python
f = open("text.txt", 'r')
print(f.readlines())
f.close()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/3.png)

### Вывод:
Этот код открывает файл text.txt для чтения, читает все строки этого файла, затем закрывает файл с помощью метода close().

### №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

### Ответ:
```python
with open ('text.txt') as f:
    print(f.readlines())
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/4.png)

### Вывод: 
Этот код открывает файл text.txt для чтения и затем выводит все строки этого файла.

### №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

### Ответ:
```python
with open ('text.txt') as f:
    for line in f:
        print(line)
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/5.png)

### Вывод: 
Данный код открывает файл text.txt для чтения и обрабатывает каждую строку этого файла. С помощью функции print() выводится каждая строка.

### №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

### Ответ:
```python
with open ('text.txt', 'a+') as f:
    f.write('\n Hello world')

with open ('text.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/6.png)

### Вывод: 
Этот код выполняет две операции с файлом text.txt. Во-первых, он открывает файл для записи, добавляет строку в конец файла и закрывает его. Затем он снова открывает файл для чтения и выводит все на экран.

### №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например, направит любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

### Ответ:
```python
lines = ['one', 'two', 'three']

with open ('text.txt', 'w') as f:
    for line in lines:
        f.write('\n Cycle run ' + line)
    print('Done!')
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/7.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/7.1.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/7.2.png)

### Вывод: 
Этот код записывает строки ['one', 'two', 'three'] в файл text.txt. После завершения всей работы выводится сообщение Done!.

### №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

### Ответ:
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join ([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs(r'C:\xampp\htdocs\myphp')
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/8.png)

### Вывод: 
Функция print_docs принимает путь к директории и с помощью импорта os получает информацию обо всех файлах и поддиректориях в данной директории. Она печатает название папки, список директорий внутри нее и список файлов.

### №9
### Документ «input.txt» содержит следующий текст:
```
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
```
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

### Ответ:
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_lenght = len(max(words, key=len))
        for word in words:
            if len(word) == max_lenght:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('text.txt'))
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/9.png)

### Вывод:
Функция longest_words принимает файл и возвращает самое длинное слово в нем. Она открывает файл, читает его содержимое, разбивает строку на слова и определяет максимальную длину слова. Затем она проходит по всем словам и выбирает те, которые имеют такую же длину, как и самое длинное слово.

### №10
### Требуется создать сsv-файл «rows_300.csv» со следующими столбцами: . № – номер по порядку (от 1 до 300); . Секунда – текущая секунда на вашем ПК; . Микросекунда – текущая миллисекунда на часах. Для наглядности на каждой интерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

### Ответ:
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/10.1.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/10.png)

### Вывод: 
Данный код  создает файл rows_300.csv с 300 строками данных, каждая из которых содержит номер строки, секунды и микросекунды текущего времени. Используются модули csv, datetime и time. Выполняется цикл, который записывает данные для каждой строки, включая текущие значения секунд и микросекунд. После завершения цикла происходит пауза в 0.01 секунды перед завершением программы.

## Самостоятельная работа

### №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

### Ответ:
```python
def words(file):
    words = []
    summ = []
    count = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower().split()
            lenn = len(line)
            words.append((line, lenn))

            for word in line:
                if word in count: count[word] += 1
                else: count[word] = 1

        for i, v in words:  summ.append(v)

        print(f'Всего слов в статье: {sum(summ)}')

    word_max = max(count, key=count.get)
    max_count = max(count.values())
    print(f'Cамое часто повторяющееся слово в тексте: {word_max}\nОно повторяется: {max_count} раз')

words('text.txt')
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/11.1.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/11.2.png)

### Вывод: 
Функция number_of_words принимает файл file в качестве аргумента и открывает его, после чего проходится по каждой строке, преобразует её и разбивает на отдельные слова. После выполнений всех действий выводит количество слов в статье и печатает информацию о самом частом слове и количестве его повторений.

### №2 
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.


### Ответ:
```python
def add_res():
    reson = input("Причина расходов: ")
    summ = input("Сумма: ")
    with open('text.txt', 'a', encoding='utf-8') as file:
        file.write(f'{reson}: {summ}\n')
def show_ras():
    print("Расходы:")
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
while True:
    action = input("Введите 'добавить' для добавления расхода или 'показать' для показа всех расходов: ").strip()
    if action.lower() == 'добавить':
        add_res()
    elif action.lower() == 'показать':
        show_ras()
    else:
        print("Неверный ввод. Попробуйте снова.")
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/12.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/12.1.png)

### Вывод: 
Данныйф код позволяет пользователю добавлять и просматривать записи о расходах. Функция add_res принимает назначение расходов и сумму через стандартный ввод и записывает их в файл text.txt. Функция show_ras считывает содержимое этого файла и выводит его на экран. 

### №3 
### Имеются файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

- Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
- Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines

### Ответ:
```python
def count(file):
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()

    count_lines = text.count('\n') + 1
    count_words = len(text.split())
    count_letters = sum(a.isalpha() for a in text)

    print(f'Input file contains: \n {count_letters} letters'
          f'\n {count_words} words \n {count_lines} lines')

count("input.txt")
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/13.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/13.1.png)

### Вывод: 
Функция count принимает на вход имя файла и возвращает количество букв, слов и строк в этом файле. 

### №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звёздочками (* количество звёздочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встретились, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит следующее слово exam, то слова экзамен, Exam, ExaM, EXAM и exAm должны быть замены на ****.

- Запрещенные слова: hello email python the exam wor is
- Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is... PYTHON is awesome!!!
- Ожидаемый результат: **** the ** *****, ***ld! ****** ** *** programming language of *** future. My ***** **... ****** ** awesome!!!

### Ответ:
```python
import re
def replace_world(banned, sen):
    for word in banned:
        sen = re.sub(word, '*' * len(word), sen, flags=re.IGNORECASE)
    return sen

with open('input.txt', 'r', encoding='utf-8') as f:
    ban = f.read().strip().split()

sen = input("Введите предложение для проверки: ")
result = replace_world(ban, sen)
print(f'Проверенное предложение: {result}')
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/14.png)

### Вывод: 
Функция replace_world принимает два аргумента: строку и список запрещенных слов. Используя регулярное выражение для поиска каждого слова из списка ban в строке, заменяет каждое найденное слово символами '*', и возвращает измененную строку. 
### №5 
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Задача: 
Необходимо в текстовом файле "библиотека" со списком книг посчитать количество символов с самым длинным названием и вывести это число, а также добавить в этот файл новую книгу.

### Ответ:
```python
def count_litters(text):
    count = []
    for word in text:
        letters = sum(a.isalpha() for a in word)
        count.append(letters)
    return max(count)

text = open("library.txt", 'r')
print(f"Количество символов, в названии книги с самым длинным названием из файла: {count_litters(text)}")
text.close()

text = open("library.txt", 'a')
text.write(input('Напишите навзание книги, которую хотите добавить: '))
print("Новое название добавлено!")
text.close()
```
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/15.png)
![Меню](https://github.com/TanyaTolm/PI/blob/Theme7/pic/15.1.png)

### Вывод:
Этот код принимает название книги и добавлет его в список, находящийся в library.txt. Помимо этого также выводится количество символом в книге с самым длинным названием. Поиск и подсчет происходит с помощью функции count_litters.

### Общий вывод по теме:
### Основные операции с файлами:
- Открытие файла (функция open())
- Чтение из файла (методы read(), readline(), readlines())
- Запись в файл (метод write())
- Закрытие файла (метод close())
### Режимы доступа к файлу:
"r" - чтение
"w" - запись
"a" - добавление
"b" - бинарный режим
"t" - текстовый режим
"+" - чтение/запись
### Методы работы с содержимым:
readline() - чтение одной строки
readlines() - чтение всех строк в список
write() - запись данных
seek(), tell() - управление указателем чтения/записи
flush() - принудительная запись буфера
