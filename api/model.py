class Book():
    def __init__(self, id, name, price, isbn):
        self.id = id
        self.name = name
        self.price = price
        self.isbn = isbn

books = []
newBook = Book(1, "Boek 1", 10, 11)
books.append(newBook.__dict__)
newBook = Book(2, "Boek 2", 20, 22)
books.append(newBook.__dict__)
newBook = Book(3, "Boek 3", 30, 33)
books.append(newBook.__dict__)
