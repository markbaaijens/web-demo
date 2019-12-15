import json
from os import path
import sqlite3

# TODO (db) Proper capitalisation of fieldnames

# TODO Strong typed class
class Book():
    def __init__(self, id=0, name='', price=0, isbn=0, obsolete=False, bookType=0):
        self.id = id              # Integer
        self.name = name          # String(30)
        self.price = price        # Numeric
        self.isbn = isbn          # Integer
        self.obsolete = obsolete  # Boolean
        self.bookType = bookType  # Enum: 0 = Unknown, 1 = fiction, 2 = non-fiction, 3 = educational    

class Books:
    def All(self):
        return getAllBooksModel()
    def Single(self, id):
        return getBookByIdModel(id)
    def Add(self, newBook):
        return addBookModel(newBook)
    def Delete(self, id):
        return deleteBookModel(id)
    def Edit(self, id, updatedBook):
        return editBookModel(id, updatedBook)

def getAllBooksModel():
    con = sqlite3.connect(app.config['DB_FILE_NAME'])
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
    con = sqlite3.connect(app.config['DB_FILE_NAME'])
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    returnValue = []
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
            returnValue = [vars(newBook)]
    finally:
        cur.close()
        con.close()

    return returnValue

def addBookModel(newBook):
    con = sqlite3.connect(app.config['DB_FILE_NAME'])   
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
    con = sqlite3.connect(app.config['DB_FILE_NAME'])   
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
    con = sqlite3.connect(app.config['DB_FILE_NAME'])   
    cur = con.cursor()
    try:
        sql = 'update Books set '

        if 'name' in updatedBook:
            sql = sql + 'Name = \'%s\'' % (updatedBook['name']) + ', '
        if 'isbn' in updatedBook:
            sql = sql + 'ISBN = %d' % (int(updatedBook['isbn'])) + ', '
        if 'price' in updatedBook:
            sql = sql + 'Price = %f' % (float(updatedBook['price'])) + ', '
        if 'obsolete' in updatedBook:
            sql = sql + 'Obsolete = %d' % (updatedBook['obsolete']) + ', '
        if 'bookType' in updatedBook:
            sql = sql + 'BookType = %d' % (int(updatedBook['bookType'])) + ', '  
        sql = sql[:-2]  # Trim last comma

        sql = sql + ' ' + 'where Id = %d' % (id)

        cur.execute(sql)
        con.commit()
    finally:
        cur.close()
        con.close()
    return

