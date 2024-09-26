class Library:
    def __init__(self, name):
        self.name = name
        self.entire_library = []
        self.bookshelves = [] 

    def add_book(self, new_book):
        self.entire_library.append(new_book)

    def list_all_books(self):
        return self.entire_library
    
    def add_bookshelf(self, new_bookshelf):
        self.bookshelves.append(new_bookshelf)

    def list_bookshelves(self):
        return self.bookshelves