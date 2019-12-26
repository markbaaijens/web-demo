from flask import Flask, jsonify, abort, make_response, request
import logging
from logging.handlers import RotatingFileHandler
import traceback

import logic 
from config import Config
import globals

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405

app = Flask(__name__)

app.config.from_object(Config)

logger = logging.getLogger()
if not logger.handlers:
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.handlers.RotatingFileHandler(
        app.config['LOG_FILE_NAME'], 'a', app.config['LOG_MAX_SIZE'], app.config['LOG_BACKUP_COUNT'])
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(consoleHandler)

@app.errorhandler(HTTP_NOT_FOUND)
def notFoundError(error):
    return make_response(jsonify({'message': 'Not Found: ' + request.url}), HTTP_NOT_FOUND)

@app.errorhandler(HTTP_BAD_REQUEST)
def invalidBodyError(error):
    return make_response(jsonify({'message': 'Bad request'}), HTTP_BAD_REQUEST)

@app.errorhandler(HTTP_METHOD_NOT_ALLOWED)
def methodNotAllowedError(error):
    return make_response(jsonify({'message': 'Method ' + request.method + ' is not allowed on ' + request.url}), HTTP_METHOD_NOT_ALLOWED)

def BuildResponse(statusCode, body, location):
    response = make_response( body, statusCode)
    response.headers['Location'] = location
    return response

# GET /api
# curl -i http://localhost:5000/api
@app.route('/api', methods=['GET'])
def root():
    return BuildResponse(HTTP_OK, jsonify({'name': 'web-demo'}, {'version': '1.0'}, {'engine': globals.engine}), request.url)

# GET /api/books
# curl -i http://localhost:5000/api/books
@app.route('/api/books', methods=['GET'])
def getBooks():
    try:
        books = logic.getAllBooks()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return make_response(jsonify({'message': str(e) }), HTTP_BAD_REQUEST)

    return BuildResponse(HTTP_OK, jsonify(books), request.url)

# GET /api/books/<id>
# curl -i http://localhost:5000/api/books/1
@app.route('/api/books/<int:id>', methods=['GET'])
def getBookById(id):
    try:
        book = logic.getBookById(id)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return BuildResponse(HTTP_BAD_REQUEST, jsonify({'message': str(e)}), request.url)
    
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)
    return BuildResponse(HTTP_OK, jsonify(book), request.url)

# POST /api/books
# curl -i http://localhost:5000/api/books -X POST -H "Content-Type: application/json" -d '{"isbn": 5, "name":"Name"}' 
@app.route('/api/books', methods=['POST'])
def addBook():
    if not request.json:
        abort(HTTP_BAD_REQUEST)

    try:
        newBook = logic.addBook(request.json)
    except Exception as e:
        logger.error(e)        
        logger.error(traceback.format_exc())
        return BuildResponse(HTTP_BAD_REQUEST, jsonify({'message': str(e)}), request.url)
    
    return BuildResponse(HTTP_CREATED, jsonify(newBook), request.url)

# PATCH /api/books/<id>
# curl -i http://localhost:5000/api/books/3 -X PATCH -H "Content-Type: application/json" -d '{"isbn": 66, "name":"Name"}'
@app.route('/api/books/<int:id>', methods=['PATCH'])
def editBook(id):
    if not request.json:
        abort(HTTP_BAD_REQUEST)

    book = logic.getBookById(id)
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)

    requestData = request.get_json()

    try:
        logic.editBook(id, requestData) 
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return BuildResponse(HTTP_BAD_REQUEST, jsonify({'message': str(e)}), request.url)

    return BuildResponse(HTTP_OK, jsonify(requestData), request.url)

# DELETE /api/books/<id>
# curl -i http://localhost:5000/api/books/3 -X DELETE
@app.route('/api/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    book = logic.getBookById(id)
    if len(book) == 0:
        abort(HTTP_NOT_FOUND)

    try:
        logic.deleteBook(id)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return BuildResponse(HTTP_BAD_REQUEST, jsonify({'message': str(e)}), request.url)
    return BuildResponse(HTTP_OK, '', request.url)

if __name__ == '__main__':
    logger.debug('App Started')
    app.run(port=5000, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5000)  # public server, reachable from remote
    logger.debug('App Stopped')


