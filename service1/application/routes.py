from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Users
from application.forms import RegistrationForm, LoginForm, GenerateForm
from flask_login import login_user, current_user, logout_user, login_required
import requests

@app.route('/')
@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html', title = 'view')


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = GenerateForm()
    if form.validate_on_submit():
        gender = form.gender.data
        first_letter = form.alphabet.data

        if gender == 'NONE' and first_letter == 'N/A':
            response=requests.get('http://nameapp_service4_1:5000/namegender').text
            responselist = response.split(' ')
            name = responselist[0]
            bgn = responselist[1]

            return render_template('home.html', title='Home', name=name,bgn=bgn, form=form)

        if gender == 'BOY' and first_letter == 'N/A':
            response=requests.get('http://nameapp_service4_1:5000/nameboy').text
            responselist = response.split(' ')
            name = responselist[0]
            bgn = responselist[1]

            return render_template('home.html', title='Home', name=name,bgn=bgn, form=form)

#            return response

            return render_template('home.html', title='Home', response=response,form=form)
        
        if gender == 'GIRL' and first_letter == 'N/A':
            response=requests.get('http://nameapp_service4_1:5000/namegirl').text
            responselist = response.split(' ')
            name = responselist[0]
            bgn = responselist[1]

            return render_template('home.html', title='Home', name=name, bgn=bgn, form=form)

#        form.submit.data = response
#        return(result)
#        response="%s"%(form.submit.data)
#            return response
    return render_template('home.html', title='Home', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        user = Users(first_name=form.first_name.data, last_name =form.last_name.data, email=form.email.data,  password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form=form)
