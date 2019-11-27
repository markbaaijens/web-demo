from flask import Flask

app = Flask(__name__)

# GET /
@app.route('/', methods=['GET'])
def root():
    return "Hello world"

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # auto-reload
