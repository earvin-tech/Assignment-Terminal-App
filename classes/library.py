class Library:
    def __init__(self, name):
        self.name = name
        self.entire_library = []
        self.bookshelves = [] 

    def add_book(self, new_book):
        self.entire_library.append(new_book)