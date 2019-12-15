#from model_db import Book, Books
from model_file import Book, Books

def getAllBookslogic():
    return Books().All()

def getBookByIdLogic(id):
    return Books().Single(id)

def addBookLogic(newBookData):    
    newBook = Book()
    newBook.name = newBookData.get('name', '')
    newBook.price = float(newBookData.get('price', 0))
    newBook.isbn = int(newBookData.get('isbn', 0))
    newBook.obsolete = newBookData.get('obsolete', False)
    newBook.bookType = int(newBookData.get('bookType', 0))

    validateName(newBook.name)
    validateISBN(newBook.isbn)
    validateBookType(newBook.bookType)

    Books().Add(newBook)

    return vars(newBook)

def editBookLogic(id, updatedBook):
    if 'name' in updatedBook:
        validateName(updatedBook['name'])
    if 'isbn' in updatedBook:
        validateISBN(updatedBook['isbn'])
    if 'bookType' in updatedBook:
        validateBookType(updatedBook['bookType'])

    Books().Edit(id, updatedBook)
    return    

def deleteBookLogic(id):
    Books().Delete(id)
    return

def validateName(value):
    if len(value) > 30:
        raise Exception('Maximum length of field [Name] is 30 characters')
    return

def validateISBN(value):
    if (int(value) < 1) or (int(value) > 10000 - 1):
        raise Exception('Value of [ISBN] must be between 1 and 9999')
    return

def validateBookType(value):
    if (int(value) < 1) or (int(value) > 3):
        raise Exception('Value of [BookType] must be between 1 and 3')
    return
