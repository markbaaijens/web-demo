from flask import Flask, render_template, jsonify, request
import requests
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# TODO (api)/version instead of (api)/
# TODO Edit-form (flask-wtf)
# TODO Implement delete (show delete-link on each item); delete button
# TODO Error when page (or id) not found
# TODO Show API-url

# Globals
apiInfo = []

def getApiInfo():
    try:
        # Using eval to convert string to a dictionairy
        apiInfo = eval(requests.get(Config.API_ROOT_URL).content)
    except:
        apiInfo = []

    return apiInfo

# GET /
@app.route('/', methods=['GET'])
def index():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(Config.API_ROOT_URL + '/books').content)
    except:
        bookList = []

    return render_template('index.html', title = 'Titel', api = apiInfo, books = bookList)

# GET /books
@app.route('/books', methods=['GET'])
def getBooks():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(Config.API_ROOT_URL + '/books').content)
    except:
        bookList = []

    nrOfBooks = len(bookList)  # Count books client-side
    print(nrOfBooks)

    return render_template('books.html', title = 'Titel', api = apiInfo, books = bookList, 
        nrOfBooks = nrOfBooks)

# GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def getBooksById(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(Config.API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []  

    return render_template('book.html', title = 'Titel', api = apiInfo, books = bookList)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload
