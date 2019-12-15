#from model_db import Book, Books
from model_file import Book, Books

EXCEPTION_FIELD_ISBN_IS_REQUIRED = 'EXCEPTION_FIELD_ISBN_IS_REQUIRED'

def getAllBookslogic():
    return Books().All()

def getBookByIdLogic(id):
    return Books().Single(id)

def addBookLogic(newBookData):
    if newBookData['isbn'] == 0:
        raise Exception(EXCEPTION_FIELD_ISBN_IS_REQUIRED)
    
    newBook = Book()
    newBook.name = newBookData.get('name', '')
    newBook.price = float(newBookData.get('price', 0))
    newBook.isbn =  int(newBookData.get('isbn', 0))
    newBook.obsolete = newBookData.get('obsolete', False)
    newBook.bookType = int(newBookData.get('bookType', 0))

    Books().Add(newBook)

    return vars(newBook)

def editBookLogic(id, updatedBook):
    Books().Edit(id, updatedBook)
    return True    

def deleteBookLogic(id):
    Books().Delete(id)
    return True