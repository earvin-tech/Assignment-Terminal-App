from book import Book

class FictionBook(Book):
    def __init__(self, title, author, genre, rating):
        super().__init__(title, author, rating)
        self.genre = genre

    def __str__(self):
        return super().__str__()