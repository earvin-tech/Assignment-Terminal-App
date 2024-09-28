import json

from classes.library import Library
from classes.bookshelf import Bookshelf

def save_and_exit(library):
    json_to_write1 = []
    for bookshelf in library.get_all_bookshelves():
        if bookshelf.get_books():
            bookshelf_json = {
                "bookshelf_name": bookshelf.get_name(),
                "books": bookshelf.get_books()
            }
        else:
            bookshelf_json = {
                "bookshelf_name": bookshelf.get_name()
            }
        json_to_write1.append(bookshelf_json)
    
    with open("data/library.json", "w") as json_file1:
        json.dump(json_to_write1, json_file1, indent=4)

    json_to_write2 = []

def load_from_file(library):
    try:
        with open("data/library.json", "r") as json_file1:
            json_to_load1 = json.load(json_file1)

        for bookshelf in json_to_load1:
            bookshelf = Bookshelf(bookshelf["bookshelf_name"])
            
            library.add_bookshelf(bookshelf)

    except FileNotFoundError:
        print("The file does not exist")
