class library:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

l_library = library("Война и мир", "роман")
print(f'Данное произведение называется {l_library.name} и один из его жанров - {l_library.genre}')