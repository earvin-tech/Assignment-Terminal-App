class Bookshelf:
    def __init__(self, bookshelf_name):
        self.bookshelf_name = bookshelf_name
        self.books = []

    def get_name(self):
        return self.bookshelf_name

    def add_book_to_bookshelf(self, new_book):
        self.books.append(new_book)

    def get_books(self):
        if self.books:
            return self.books
        else:
            return f"No books found"

    def __str__(self):
        if self.books:
            return f"Bookshelf: {self.bookshelf_name}."
        else:
            return f"Bookshelf: {self.bookshelf_name}" 