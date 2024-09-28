from colored import Fore, Back, Style # type: ignore

from classes.library import Library
from functions.library_functions import add_book, list_all_books, add_new_bookshelf, list_all_bookshelves, delete_bookshelf
from functions.file_functions import save_and_exit, load_from_file
# open app
print(f"{Fore.yellow}{Back.red}\nWelcome to the Personal Library App\n{Style.reset}")
# open menu
def open_menu():
    print("Enter 1 to add a new book")
    print("Enter 2 to list all books in the library")
    print("Enter 3 to add a new bookshelf")
    print("Enter 4 to add existing book to an existing bookshelf")
    print("Enter 5 to remove a bookshelf")
    print("Enter 6 to list all bookshelves")
    print("Enter 7 to list books in a bookshelf")
    print("Enter 8 to list books of a genre")
    print("Enter 9 to list books by rating")
    print("Enter 0 to exit\n")

    choice = input("Enter your choice: ")
    return choice

choice = ""

library = Library("library_main")

load_from_file(library)

while choice != "9":
    choice = open_menu()
    # Add book
    if choice == "1":
        add_book(library)
        pass
    # List all books in library
    elif choice == "2":
        list_all_books(library)
    # Add bookshelf
    elif choice == "3":
        add_new_bookshelf(library)
    # Add existing book to existing bookshelf
    elif choice == "4":
        pass
    # Remove bookshelf
    elif choice == "5":
        delete_bookshelf(library)
    # List all bookshelves
    elif choice == "6":
        list_all_bookshelves(library)
    # List books in a bookshelf 
    elif choice == "7":
        pass
    # List books by genre/research topic
    elif choice == "8":
        pass
    # List books by highest rating
    elif choice == "9":
        pass
    # Exit
    elif choice == "0":
        save_and_exit(library)
        break
    else: 
        print("Invalid, enter choice between 0-9\n")
