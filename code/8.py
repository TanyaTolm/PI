class Library:
    def __init__(self, name):
        self.name = name

    def autor(self):
        a = input(f"Введите автора {self.name} ")
        print(f"Автором {self.name} является {a}")

class Book(Library):
    def __init__(self, name):
        self.name = name

    def find_book(self):
        b = input("Введите название книги, которую ищите: ")
        if b == self.name: print(f'Данная книга есть в нашей библиотеке')
        else: print("В библиотеке нет нужной вам книги")


l_library = Book("Война и мир")
l_library.autor()
l_library.find_book()