import json
from os import path

import globals

globals.engine = 'file'

DATA_FILE_NAME = "./data/book.json"

books = []

# TODO Strong typed class
class Book():
    def __init__(self, id=0, name='', price=0, isbn=0, isObsolete=False, bookType=0):
        self.id = id              # Integer
        self.name = name          # String(30)
        self.price = price        # Numeric
        self.isbn = isbn          # Integer
        self.isObsolete = isObsolete  # Boolean
        self.bookType = bookType  # Enum: 0 = Unknown, 1 = fiction, 2 = non-fiction, 3 = educational       

class Books:
    def All(self):
        return getAllBooks()
    def Single(self, id):
        return getBookById(id)
    def Add(self, newBook):
        return addBook(newBook)
    def Delete(self, id):
        return deleteBook(id)
    def Edit(self, id, updatedBook):
        return editBook(id, updatedBook)

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
            book['isObsolete'],
            book['bookType']
        )
        books.append(vars(newBook))

    return

def getAllBooks():
    return books

def getBookById(id):
    book = [book for book in books if book['id'] == id]
    return book

def addBook(newBook):
    try:   
        # This will bounce when books is empty
        id = books[-1]['id'] + 1
    except:
        id = 0
    newBook.id = id

    books.append(vars(newBook))
    saveData()
    return id

def deleteBook(id):
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1
    
    books.remove(books[index])
    saveData()
    return

def editBook(id, updatedBook):
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
    if 'isObsolete' in updatedBook:
        books[index]['isObsolete'] = updatedBook['isObsolete']
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

