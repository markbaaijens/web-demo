from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

CONST_API_ROOT_URL = 'http://localhost:5000'
CONST_WEB_ROOT_URL = 'http://localhost:5001'

# TODO (api)/version instead of (api)/
# TODO Implement delete (show delete-link on each item)
# TODO Show number of books (API-call)
# TODO Error when page (or id) not found

# Globals
apiInfo = []

def getApiInfo():
    try:
        # Using eval to convert string to a dictionairy
        apiInfo = eval(requests.get(CONST_API_ROOT_URL).content)
    except:
        apiInfo = []

    return apiInfo

# GET /
@app.route('/', methods=['GET'])
def index():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(CONST_API_ROOT_URL + '/books').content)
    except:
        bookList = []

    return render_template('index.html', title = 'Titel', api = apiInfo, books = bookList, webRootUrl = CONST_WEB_ROOT_URL)

# GET /books
@app.route('/books', methods=['GET'])
def getBooks():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(CONST_API_ROOT_URL + '/books').content)
    except:
        bookList = []

    return render_template('books.html', title = 'Titel', api = apiInfo, books = bookList, webRootUrl = CONST_WEB_ROOT_URL)

# GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def getBooksById(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(CONST_API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []

    return render_template('book.html', title = 'Titel', api = apiInfo, books = bookList, webRootUrl = CONST_WEB_ROOT_URL)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload
