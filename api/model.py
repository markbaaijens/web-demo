import json
from os import path

DATA_FILE_NAME = "./data/book.json"

books = []

# TODO Strong typed class
class Book():
    def __init__(self, id, name, price, isbn, obsolete, bookType):
        self.id = id              # Integer
        self.name = name          # String(30)
        self.price = price        # Float
        self.isbn = isbn          # Integer
        self.obsolote = obsolete  # Boolean
        self.type = bookType      # Enum: 0 = Unknown, 1 = fiction, 2 = non-fiction, 3 = educational       

def saveData():
    datasAsJson = json.dumps(books)
    f = open(DATA_FILE_NAME,"w")
    f.write(datasAsJson)
    f.close()
    return

def readData():
    if not path.exists(DATA_FILE_NAME):
        return

    booksFromFile = json.loads(open(DATA_FILE_NAME).read())

    for book in booksFromFile:
        newBook = {
            'id': book['id'], 
            'name': book['name'],
            'price': book['price'],
            'isbn': book['isbn'],
            'obsolete': book['obsolete'],
            'bookType': book['bookType']
        }       
        books.append(newBook)

    return

'''
# Manual methods to fill books-dictionairy

# (1) Fill books by fixed data
books = [
    {
        "price": 20,
        "isbn": 22, 
        "id": 2, 
        "name": "Boek 2"
    }
]

# (2) Fill books by generating data
newBook = Book(1, "Boek 1", 10, 11)
books.append(newBook.__dict__)
newBook = Book(2, "Boek 2", 20, 22)
books.append(newBook.__dict__)
newBook = Book(3, "Boek 3", 30, 33)
books.append(newBook.__dict__)
'''
