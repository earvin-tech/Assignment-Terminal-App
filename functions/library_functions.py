from classes.library import Library
from classes.bookshelf import Bookshelf
from classes.non_fiction_book import NonFictionBook
from classes.fiction_book import FictionBook

def add_book(library):
    # Take title of book as input
    book_title = input("Enter title of book: ")
    # Take author as input
    book_author = input("Enter author of book: ")
    # Take rating as input
    book_rating = input("Enter your rating of the book 1-5: ")
    # Check if fiction or non-fiction
    # Create instance of book (Fiction or Non-Fiction)
    fiction_or_non_fiction = ""
    
    while fiction_or_non_fiction != "1" or fiction_or_non_fiction != "2":
        
        fiction_or_non_fiction = input("If fiction enter 1, if non-fiction enter 2: ")
        
        if fiction_or_non_fiction == "1":
            book_genre = input("What is the genre?: ")
            new_book = FictionBook(book_title, book_author, book_rating, book_genre)
            break
        elif fiction_or_non_fiction == "2":
            book_research_topic = input("What is the research topic?: ")
            new_book = NonFictionBook(book_title, book_author, book_rating, book_research_topic)
            break
        else: 
            print("Invalid option, try again")
            
    
    library.add_book(new_book)

    print("Book has been added")

    # if library.bookshelves:
    #     print("Would you like to add this book to a bookshelf?")
    #     adding_to_bookshelf_option = input("Press 1 if yes, or 2 if no: ")

def list_all_books(library):
    all_books = library.list_all_books()
    if not all_books:
        print("No books found")
    for book in all_books:
        print(book)
    print("\n")