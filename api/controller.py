from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'name': 'Boek 1',
        'price': 10,
        'isbn': 11
    },
    {
        'id': 2,
        'name': 'Boek 2',
        'price': 20.0,
        'isbn': 22
    },
    {
        'id': 3,
        'name': 'Boek 3',
        'price': 30.0,
        'isbn': 33
    }
]

@app.errorhandler(404)
def notFoundError(error):
    return make_response(jsonify({'message': 'Not Found: ' + request.url}), 404)

@app.errorhandler(400)
def invalidBodyError(error):
    return make_response(jsonify({'message': 'Bad request'}), 400)

@app.errorhandler(405)
def methodNotAllowedError(error):
    return make_response(jsonify({'message': 'Method ' + request.method + ' is not allowed on ' + request.url}), 400)

# GET /
@app.route('/', methods=['get'])
def root():
    return make_response(jsonify({'message': 'API-demo version 1.0'}), 200)

# GET /books
# curl -i http://localhost:5000/books
@app.route('/books', methods=['get'])
def getBooks():
    return make_response(jsonify(getAllBookslogic()), 200)

# GET /books/<id>
# curl -i http://localhost:5000/books/1
@app.route('/books/<int:id>', methods=['get'])
def getBookById(id):
    book = getBookByIdLogic(id)
    if len(book) == 0:
        abort(404)
    return make_response(jsonify(book), 200)

# POST /books/<id>
# curl -i http://localhost:5000/books -X POST -H "Content-Type: application/json" -d '{"isbn": 5, "name":"Name"}' 
@app.route('/books', methods=['post'])
def addBook():
    if not request.json:
        abort(400)
    if not 'isbn' in request.json:
        abort(400)

    newBookData = {
        'name': request.json['name'],
        'price': request.json.get('price', 0),
        'isbn': request.json.get('isbn', 0),
    }
    newBook = addBookLogic(newBookData)
    return make_response(jsonify(newBook), 201)

# PATCH /books/<id>
# curl -i http://localhost:5000/books/3 -X PATCH -H "Content-Type: application/json" -d '{"isbn": 66, "name":"Name"}'
@app.route('/books/<int:id>', methods=['patch'])
def editBook(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)

    requestData = request.get_json()

    updatedBook = {}
    if 'name' in requestData:
        updatedBook['name'] = requestData['name']
    if 'isbn' in requestData:
        updatedBook['isbn'] = requestData['isbn']
    if 'price' in requestData:
        updatedBook['price'] = requestData['price']

    editBookLogic(id, updatedBook)

    return make_response(jsonify(updatedBook), 200)

# DELETE /books/<id>
# curl -i http://localhost:5000/books/3 -X DELETE
@app.route('/books/<int:id>', methods=['delete'])
def deleteBook(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    deleteBookLogic(id)
    return make_response("", 200)

#
# Logic
#
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # auto-reload
