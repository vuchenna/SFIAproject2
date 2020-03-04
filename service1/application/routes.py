from flask import render_template, request
from application import app, db
from application.models import Name, Gender
from application.forms import  GenerateForm

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', title='Home')
