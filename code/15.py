def count_litters(text):
    count = []
    for word in text:
        letters = sum(a.isalpha() for a in word)
        count.append(letters)
    return max(count)

text = open("library.txt", 'r')
print(f"Книга, в названии которой наибольшее количество символов: {count_litters(text)}")
text.close()

text = open("library.txt", 'a')
text.write(input('Напишите навзание книги, которую хотите добавить: '))
print("Новое название добавлено!")
text.close()