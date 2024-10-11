from classes.book import Book

class FictionBook(Book):
    def __init__(self, title, author, rating, genre):
        super().__init__(title, author, rating)
        self.genre = genre

    def get_genre(self):
        return self.genre

    def __str__(self):
        return f"{self.title} by {self.author} with a rating of {self.rating}/5"