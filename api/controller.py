from flask import Flask, jsonify, abort, make_response, request
from logic import addBookLogic, editBookLogic, deleteBookLogic
from logic import getAllBookslogic, getBookByIdLogic
from logic import books, readData

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405

app = Flask(__name__)

@app.errorhandler(HTTP_NOT_FOUND)
def notFoundError(error):
    return make_response(jsonify({'message': 'Not Found: ' + request.url}), HTTP_NOT_FOUND)

@app.errorhandler(HTTP_BAD_REQUEST)
def invalidBodyError(error):
    return make_response(jsonify({'message': 'Bad request'}), HTTP_BAD_REQUEST)

@app.errorhandler(HTTP_METHOD_NOT_ALLOWED)
def methodNotAllowedError(error):
    return make_response(jsonify({'message': 'Method ' + request.method + ' is not allowed on ' + request.url}), HTTP_METHOD_NOT_ALLOWED)

# GET /
# curl -i http://localhost:5000
@app.route('/', methods=['GET'])
def root():
    return make_response(jsonify({'app': 'API-demo'}, {'version': '1.0'}), HTTP_OK)

# GET /books
# curl -i http://localhost:5000/books
@app.route('/books', methods=['GET'])
def getBooks():
    try:
        books = getAllBookslogic()
    except Exception as e:
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)

    return make_response(jsonify(books), HTTP_OK)

# GET /books/<id>
# curl -i http://localhost:5000/books/1
@app.route('/books/<int:id>', methods=['GET'])
def getBookById(id):
    try:
        book = getBookByIdLogic(id)
    except Exception as e:
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)
    
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)
    return make_response(jsonify(book), HTTP_OK)

# POST /books/<id>
# curl -i http://localhost:5000/books -X POST -H "Content-Type: application/json" -d '{"isbn": 5, "name":"Name"}' 
@app.route('/books', methods=['POST'])
def addBook():
    # TODO Facilitate minimal data
    if not request.json:
        abort(HTTP_BAD_REQUEST)
    if not 'isbn' in request.json:
        abort(HTTP_BAD_REQUEST)

    newBookData = {
        'name': request.json['name'],
        'price': float(request.json.get('price', 0)),
        'isbn': int(request.json.get('isbn', 0)),
    }

    try:
        newBook = addBookLogic(newBookData)
    except Exception as e:
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)
    
    return make_response(jsonify(newBook), HTTP_CREATED)

# PATCH /books/<id>
# curl -i http://localhost:5000/books/3 -X PATCH -H "Content-Type: application/json" -d '{"isbn": 66, "name":"Name"}'
@app.route('/books/<int:id>', methods=['PATCH'])
def editBook(id):
    if not request.json:
        abort(HTTP_BAD_REQUEST)

    # TODO Use getBookByIdLogic
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)

    requestData = request.get_json()

    updatedBook = {}
    if 'name' in requestData:
        updatedBook['name'] = requestData['name']
    if 'isbn' in requestData:
        updatedBook['isbn'] = int(requestData['isbn'])
    if 'price' in requestData:
        updatedBook['price'] = float(requestData['price'])
    try:
        editBookLogic(id, updatedBook) 
    except Exception as e:
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)

    return make_response(jsonify(updatedBook), HTTP_OK)

# DELETE /books/<id>
# curl -i http://localhost:5000/books/3 -X DELETE
@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    # TODO Use getBookByIdLogic
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)

    try:
        deleteBookLogic(id)
    except Exception as e:
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)        
    return make_response("", HTTP_OK)

if __name__ == '__main__':
    readData()
    app.run(port=5000, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5000)  # public server, reachable from remote

