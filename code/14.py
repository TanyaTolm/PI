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

