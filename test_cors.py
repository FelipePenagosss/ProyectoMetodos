from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Flask-Cors is installed and working!"

if __name__ == '__main__':
    app.run(port=5013)
