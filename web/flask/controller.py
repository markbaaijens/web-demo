# TODO Exception handling API-calls (based on return codes op calls) 
from flask import Flask, render_template, jsonify, request, redirect, flash
import requests
import json

from config import Config
from forms import EditBookForm, DeleteBookForm
from converters import ConvertToTwoDecimals, ConvertBooleanToText, ConvertEnumBookTypeToDescription
from model import Book

app = Flask(__name__)

app.config.from_object(Config)

# TODO Error when page (or id) not found

# Globals
apiInfo = []

def getApiInfo():
    try:
        # Using eval to convert string to a dictionairy
        apiInfo = json.loads(requests.get(Config.API_ROOT_URL).content)
        apiInfo.append({"url": Config.API_ROOT_URL})
    except:
        apiInfo = []

    return apiInfo

# GET /
@app.route('/', methods=['GET'])
def index():
    global apiInfo

    return render_template('index.html', appTitle = Config.APP_TITLE, api = apiInfo)

# GET /books
@app.route('/books', methods=['GET'])
def listBook():
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = json.loads(requests.get(Config.API_ROOT_URL + '/books').content)
    except:
        bookList = []

    nrOfBooks = len(bookList)  # Count books client-side

    # Some formatting 
    for book in bookList:
        book['price'] = ConvertToTwoDecimals(book['price'])
        book['obsolete'] = ConvertBooleanToText(book['obsolete'])
        book['bookType'] = ConvertEnumBookTypeToDescription(book['bookType'])

    return render_template('books/list.html', appTitle = Config.APP_TITLE, api = apiInfo, books = bookList, 
        nrOfBooks = nrOfBooks)

# GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def detailsBook(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = json.loads(requests.get(Config.API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []  

    for book in bookList:  
        # There is one and only one book
        orgBook = Book (
            book['id'], 
            book['name'],
            book['price'],  # Two decimals
            book['isbn'],
            book['obsolete'],
            book['bookType']
        )    

    orgBook.price = ConvertToTwoDecimals(orgBook.price)
    orgBook.obsolete = ConvertBooleanToText(orgBook.obsolete)
    orgBook.bookType = ConvertEnumBookTypeToDescription(orgBook.bookType)

    return render_template('books/details.html', actionTitle = 'Book details', appTitle = Config.APP_TITLE, api = apiInfo, book = vars(orgBook))

# GET/POST /books/edit/<id>
@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def editBook(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = json.loads(requests.get(Config.API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []  

    for book in bookList:  
        # There is one and only one book
        # TODO (bug) Converting this to Book objects result in unpredictable data result
        orgBook = {
            'id': book['id'], 
            'name': book['name'],
            'price': book['price'],
            'isbn': book['isbn'],
            'obsolete': book['obsolete'],
            'bookType': book['bookType']
        }  

    form = EditBookForm()

    if request.method == 'GET':
        form.id.data = orgBook['id']
        form.name.data = orgBook['name']
        form.price.data = orgBook['price']
        form.isbn.data = orgBook['isbn']
        form.obsolete.data = orgBook['obsolete']
        form.bookType.data = orgBook['bookType']

    if request.method == 'POST' and form.validate():  # Equivalent to validate_on_submit()
        newName = request.form['name']
        newIsbn = request.form['isbn']
        newPrice = request.form['price']
        newObsolete = form.obsolete.data  # TODO (bug) request.form['<booelan>'] does not return
        newBookType = request.form['bookType']
        deltaBook = {}

        if newName.strip() != orgBook['name'].strip():
            deltaBook['name'] = newName
        if int(newIsbn) != int(orgBook['isbn']):  # Convert to int to have a precise comparison
            deltaBook['isbn'] = newIsbn
        if float(newPrice) != float(orgBook['price']):  # Convert to float to have a precise comparison
            deltaBook['price'] = newPrice
        if newObsolete != orgBook['obsolete']: 
            deltaBook['obsolete'] = newObsolete
        if int(newBookType) != int(orgBook['bookType']):  # Convert to int to have a precise comparison
            deltaBook['bookType'] = newBookType

        if deltaBook <> {}:
            # TODO (bug) Error when doing the api-call
            requests.patch(Config.API_ROOT_URL + '/books' + '/' + str(id), json = deltaBook)
            flash('Saved book {}'.format(deltaBook))
            
        return redirect('/books/' + str(id))     

    return render_template('books/edit.html', actionTitle = 'Edit book', appTitle = Config.APP_TITLE, api = apiInfo, book = orgBook, form = form)

# GET/POST /books/add
@app.route('/books/add', methods=['GET', 'POST'])
def addBook():
    global apiInfo

    orgBook = Book()  

    form = EditBookForm()

    if request.method == 'GET':
        form.id.data = orgBook.id
        form.name.data = orgBook.name
        form.price.data = orgBook.price
        form.isbn.data = orgBook.isbn
        form.obsolete.data = orgBook.obsolete
        form.bookType.data = orgBook.bookType

    if request.method == 'POST' and form.validate():  # Equivalent to validate_on_submit()
        newBook = Book()
        newBook.name = request.form['name']
        newBook.isbn = request.form['isbn']
        newBook.price = request.form['price']
        newBook.obsolete = form.obsolete.data # TODO (bug) request.form['<booelan>'] does not return
        newBook.bookType = request.form['bookType']

        # TODO (bug) Error when doing the api-call
        requests.post(Config.API_ROOT_URL + '/books', json = vars(newBook))

        flash('Added book {}'.format(vars(newBook)))
        return redirect('/books')      

    return render_template('books/edit.html', actionTitle = 'Add book', appTitle = Config.APP_TITLE, api = apiInfo, book = vars(orgBook), form = form)

# DELETE /books/<id>
@app.route('/books/delete/<int:id>', methods=['GET', 'POST'])
def deleteBook(id):
    global apiInfo

    try:
        # Using eval to convert string to a dictionairy
        bookList = json.loads(requests.get(Config.API_ROOT_URL + '/books' + '/' + str(id)).content)
    except:
        bookList = []  

    for book in bookList:  
        # There is one and only one book
        orgBook = Book()
        orgBook.id = book['id'], 
        orgBook.name = book['name'],
        
    form = DeleteBookForm()     

    if form.validate_on_submit():
        requests.delete(Config.API_ROOT_URL + '/books' + '/' + str(id))

        flash('Deleted book id = {}'.format(id))
        return redirect('/books')  

    return render_template('books/delete.html', actionTitle = 'Delete book', appTitle = Config.APP_TITLE, api = apiInfo, book = vars(orgBook), form = form)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5001)  # public server, reachable from remote
