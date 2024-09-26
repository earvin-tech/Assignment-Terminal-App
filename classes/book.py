class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __str__(self):
        return f"This book is {self.title} by {self.author}, with a rating of {self.rating}"