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
    
    while fiction_or_non_fiction not in ["1", "2"]:
        
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
    print("Listing all bookshelves: ")
    all_bookshelves = library.get_all_bookshelves()
    if not all_bookshelves:
        print("No bookshelves found\n")
    for bookshelf in all_bookshelves:
        print(bookshelf)
    print("\n")

def delete_bookshelf(library):
    # take input the name of the bookshelf
    shelf_name = input("Enter the name of the bookshelf you wish to remove: ")
    # delete the bookshelf
    if library.delete_bookshelf(shelf_name):
        print("Bookshelf deleted\n")
    else:
        print("No bookshelf with that name.\n")

def list_books_in_bookshelf(library):
    shelf_name = input("Enter bookshelf you wish to list: ")
    bookshelf = library.find_bookshelf(shelf_name)


    if not bookshelf:
        print("Bookshelf not found.\n")
        return
    

    books = bookshelf.get_book_list()


    if not books:
        print(f"No books in '{shelf_name}' shelf.\n")
    else:
        print(f"\n Books in '{shelf_name}':")
        for book in books:
            print(f"- {book.get_title()} by {book.get_author()} ({book.get_rating()}/5)")
        print()


    # input_bookshelf_to_list = input("Enter bookshelf you wish to list: ")
    # bookshelf_to_list = library.find_bookshelf(input_bookshelf_to_list)
    # print(bookshelf_to_list.get_books())

def add_book_to_bookshelf(library):
    shelf_name = input("Enter bookshelf to add to: ")
    bookshelf = library.find_bookshelf(shelf_name)

    if not bookshelf:
        print("Bookshelf not found.\n")
        return

    # Collect book details
    book_title = input("Enter title of book: ")
    book_author = input("Enter author of book: ")
    book_rating = input("Enter your rating of the book 1-5: ")

    # Validate rating
    while not book_rating.isdigit() or int(book_rating) < 1 or int(book_rating) > 5:
        print("Rating must be between 1-5. Try Again.\n")
        book_rating = input("Enter your rating of the book 1-5: ")

    # Determine book type
    fiction_or_non_fiction = input("If fiction enter 1, if non-fiction enter 2: ")

    if fiction_or_non_fiction == "1":
        book_genre = input("What is the genre?: ")
        new_book = FictionBook(book_title, book_author, int(book_rating), book_genre)
    elif fiction_or_non_fiction == "2":
        book_research_topic = input("What is the research topic?: ")
        new_book = NonFictionBook(book_title, book_author, int(book_rating), book_research_topic)
    else:
        print("Invalid option, select 1 or 2.\n")
        return

    # Add book to bookshelf
    bookshelf.add_new_book_to_bookshelf(new_book)

    # Also add book to the entire library
    library.add_book(new_book)

    print("Book has been added to the bookshelf and the entire library.\n")



    # input_book_to_add_to_shelf = input("Enter the book you would like to add to a bookshelf: ")
    # book_to_add = library.find_book(input_book_to_add_to_shelf)
    # input_bookshelf_to_add_to = input("Enter the bookshelf you would like to add to: ")
    # bookshelf_to_add_to = library.find_bookshelf(input_bookshelf_to_add_to)
    # bookshelf_to_add_to.add_book_to_bookshelf(book_to_add)
    # print(f"{book_to_add.get_title()} has been added to {bookshelf_to_add_to}")

def list_same_genre(library):
    genre_input = input("Enter genre to search for: ").strip().lower()
    books = library.get_all_books()
    if not books:
        print("No books in the library.\n")
        return

    # Filter fiction books that match the specified genre
    matching_books = [
        book for book in books
        if isinstance(book, FictionBook) and book.get_genre().lower() == genre_input
    ]

    if not matching_books:
        print(f"No books found in genre '{genre_input}'.\n")
    else:
        print(f"\nBooks in genre '{genre_input}':")
        for book in matching_books:
            print(f"- {book.get_title()} by {book.get_author()} ({book.get_rating()}/5)")
        print()


def list_by_rating(library):
    books = library.get_all_books()
    if not books:
        print("No books in the library.\n")
        return

    # Sort books by rating in descending order
    sorted_books = sorted(books, key=lambda b: b.get_rating(), reverse=True)

    print("\nBooks sorted by rating:")
    for book in sorted_books:
        print(f"- {book.get_title()} by {book.get_author()} ({book.get_rating()}/5)")
    print()
