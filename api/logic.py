from model import books, saveData, readData, Book

EXCEPTION_FIELD_ISBN_IS_REQUIRED =  'EXCEPTION_FIELD_ISBN_IS_REQUIRED'

def getAllBookslogic():
    return books

def getBookByIdLogic(id):
    book = [book for book in books if book['id'] == id]
    return book

def addBookLogic(newBookData):
    if newBookData['isbn'] == 0:
        raise Exception(EXCEPTION_FIELD_ISBN_IS_REQUIRED)

    try:   
        # This will bounce when books is empty
        id = books[-1]['id'] + 1
    except:
        id = 0
    
    newBook = Book()
    newBook.id = id 
    newBook.name = newBookData.get('name', '')
    newBook.price = float(newBookData.get('price', 0))
    newBook.isbn = int(newBookData.get('isbn', 0))
    newBook.obsolete = newBookData.get('obsolete', False)
    newBook.bookType = int(newBookData.get('bookType', 0))

    books.append(vars(newBook))
    saveData()
    return vars(newBook)

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
        books[index]['isbn'] = int(updatedBook['isbn'])
    if 'price' in updatedBook:
        books[index]['price'] = float(updatedBook['price'])
    if 'obsolete' in updatedBook:
        books[index]['obsolete'] = updatedBook['obsolete']
    if 'bookType' in updatedBook:
        books[index]['bookType'] = int(updatedBook['bookType'])

    saveData()
    return   

def deleteBookLogic(id):
    index = 0
    for book in books:
        if book['id'] == id:
            break
        index += 1
    books.remove(books[index])
    saveData()
    return
