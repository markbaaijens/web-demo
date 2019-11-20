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
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url
    }
    return make_response(jsonify(message), 404)

@app.errorhandler(400)
def invalidBodyError(error):
    message = {
            'status': 400,
            'message': 'Bad request'
    }
    return make_response(jsonify(message), 400)

@app.errorhandler(405)
def methodNotAllowedError(error):
    message = {
            'status': 405,
            'message': 'Method ' + request.method + ' is not allowed on ' + request.url
    }
    return make_response(jsonify(message), 400)

@app.route('/')
def root():
    return "Hello world"

# GET /books
# curl -i http://localhost:5000/books
@app.route('/books', methods=['get'])
def getBooks():
    print('get')
    return jsonify({'books': books})

# GET /books/<id>
# curl -i http://localhost:5000/books/1
@app.route('/books/<int:id>', methods=['get'])
def getBookById(id):
    returnValue = {}
    for book in books:
        if book['id'] == id:
            returnValue = {
                'id': book['id'],
                'name': book['name'],
                'price': book['price'],
                'isbn': book['isbn']
            }   
    if len(returnValue) == 0:
        abort(404)

    return jsonify(returnValue)

# POST /books/<id>
# curl -i http://localhost:5000/books -H "Content-Type: application/json" -X POST -d '{"isbn": 5, "name":"Name"}' 
@app.route('/books', methods=['post'])
def addBook():
    if not request.json or not 'isbn' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json.get('price', ""),
        'isbn': request.json.get('isbn', 0),
    }
    books.append(book)
    return jsonify({'book': book}), 201

# PATCH /books
# curl -i http://localhost:5000/books/3 -H "Content-Type: application/json" -X PATCH -d '{"isbn": 66, "name":"Name"}' @a
@app.route('/books/<int:id>', methods=['patch'])d
ef editBook(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)

    req = request.get_json()
    print(book)
    print(req)

    for key, value in req.items():
        print(key + '|' + str(value))
        #print(book[key])
        #book[key] = value

        if key =='isbn':  
            book['isbn'] = key
        if key == 'name': 
            book['name'] = key
 #   print(book)

 #   book[id] = req
 #   res = make_response(jsonify({"message": "Collection created"}), 201)
 #   return res

    return jsonify({'result': True})
#    return jsonify({"message": "Collection updated"}), 200)


# DELETE /books/<id>
# curl -i http://localhost:5000/books/3 -X DELETE
@app.route('/books/<int:id>', methods=['delete'])
def deleteBook(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # auto-reload
