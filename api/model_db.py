import json
from os import path
import sqlite3

DB_FILE_NAME = "data/data.db"

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
    con = sqlite3.connect(DB_FILE_NAME)
    con.row_factory = sqlite3.Row
    try:
        cur = con.cursor()
        sql = 'select Id, ISBN, Name, Obsolete, Price, Booktype from Books order by Id;'
        cur.execute(sql)
    
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
    finally:
        cur.close()
        con.close()
    return books

def getBookByIdModel(id):
    con = sqlite3.connect(DB_FILE_NAME)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    try:
        sql = 'select Id, ISBN, Name, Obsolete, Price, Booktype from Books where Id = %s;' % (id)
        cur.execute(sql)
    
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
    finally:
        cur.close()
        con.close()
    # TODO (db) Valid output when record not found
    return vars(newBook)

def addBookModel(newBook):
    con = sqlite3.connect(DB_FILE_NAME)   
    cur = con.cursor()
    try:
        sql = 'insert into Books (Name, ISBN, Price, Obsolete, Booktype) values (\'%s\', %d, %f, %s, %d);' % (newBook.name, newBook.isbn, newBook.price, newBook.obsolete, newBook.bookType)
        cur.execute(sql)
        con.commit()
    finally:
        cur.close()
        con.close()
    return

def deleteBookModel(id):
    con = sqlite3.connect(DB_FILE_NAME)   
    cur = con.cursor()
    try:
        sql = 'delete from Books where Id = %s;' % (id)
        cur.execute(sql)
        con.commit()
    finally:
        cur.close()
        con.close()
    return

def editBookModel(id, updatedBook):
    # TODO (db) Implement editBookModel
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

