from classes.book import Book

class NonFictionBook(Book):
    def __init__(self, title, author, rating, research_topic):
        super().__init__(title, author, rating)
        self.research_topic = research_topic
        
    def get_research_topic(self):
        return self.research_topic
    
    def __str__(self):
        return f"{self.title} by {self.author} with a rating of {self.rating}/5"