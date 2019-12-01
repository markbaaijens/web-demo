from flask import Flask, render_template, jsonify, request, redirect, flash
import requests
from config import Config
from forms import EditBookForm

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

    return render_template('index.html', title = 'Title', api = apiInfo, books = bookList)

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

    return render_template('books.html', title = 'Title', api = apiInfo, books = bookList, 
        nrOfBooks = nrOfBooks)

# GET/POST /books/<id>
@app.route('/books/<int:id>', methods=['GET', 'POST'])
def getBooksById(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get(Config.API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []  

    for book in bookList:  
        # There is one and only one book
        editBook = {
            'id': book['id'], 
            'name': book['name'],
            'price': book['price'],
            'isbn': book['isbn']
        }  

    form = EditBookForm()
    form.id.data = editBook['id']
    form.name.data = editBook['name']
    form.price.data = editBook['price']
    form.isbn.data = editBook['isbn']

    if request.method == 'POST':
        name=request.form['name']
        isbn=request.form['isbn']
        print(name + " " + isbn)
        flash('1 Save requested for book {}, id {}'.format(
            form.id.data, form.name.data))
        return redirect('/')      

    if form.validate_on_submit():
        flash('2 Save requested for book {}, id {}'.format(
            form.id.data, form.name.data))
        print('form.validate')
        return redirect('/')      

    return render_template('book.html', title = 'Title', api = apiInfo, book = editBook, 
        form = form)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5001)  # public server, reachable from remote
