import json

# TODO: book.json
# TODO: separate data-folder ./data
DATA_FILE_NAME = "data.json"

books = []

class Book():
    def __init__(self, id, name, price, isbn):
        self.id = id
        self.name = name
        self.price = price
        self.isbn = isbn

def saveData():
    datasAsJson = json.dumps(books)
    f = open(DATA_FILE_NAME,"w")
    f.write(datasAsJson)
    f.close()
    return

def readData():
    booksFromFile = eval(open(DATA_FILE_NAME).read())

    # TODO: parse booksFromFile into newBook

    newBook = {
        'id': 1, 
        'name': "",
        'price': 0,
        'isbn': 0,
    }       
    
    books.append(newBook)

    return

'''
# Manual methods to fill books-dictionairy

# (1) Fill books by fixed data
books = [
    {
        "price": 20,
        "isbn": 22, 
        "id": 2, 
        "name": "Boek 2"
    }
]

# (2) Fill books by generating data
newBook = Book(1, "Boek 1", 10, 11)
books.append(newBook.__dict__)
newBook = Book(2, "Boek 2", 20, 22)
books.append(newBook.__dict__)
newBook = Book(3, "Boek 3", 30, 33)
books.append(newBook.__dict__)
'''
