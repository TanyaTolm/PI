def count(file):
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()

    count_lines = text.count('\n') + 1
    count_words = len(text.split())
    count_letters = sum(a.isalpha() for a in text)

    print(f'Input file contains: \n {count_letters} letters'
          f'\n {count_words} words \n {count_lines} lines')

count("input.txt")

