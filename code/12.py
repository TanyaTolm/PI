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