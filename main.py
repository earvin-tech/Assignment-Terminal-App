from classes.library import Library
# open app
print("Welcome to the Personal Library App\n")
# open menu
def open_menu():
    print("Enter 1 to add a new book")
    print("Enter 2 to find a book")
    print("Enter 3 to add a new bookshelf")
    print("Enter 4 to remove a bookshelf")
    print("Enter 5 to list all bookshelves")
    print("Enter 6 to list books in a bookshelf")
    print("Enter 7 to list books of a genre")
    print("Enter 8 to list books by rating")
    print("Enter 9 to exit\n")

    choice = input("Enter your choice: ")
    return choice

library = Library("library_main")

choice = ""

while choice != "9":
    choice = open_menu()
    # Add book
    if choice == "1":
        pass
    # Find book
    elif choice == "2":
        pass
    # Add bookshelf
    elif choice == "3":
        pass
    # Remove bookshelf
    elif choice == "4":
        pass
    # List all bookshelves
    elif choice == "5":
        pass
    # List books in a bookshelf 
    elif choice == "6":
        pass
    # List books by genre
    elif choice == "7":
        pass
    # List books by highest rating
    elif choice == "8":
        pass
    # Exit
    elif choice == "9":
        pass
    else: 
        print("Invalid, enter choice between 1-9\n")
