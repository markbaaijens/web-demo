from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

# GET /
@app.route('/', methods=['GET'])
def index():

    try:
        # Using eval to convert string to a dictionairy
        bookList = eval(requests.get('http://localhost:5000/books').content)
    except:
        bookList = []

    try:
        # Using eval to convert string to a dictionairy
        apiInfo = eval(requests.get('http://localhost:5000').content)
    except:
        apiInfo = []

    return render_template('index.html', title = 'Titel', api = apiInfo, books = bookList)

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # auto-reload
