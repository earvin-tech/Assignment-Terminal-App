class Library:
    def __init__(self, name):
        self.name = name
        self.entire_library = []
        self.bookshelves = [] 

    def add_book(self, new_book):
        self.entire_library.append(new_book)

    def get_all_books(self):
        return self.entire_library
    
    def add_bookshelf(self, new_bookshelf):
        self.bookshelves.append(new_bookshelf)

    def get_all_bookshelves(self):
        return self.bookshelves
    
    def find_book(self, book_name):
        for book in self.entire_library:
            if book.title == book_name:
                return book

    def find_bookshelf(self, bookshelf_name):
        for bookshelf in self.bookshelves:
            if bookshelf.bookshelf_name == bookshelf_name:
                return bookshelf
            
    def delete_bookshelf(self, shelf_name):
        new_bookshelves = []
        is_deleted = False
        for shelf in self.bookshelves:
            if shelf.bookshelf_name != shelf_name:
                new_bookshelves.append(shelf)
            else:
                is_deleted = True

        self.bookshelves = new_bookshelves
        return is_deleted