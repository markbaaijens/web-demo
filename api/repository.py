# TODO (db) Proper capitalisation of fieldnames
class Book():
    def __init__(self, id=0, name='', price=0, isbn=0, isObsolete=False, bookType=0):
        self.id = id              # Integer
        self.name = name          # String(30)
        self.price = price        # Numeric
        self.isbn = isbn          # Integer
        self.isObsolete = isObsolete  # Boolean
        self.bookType = bookType  # Enum: 0 = Unknown, 1 = fiction, 2 = non-fiction, 3 = educational    
