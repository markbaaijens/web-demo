import json
from os import path

DATA_FILE_NAME = "./data/book.json"

books = []

# TODO Strong typed class
class Book():
    def __init__(self, id=0, name='', price=0, isbn=0, obsolete=False, bookType=0):
        self.id = id              # Integer
        self.name = name          # String(30)
        self.price = price        # Numeric
        self.isbn = isbn          # Integer
        self.obsolete = obsolete  # Boolean
        self.bookType = bookType  # Enum: 0 = Unknown, 1 = fiction, 2 = non-fiction, 3 = educational       

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
        newBook = Book (
            book['id'], 
            book['name'],
            book['price'],
            book['isbn'],
            book['obsolete'],
            book['bookType']
        )
        books.append(vars(newBook))

    return

def getAllBooksModel():
    return books

def getBookByIdModel(id):
    book = [book for book in books if book['id'] == id]
    return book

def addBookModel(newBook):
    try:   
        # This will bounce when books is empty
        id = books[-1]['id'] + 1
    except:
        id = 0
    newBook.id = id

    books.append(vars(newBook))
    saveData()
    return

def deleteBookModel(id):
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1
    
    books.remove(books[index])
    saveData()
    return

def editBookModel(id, updatedBook):
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1

    if 'name' in updatedBook:
        books[index]['name'] = updatedBook['name']
    if 'isbn' in updatedBook:
        books[index]['isbn'] = int(updatedBook['isbn'])
    if 'price' in updatedBook:
        books[index]['price'] = float(updatedBook['price'])
    if 'obsolete' in updatedBook:
        books[index]['obsolete'] = updatedBook['obsolete']
    if 'bookType' in updatedBook:
        books[index]['bookType'] = int(updatedBook['bookType'])

    saveData()    
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

# Execute on load
readData()

