import json

from classes.bookshelf import Bookshelf
from classes.fiction_book import FictionBook
from classes.non_fiction_book import NonFictionBook

# def save_and_exit(library):
#     json_to_write1 = []
#     for bookshelf in library.get_all_bookshelves():
#             if bookshelf.get_books():
#                 i = 0
#                 for book in bookshelf.get_book_list():
#                     bookshelf_json = {
#                         "bookshelf_name": bookshelf.get_name(),
#                         f"book{i}": {
#                             f"title{i}": book.get_title(),
#                             f"author{i}": book.get_author(),
#                             f"rating{i}": book.get_rating(),
#                             f"genre{i}": book.get_genre()
#                         }
#                 }
                
#             else: 
#                 bookshelf_json = {
#                     "bookshelf_name": bookshelf.get_name()
#                 }

#             json_to_write1.append(bookshelf_json)
    
#     with open("data/library.json", "w") as json_file1:
#         json.dump(json_to_write1, json_file1, indent=4)

#     json_to_write2 = []
#     for book in library.get_all_books():
#         if book.get_genre():
#             books_json = {
#             "title_book": book.get_title(),
#             "author_book": book.get_author(),
#             "rating_book": book.get_rating(),
#             "genre": book.get_genre()
#         }
#         elif book.get_research_topic():
#             books_json = {
#             "title_book": book.get_title(),
#             "author_book": book.get_author(),
#             "rating_book": book.get_rating(),
#             "research_topic": book.get_research_topic()
#         }
#         json_to_write2.append(books_json)

#     with open("data/books.json", "w") as json_file2:
#         json.dump(json_to_write2, json_file2, indent=4)
#        

def save_and_exit(library):
    bookshelf_data = []

    for bookshelf in library.get_all_bookshelves():
        books = []
        for book in bookshelf.get_book_list():
            books.append({
                "title": book.get_title(),
                "author": book.get_author(),
                "rating": book.get_rating(),
                "genre": getattr(book, "genre", None),
                "research_topic": getattr(book, "research_topic", None)
            })
        
        bookshelf_data.append({
            "bookshelf_name": bookshelf.get_name(),
            "books": books
        })

    
    with open("data/library.json", "w") as f:
        json.dump(bookshelf_data, f, indent=4)

    
    books_data = []

    for book in library.get_all_books():
        if getattr(book, "genre", None):
            books_data.append({
                "title": book.get_title(),
                "author": book.get_author(),
                "rating": book.get_rating(),
                "genre": book.get_genre()
            })
        elif getattr(book, "research_topic", None):
            books_data.append({
                "title": book.get_title(),
                "author": book.get_author(),
                "rating": book.get_rating(),
                "research_topic": book.get_research_topic()
            })
    
    with open("data/books.json", "w") as f:
        json.dump(books_data, f, indent=4)






def load_from_file(library):
    try:
        with open("data/library.json", "r") as json_file1:
            json_to_load1 = json.load(json_file1)

        for shelf_entry in json_to_load1:
            shelf_name = shelf_entry.get("bookshelf_name")
            bookshelf = Bookshelf(shelf_name)

            books = shelf_entry.get("books", [])

            for book_data in books:
                title = book_data.get("title")
                author = book_data.get("author")
                rating = book_data.get("rating")
                genre = book_data.get("genre")
                research_topic = book_data.get("research_topic")

                if genre:
                    book = FictionBook(title, author, rating, genre)
                elif research_topic:
                    book = NonFictionBook(title, author, rating, research_topic)
                else:
                    continue  # Skip if neither genre nor research_topic is provided

                bookshelf.add_book_to_bookshelf(book)

            library.add_bookshelf(bookshelf)

    except FileNotFoundError:
        print("The file does not exist")

    try:
        with open("data/books.json", "r") as json_file2:
            json_to_load2 = json.load(json_file2)

        for book_data in json_to_load2:
            title = book_data.get("title")
            author = book_data.get("author")
            rating = book_data.get("rating")
            genre = book_data.get("genre")
            research_topic = book_data.get("research_topic")

            if genre:
                book = FictionBook(title, author, rating, genre)
            elif research_topic:
                book = NonFictionBook(title, author, rating, research_topic)
            else:
                continue  # Skip if neither genre nor research_topic is provided

            library.add_book(book)

    except FileNotFoundError:
        print("File does not exist")