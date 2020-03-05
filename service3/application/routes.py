from application import app, db
from application.models import Name
import random, requests
from sqlalchemy import func, select

@app.route('/name', methods=['GET', 'POST'])
def name():

    gender_genderid = 1

    if gender_genderid == 3:
        name = Name.query.order_by(func.random()).limit(1).first()
    else:
        name= Name.query.filter_by(genderno=gender_genderid).order_by(func.random()).limit(1).first()
 #       name= Name.query.order_by(func.random()).filter_by(id=gender_genderid).first()

    return str(name.value)

