class Bookshelf:
    def __init__(self, bookshelf_name):
        self.bookshelf_name = bookshelf_name
        self.books = []

    def get_name(self):
        return self.bookshelf_name

    def add_book_to_bookshelf(self, new_book):
        self.books.append(new_book)

    def get_book_list(self):
        if self.books:
            return self.books
        else:
            return None

    def get_books(self):
        return self.books if self.books else None

    def __str__(self):
        return f"Bookshelf: {self.bookshelf_name}"