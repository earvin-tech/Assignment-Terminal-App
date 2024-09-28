class Bookshelf:
    def __init__(self, bookshelf_name):
        self.bookshelf_name = bookshelf_name
        self.books = []

    def add_book_to_bookshelf(self, new_book):
        self.books.append(new_book)

    def get_books(self):
        return self.books

    def __str__(self):
        if self.books:
            return f"Bookshelf: {self.bookshelf_name}."
        else:
            return f"Bookshelf: {self.bookshelf_name}" 