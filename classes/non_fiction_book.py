from book import Book

class NonFictionBook(Book):
    def __init__(self, title, author, genre, rating, research_topic):
        super().__init__(title, author, genre, rating)
        self.research_topic = research_topic
        
        
    
    def __str__(self):
        return super().__str__()