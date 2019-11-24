from model import *

EXCEPTION_FIELD_ISBN_IS_REQUIRED =  'EXCEPTION_FIELD_ISBN_IS_REQUIRED'

def getAllBookslogic():
    return books

def getBookByIdLogic(id):
    book = [book for book in books if book['id'] == id]
    return book

def addBookLogic(newBookData):

    newBook = {
        'id': books[-1]['id'] + 1, 
        'name': newBookData.get('name', ''),
        'price': newBookData.get('price', 0),
        'isbn': newBookData.get('isbn', 0),
    }

    books.append(newBook)
    return newBook

def editBookLogic(id, updatedBook):
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
        books[index]['isbn'] = updatedBook['isbn']
    if 'price' in updatedBook:
        books[index]['price'] = updatedBook['price']

    return True    

def deleteBookLogic(id):
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1
    books.remove(books[index])
    return True