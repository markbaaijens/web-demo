import json
from os import path
import sqlite3

import controller
import globals

globals.engine = 'sqlite'

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
        return getAllBooks()
    def Single(self, id):
        return getBookById(id)
    def Add(self, newBook):
        return addBook(newBook)
    def Delete(self, id):
        return deleteBook(id)
    def Edit(self, id, updatedBook):
        return editBook(id, updatedBook)

def getAllBooks():
    con = sqlite3.connect(controller.app.config['DB_FILE_NAME'])
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

def getBookById(id):
    con = sqlite3.connect(controller.app.config['DB_FILE_NAME'])
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    returnValue = []
    try:
        sql = 'select Id, ISBN, Name, Obsolete, Price, Booktype from Books where Id = %s;' % (id)
        cur.execute(sql)
        booksFromDb = [cur.fetchone()]
        newBook = Book (
            booksFromDb[0]['id'], 
            booksFromDb[0]['name'],
            booksFromDb[0]['price'],
            booksFromDb[0]['isbn'],
            booksFromDb[0]['obsolete'],
            booksFromDb[0]['bookType']
        )
        returnValue = [vars(newBook)]
    finally:
        cur.close()
        con.close()

    return returnValue

def addBook(newBook):
    con = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
    cur = con.cursor()
    try:
        sql = 'insert into Books (Name, ISBN, Price, Obsolete, Booktype) values (\'%s\', %d, %f, %s, %d);' % (newBook.name, newBook.isbn, newBook.price, newBook.obsolete, newBook.bookType)
        cur.execute(sql)
        con.commit()
    finally:
        cur.close()
        con.close()
    return

def deleteBook(id):
    con = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
    cur = con.cursor()
    try:
        sql = 'delete from Books where Id = %s;' % (id)
        cur.execute(sql)
        con.commit()
    finally:
        cur.close()
        con.close()
    return

def editBook(id, updatedBook):
    con = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
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

