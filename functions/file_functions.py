import json

from classes.library import Library
from classes.bookshelf import Bookshelf
from classes.fiction_book import FictionBook
from classes.non_fiction_book import NonFictionBook

def save_and_exit(library):
    json_to_write1 = []
    for bookshelf in library.get_all_bookshelves():
            if bookshelf.get_books():
                bookshelf_json = {
                    "bookshelf_name": bookshelf.get_name()
                }
                for book in bookshelf.get_books():
                    bookshelf_json[f"{book}"] = book
            
            else: 
                bookshelf_json = {
                    "bookshelf_name": bookshelf.get_name()
                }

            json_to_write1.append(bookshelf_json)
    
    with open("data/library.json", "w") as json_file1:
        json.dump(json_to_write1, json_file1, indent=4)

    json_to_write2 = []
    for book in library.get_all_books():
        if book.get_genre():
            books_json = {
            "title_book": book.get_title(),
            "author_book": book.get_author(),
            "rating_book": book.get_rating(),
            "genre": book.get_genre()
        }
        elif book.get_research_topic():
            books_json = {
            "title_book": book.get_title(),
            "author_book": book.get_author(),
            "rating_book": book.get_rating(),
            "research_topic": book.get_research_topic()
        }
        json_to_write2.append(books_json)

    with open("data/books.json", "w") as json_file2:
        json.dump(json_to_write2, json_file2, indent=4)
        
        

def load_from_file(library):
    try:
        with open("data/library.json", "r") as json_file1:
            json_to_load1 = json.load(json_file1)

        for bookshelf in json_to_load1:
            bookshelf = Bookshelf(bookshelf["bookshelf_name"])
            
            library.add_bookshelf(bookshelf)

    except FileNotFoundError:
        print("The file does not exist")

    try:
        with open("data/books.json", "r") as json_file2:
            json_to_load2 = json.load(json_file2)
        
        for book in json_to_load2:
            if book["genre"]:
                book = FictionBook(book["title_book"],book["author_book"], book["rating_book"], book["genre"])
            elif book["research_topic"]:
                book = NonFictionBook(book["title_book"], book["author_book"], book["rating_book"], book["research_topic"])
            library.add_book(book)
    
    except FileNotFoundError:
        print("File does not exist")
