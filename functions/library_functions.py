from classes.library import Library
from classes.bookshelf import Bookshelf
from classes.non_fiction_book import NonFictionBook
from classes.fiction_book import FictionBook

from colored import Fore, Back, Style # type: ignore

def add_book(library):
    # Take title of book as input
    book_title = input("Enter title of book: ")
    # Take author as input
    book_author = input("Enter author of book: ")
    # Take rating as input
    book_rating = "0"
    while int(book_rating) < 1 or int(book_rating) > 5:

        book_rating = input("Enter your rating of the book 1-5: ")
        
        if int(book_rating) < 1 or int(book_rating) > 5:
            print(f"{Back.red}Rating must be between 1-5. Try Again.{Style.reset}\n")
   
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
            print(f"{Back.red}Invalid option, select 1 or 2.{Style.reset}\n")
            
    library.add_book(new_book)

    print("Book has been added\n")

def list_all_books(library):
    # Use library getter method to get list of all books
    all_books = library.get_all_books()
    if not all_books:
        print("No books found")
    for book in all_books:
        print(book)
    print("\n") 

def add_new_bookshelf(library):
    bookshelf_input = input("Enter name of new bookshelf: ")
    # Create instance of bookshelf
    new_bookshelf = Bookshelf(bookshelf_input)
    library.add_bookshelf(new_bookshelf)
    print("Bookshelf added\n")

def list_all_bookshelves(library):
    all_bookshelves = library.get_all_bookshelves()
    if not all_bookshelves:
        print("No bookshelves found")
    for bookshelf in all_bookshelves:
        print(bookshelf)
    print("\n")

def delete_bookshelf(library):
    print("Removing Bookshelf")
    # take input the id of the parking slot
    shelf_name = input("Enter the name of the bookshelf you wish to remove: ")
    # delete the parking slot
    if library.delete_bookshelf(shelf_name):
        print("Bookshelf deleted\n")
    else:
        print("No parking slot with that id.\n")

# To fix below

def list_books_in_bookshelf(library):
    input_bookshelf_to_list = input("Enter bookshelf you wish to list: ")
    bookshelf_to_list = library.find_bookshelf(input_bookshelf_to_list).get_books()
    print(bookshelf_to_list)

def add_book_to_bookshelf(library):
    input_book_to_add_to_shelf = input("Enter the book you would like to add to a bookshelf: ")
    book_to_add = library.find_book(input_book_to_add_to_shelf)
    input_bookshelf_to_add_to = input("Enter the bookshelf you would like to add to: ")
    bookshelf_to_add_to = library.find_bookshelf(input_bookshelf_to_add_to).get_self()
    bookshelf_to_add_to.add_book_to_bookshelf(book_to_add)
    print(f"{book_to_add} has been added to bookshelf {bookshelf_to_add_to}")

# To fix above

def list_same_genre(library):
    genre_to_search = input("Enter genre you wish to search: \n")
    genre_list = []
    for book in library.get_all_books():
        if book.get_genre() == genre_to_search:
            genre_list.append(book.get_title())
        else:
            continue
    print(f"The following are books in the genre {genre_to_search}:\n")
    for item in genre_list:
        print(item)
    print("\n")

def list_by_rating(library):
    rating_list = []
    while len(rating_list) != len(library.get_all_books()):
        for book in library.get_all_books():
            if book.get_rating() == "5":
                rating_list.append(book)
            else:
                continue
        for book in library.get_all_books():
            if book.get_rating() == "4":
                rating_list.append(book)
            else:
                continue
        for book in library.get_all_books():
            if book.get_rating() == "3":
                rating_list.append(book)
            else:
                continue
        for book in library.get_all_books():
            if book.get_rating() == "2":
                rating_list.append(book)
            else:
                continue
        for book in library.get_all_books():
            if book.get_rating() == "1":
                rating_list.append(book)
            else:
                continue
    print("Listing in order of highest rating:\n")
    for book in rating_list:
        print(book.get_title())
    print("\n")
        
    