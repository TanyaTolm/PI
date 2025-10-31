class Library:
    def dep(self): pass
    def get_name(self): pass

class Book(Library):
    def __init__(self, name): self.name = name
    def get_name(self): return self.name
    def dep(self): print("B_010")

class Music(Library):
    def __init__(self, name): self.name = name
    def get_name(self): return self.name
    def dep(self): print("Mus_022")

class Movie(Library):
    def __init__(self, name): self.name = name
    def get_name(self): return self.name
    def dep(self): print("Mov_213")

a = [Book('Война и мир'), Music('3 сентября'), Movie('Титаник')]

for items in a:
    print(f'Название произведения: {items.get_name()}')
    items.dep()