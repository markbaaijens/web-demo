from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

# Globals
apiInfo = []

def getApiInfo():
    try:
        # Using eval to convert string to a dictionairy
        apiInfo = eval(requests.get('http://localhost:5000').content)
    except:
        apiInfo = []

    return apiInfo

# GET /
@app.route('/', methods=['GET'])
def index():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get('http://localhost:5000/books').content)
    except:
        bookList = []

    return render_template('index.html', title = 'Titel', api = apiInfo, books = bookList)

# GET /books
@app.route('/books', methods=['GET'])
def books():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get('http://localhost:5000/books').content)
    except:
        bookList = []

    return render_template('books.html', title = 'Titel', api = apiInfo, books = bookList)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload
