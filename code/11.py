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