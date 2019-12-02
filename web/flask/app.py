from flask import Flask, render_template, jsonify, request, redirect, flash
import requests
from config import Config
from forms import EditBookForm

app = Flask(__name__)

app.config.from_object(Config)

# TODO (api)/version instead of (api)/
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
        # TODO make use of a pre-defined class
        # There is one and only one book
        orgBook = {
            'id': book['id'], 
            'name': book['name'],
            'price': book['price'],
            'isbn': book['isbn']
        }  

    form = EditBookForm()
    form.id.data = orgBook['id']
    form.name.data = orgBook['name']
    form.price.data = orgBook['price']
    form.isbn.data = orgBook['isbn']

    if request.method == 'POST':
        newName = request.form['name']
        newIsbn = request.form['isbn']
        newPrice = request.form['price']
   
        updatedBook = {}

        if newName.strip() != orgBook['name'].strip():
            updatedBook['name'] = newName
        if str(newIsbn) != str(orgBook['isbn']):  # Convert numeric to string to have a precise comparison
            updatedBook['isbn'] = newIsbn
        if str(newPrice) != str(orgBook['price']):  # Convert numeric to string to have a precise comparison
            updatedBook['price'] = newPrice

        requests.patch(Config.API_ROOT_URL + '/books' + '/' + str(id), json = updatedBook)

        flash('Saved book {}'.format(updatedBook))
        return redirect('/books/' + str(id))      

    if form.validate_on_submit():
        # TODO Function validate_on_submit is never reached
        flash('Save requested for book {}, id {}'.format(
            form.id.data, form.name.data))
        return redirect('/books/' + str(id))   

    return render_template('book.html', title = 'Title', api = apiInfo, book = orgBook, form = form)

# GET/POST /books/addbook
@app.route('/books/addbook', methods=['GET', 'POST'])
def addBook():
    global apiInfo

    orgBook = {
        'id': 0, 
        'name': "",
        'price': 0,
        'isbn': None
    }  

    print(orgBook)

    form = EditBookForm()
    form.id.data = orgBook['id']
    form.name.data = orgBook['name']
    form.price.data = orgBook['price']
    form.isbn.data = orgBook['isbn']

    if request.method == 'POST':   
        updatedBook = {}
        updatedBook['name'] = request.form['name']
        updatedBook['isbn'] = request.form['isbn']
        updatedBook['price'] = request.form['price']

        requests.post(Config.API_ROOT_URL + '/books', json = updatedBook)

        flash('Added book {}'.format(updatedBook))
        return redirect('/books')      

    if form.validate_on_submit():
        # TODO Function validate_on_submit is never reached
        flash('Save requested for book {}, id {}'.format(
            form.id.data, form.name.data))
        return redirect('/books')

    return render_template('book.html', title = 'Title', api = apiInfo, book = orgBook, form = form)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5001)  # public server, reachable from remote
