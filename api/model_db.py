import json
from os import path
import sqlite3

import controller
import globals

globals.engine = 'sqlite'

# TODO (db) Proper capitalisation of fieldnames

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

def getAllBooks():
    connection = sqlite3.connect(controller.app.config['DB_FILE_NAME'])
    connection.row_factory = sqlite3.Row
    try:
        cursor = connection.cursor()
        sql = 'select Id, ISBN, Name, IsObsolete, Price, Booktype from Books order by Id;'
        cursor.execute(sql)
    
        booksFromDb = cursor.fetchall()

        books = []
        for book in booksFromDb:
            newBook = Book (
                book['id'], 
                book['name'],
                book['price'],
                book['isbn'],
                book['isObsolete'],
                book['bookType']
            )
            books.append(vars(newBook))
    except sqlite3.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return books

def getBookById(id):
    connection = sqlite3.connect(controller.app.config['DB_FILE_NAME'])
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    returnValue = []
    try:
        sql = 'select Id, ISBN, Name, IsObsolete, Price, Booktype from Books where Id = %s;' % (id)
        cursor.execute(sql)
        booksFromDb = [cursor.fetchone()]
        if booksFromDb != [None]:
            newBook = Book (
                booksFromDb[0]['id'], 
                booksFromDb[0]['name'],
                booksFromDb[0]['price'],
                booksFromDb[0]['isbn'],
                booksFromDb[0]['isObsolete'],
                booksFromDb[0]['bookType']
            )
            returnValue = [vars(newBook)]
    except sqlite3.Error as error:
        raise Exception(error)            
    finally:
        cursor.close()
        connection.close()

    return returnValue

def addBook(newBook):
    connection = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
    cursor = connection.cursor()
    try:
        sql = 'insert into Books (Name, ISBN, Price, IsObsolete, Booktype) values (\'%s\', %d, %f, %s, %d);' % (newBook.name, newBook.isbn, newBook.price, newBook.isObsolete, newBook.bookType)
        cursor.execute(sql)
        cursor.execute('SELECT last_insert_rowid()')
        newId = cursor.fetchone()[0]
        connection.commit()
    except sqlite3.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return newId

def deleteBook(id):
    connection = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
    cursor = connection.cursor()
    try:
        sql = 'delete from Books where Id = %s;' % (id)
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return

def editBook(id, updatedBook):
    connection = sqlite3.connect(controller.app.config['DB_FILE_NAME'])   
    cursor = connection.cursor()
    try:
        sql = 'update Books set '

        if 'name' in updatedBook:
            sql = sql + 'Name = \'%s\'' % (updatedBook['name']) + ', '
        if 'isbn' in updatedBook:
            sql = sql + 'ISBN = %d' % (int(updatedBook['isbn'])) + ', '
        if 'price' in updatedBook:
            sql = sql + 'Price = %f' % (float(updatedBook['price'])) + ', '
        if 'isObsolete' in updatedBook:
            sql = sql + 'IsObsolete = %d' % (updatedBook['isObsolete']) + ', '
        if 'bookType' in updatedBook:
            sql = sql + 'BookType = %d' % (int(updatedBook['bookType'])) + ', '  
        sql = sql[:-2]  # Trim last comma

        sql = sql + ' ' + 'where Id = %d' % (id)

        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return

