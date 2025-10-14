from collections import Counter

def count_num(ip):
    count = Counter(ip)
    most_count = count.most_common(3)
    for key, value in sorted(most_count, key=lambda x: x[0]):
        print(f'Число {key} встречается {value} раз')

a = '54368729483478'
count_num(a)