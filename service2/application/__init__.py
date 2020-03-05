from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('DATABASE_URI2')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY2')

db = SQLAlchemy(app)

from application import routes
