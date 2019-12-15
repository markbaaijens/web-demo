from model_db import readData, Book, getAllBooksModel, getBookByIdModel, addBookModel, deleteBookModel, editBookModel
#from model_file import readData, Book, getAllBooksModel, getBookByIdModel, addBookModel, deleteBookModel, editBookModel

EXCEPTION_FIELD_ISBN_IS_REQUIRED = 'EXCEPTION_FIELD_ISBN_IS_REQUIRED'

def getAllBookslogic():
    return getAllBooksModel()

def getBookByIdLogic(id):
    return getBookByIdModel(id)

def addBookLogic(newBookData):
    if newBookData['isbn'] == 0:
        raise Exception(EXCEPTION_FIELD_ISBN_IS_REQUIRED)
    
    newBook = Book()
    newBook.name = newBookData.get('name', '')
    newBook.price = float(newBookData.get('price', 0))
    newBook.isbn =  int(newBookData.get('isbn', 0))
    newBook.obsolete = newBookData.get('obsolete', False)
    newBook.bookType = int(newBookData.get('bookType', 0))

    print(vars(newBook))
    addBookModel(newBook)

    return vars(newBook)

def editBookLogic(id, updatedBook):
    editBookModel(id, updatedBook)
    return True    

def deleteBookLogic(id):
    deleteBookModel(id)
    return True