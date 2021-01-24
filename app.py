from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#secret key was defined here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

#routes must be imported after Flask is instantiated
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
