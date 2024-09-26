class Bookshelf:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        if self.books:
            return f"This is bookshelf: {self.name} which contains {self.books}."
        else:
            return f"This is bookshelf: {self.name} which contains no books."