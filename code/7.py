class library:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def autor(self):
        a = input(f"Введите автора {self.name} ")
        print(f"Автором {self.name} является {a}")


l_library = library("Война и мир", "роман")
l_library.autor()