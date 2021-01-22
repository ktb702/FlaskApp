from flask import Flask

app = Flask(__name__)

#secret key was defined here

#routes must be imported after Flask is instantiated
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
