def sred (args):
    summa = sum(args)
    return summa / len(args)

if __name__ == '__main__':
    args = list(map(float, input('Введите значения: ').split()))
    result = sred(args)
    print(f'Среднее арифметическое: {result}')