from flask import Flask

app = Flask(__name__)
#in order to use csrf / forms you need a secret key
app.config['SECRET_KEY'] = 'secret-key13534+8761'

#routes must be imported after Flask is instantiated
from routes import *

if __name__ == '__main__':
    app.run(debug=True)