class Library:
    def __init__(self, name, genre):
        self._name = name
        self.__genre = genre

    def autor(self):
        a = input(f"Введите автора {self._name} ")
        print(f"Автором {self._name} в жанре {self.__genre} является {a}")


l_library = Library("Война и мир", "роман")
print(l_library._name)
l_library.autor()