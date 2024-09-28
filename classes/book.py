class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_rating(self):
        return self.rating

    def __str__(self):
        return f"{self.title} by {self.author} with rating of {self.rating}/5"