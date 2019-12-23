import json
from os import path
import mysql.connector

import controller
import globals
from repository import Book

globals.engine = 'mysql'

def createConnection():
    return mysql.connector.connect(
        host = controller.app.config['MYSQL_HOST'],
        user = controller.app.config['MYSQL_USER'],
        passwd = controller.app.config['MYSQL_PASSWORD'],
        database = controller.app.config['MYSQL_DATABASE'],
    )

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
    connection = createConnection()
    try:
        cursor = connection.cursor()
        # Fields MUST be in this order to provide proper extraction (only MySQL)        
        sql = 'select Id, Name, Price, ISBN, IsObsolete, Booktype from Books order by Id;'
        cursor.execute(sql)

        booksFromDb = cursor.fetchall()

        books = []
        for book in booksFromDb:
            # TODO (mysql) Access result by name, just like sqlite
            newBook = Book (
                book[0], # Id
                book[1], # Name
                book[2], # Price; use simplejson for correct conversion of decimals
                book[3], # ISBN
                book[4], # IsObsolete
                book[5]  # BookType
            )
            books.append(vars(newBook))
    except mysql.connector.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return books

def getBookById(id):
    connection = createConnection()
    cursor = connection.cursor()
    returnValue = []
    try:
        # Fields MUST be in this order to provide proper extraction (only MySQL)        
        sql = 'select Id, Name, Price, ISBN, IsObsolete, Booktype from Books where Id = %s;' % (id)
        cursor.execute(sql)
        booksFromDb = [cursor.fetchone()]        

        if booksFromDb != [None]:
            newBook = Book (
                booksFromDb[0][0], # Id
                booksFromDb[0][1], # Name
                booksFromDb[0][2], # Price; use simplejson for correct conversion of decimals
                booksFromDb[0][3], # ISBN
                booksFromDb[0][4], # IsObsolete
                booksFromDb[0][5]  # BookType
            )
            returnValue = [vars(newBook)]
    except mysql.connector.Error as error:
        raise Exception(error)            
    finally:
        cursor.close()
        connection.close()

    return returnValue

def addBook(newBook):
    connection = createConnection()
    cursor = connection.cursor()
    try:
        sql = 'insert into Books (Name, ISBN, Price, IsObsolete, Booktype) values (\'%s\', %d, %f, %s, %d);' % (newBook.name, newBook.isbn, newBook.price, newBook.isObsolete, newBook.bookType)
        cursor.execute(sql)
        cursor.execute('SELECT LAST_INSERT_ID();')
        newId = cursor.fetchone()[0]
        connection.commit()
    except mysql.connector.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return newId

def deleteBook(id):
    connection = createConnection()
    cursor = connection.cursor()
    try:
        sql = 'delete from Books where Id = %s;' % (id)
        cursor.execute(sql)
        connection.commit()
    except mysql.connector.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return

def editBook(id, updatedBook):
    connection = createConnection()
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
    except mysql.connector.Error as error:
        raise Exception(error)
    finally:
        cursor.close()
        connection.close()
    return

