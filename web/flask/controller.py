# TODO Exception handling API-calls (based on return codes op calls) 
from flask import Flask, render_template, jsonify, request, redirect, flash
import requests
from config import Config
from forms import EditBookForm, DeleteBookForm

app = Flask(__name__)

app.config.from_object(Config)

# TODO Error when page (or id) not found

# Globals
apiInfo = []

def getApiInfo():
    try:
        # Using eval to convert string to a dictionairy
        apiInfo = eval(requests.get(Config.API_ROOT_URL).content)
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
        bookList = eval(requests.get(Config.API_ROOT_URL + '/books').content)
    except:
        bookList = []

    nrOfBooks = len(bookList)  # Count books client-side

    for book in bookList:
        book['price'] = '%.2f' % book['price']  # Some formatting to obtain 2 decimals

    return render_template('books/list.html', appTitle = Config.APP_TITLE, api = apiInfo, books = bookList, 
        nrOfBooks = nrOfBooks)

# GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def detailsBook(id):
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
            'price': '%.2f' % book['price'],  # Two decimals
            'isbn': book['isbn']
        }    

    return render_template('books/details.html', actionTitle = 'Book details', appTitle = Config.APP_TITLE, api = apiInfo, book = orgBook)

# GET/POST /books/edit/<id>
@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def editBook(id):
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

    if request.method == 'GET':
        form.id.data = orgBook['id']
        form.name.data = orgBook['name']
        form.price.data = orgBook['price']
        form.isbn.data = orgBook['isbn']

    if request.method == 'POST' and form.validate():  # Equivalent to validate_on_submit()
        newName = request.form['name']
        newIsbn = request.form['isbn']
        newPrice = request.form['price']
   
        deltaBook = {}

        if newName.strip() != orgBook['name'].strip():
            deltaBook['name'] = newName
        if int(newIsbn) != int(orgBook['isbn']):  # Convert to float to have a precise comparison
            deltaBook['isbn'] = newIsbn
        if float(newPrice) != float(orgBook['price']):  # Convert to float to have a precise comparison
            deltaBook['price'] = newPrice

        if deltaBook <> {}:
            requests.patch(Config.API_ROOT_URL + '/books' + '/' + str(id), json = deltaBook)
            flash('Saved book {}'.format(deltaBook))
            
        return redirect('/books/' + str(id))     

    return render_template('books/edit.html', actionTitle = 'Edit book', appTitle = Config.APP_TITLE, api = apiInfo, book = orgBook, form = form)

# GET/POST /books/add
@app.route('/books/add', methods=['GET', 'POST'])
def addBook():
    global apiInfo

    orgBook = {
        'id': 0, 
        'name': "",
        'price': 0,
        'isbn': None
    }  

    form = EditBookForm()

    if request.method == 'GET':
        form.id.data = orgBook['id']
        form.name.data = orgBook['name']
        form.price.data = orgBook['price']
        form.isbn.data = orgBook['isbn']

    if request.method == 'POST' and form.validate():  # Equivalent to validate_on_submit()
        deltaBook = {}
        deltaBook['name'] = request.form['name']
        deltaBook['isbn'] = request.form['isbn']
        deltaBook['price'] = request.form['price']

        requests.post(Config.API_ROOT_URL + '/books', json = deltaBook)

        flash('Added book {}'.format(deltaBook))
        return redirect('/books')      

    return render_template('books/edit.html', actionTitle = 'Add book', appTitle = Config.APP_TITLE, api = apiInfo, book = orgBook, form = form)

# GET/POST /books/<id>
@app.route('/books/delete/<int:id>', methods=['GET', 'POST'])
def deleteBook(id):
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
            'name': book['name']
        }  

    form = DeleteBookForm()     

    if form.validate_on_submit():
        requests.delete(Config.API_ROOT_URL + '/books' + '/' + str(id))

        flash('Deleted book {}'.format(id))
        return redirect('/books')  

    return render_template('books/delete.html', actionTitle = 'Delete book', appTitle = Config.APP_TITLE, api = apiInfo, book = orgBook, form = form)

if __name__ == '__main__':
    apiInfo = getApiInfo()
    app.run(port=5001, debug=True)  # auto-reload, only localhoast
#    app.run(host='0.0.0.0', port=5001)  # public server, reachable from remote
