import json
from os import path
import sqlite3

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

def getAllBooksModel():
    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute('select Id, ISBN, Name, Obsolete, Price, Booktype from Books order by Id;')
   
    booksFromDb = cur.fetchall()

    books = []
    for book in booksFromDb:
        newBook = Book (
            book['id'], 
            book['name'],
            book['price'],
            book['isbn'],
            book['obsolete'],
            book['bookType']
        )
        books.append(vars(newBook))

    return books

def getBookByIdModel(id):
    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute('select Id, ISBN, Name, Obsolete, Price, Booktype from Books where Id = %s;' % (id))
   
    booksFromDb = cur.fetchall()

    for book in booksFromDb:
        # There is one and only one book
        newBook = Book (
            book['id'], 
            book['name'],
            book['price'],
            book['isbn'],
            book['obsolete'],
            book['bookType']
        )
    return vars(newBook)

def addBookModel(newBook):
    # TODO Implement addBookModel
    '''
    books.append(vars(newBook))
    saveData()
    '''
    return

def deleteBookModel(id):
    # TODO Implement deleteBookModel
    ''' 
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1
    
    books.remove(books[index])
    saveData()
    '''
    return

def editBookModel(id, updatedBook):
    # TODO Implement editBookModel
    '''
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1

    if 'name' in updatedBook:
        books[index]['name'] = updatedBook['name']
    if 'isbn' in updatedBook:
        if updatedBook['isbn'] == 0:
            raise Exception(EXCEPTION_FIELD_ISBN_IS_REQUIRED)
        books[index]['isbn'] = int(updatedBook['isbn'])
    if 'price' in updatedBook:
        books[index]['price'] = float(updatedBook['price'])
    if 'obsolete' in updatedBook:
        books[index]['obsolete'] = updatedBook['obsolete']
    if 'bookType' in updatedBook:
        books[index]['bookType'] = int(updatedBook['bookType'])

    saveData()    
    '''
    return


def readData():
    pass

def saveData():
    pass
