from application import app, db
from application.models import Name
import random, requests
from sqlalchemy import func, select
from flask import request

@app.route('/name', methods=['GET', 'POST'])
def name():
    response = requests.get('http://nameapp_service2_1:5000/gender').text

    gender_genderid = int(response)
    gender_genderid = gender_genderid +1

    if gender_genderid == 3:
        name = Name.query.order_by(func.random()).limit(1).first()
    else:
        name= Name.query.filter_by(genderno=gender_genderid).order_by(func.random()).limit(1).first()
 #       name= Name.query.order_by(func.random()).filter_by(id=gender_genderid).first()
   # check = [name.value, gender_genderid, gender]
    check = name.value
    return str(check)


@app.route('/namebyboy', methods = ['GET', 'POST'])
def namebyboy():
    #response = requests.get('http://nameapp_service2_1:5000/gender/boy').text
    boyid = 1

    #if boyid == 1:

    name = Name.query.filter_by(genderno=boyid).order_by(func.random()).limit(1).first()
    check = name.value
    return str(check)


@app.route('/namebygirl', methods = ['GET', 'POST'])
def namebygirl():
    girlid = 2
    name = Name.query.filter_by(genderno=girlid).order_by(func.random()).limit(1).first()
    check = name.value
    return str(check)
