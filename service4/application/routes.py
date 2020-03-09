from application import app, db
import requests
from sqlalchemy import select

@app.route('/namegender', methods=['GET', 'POST'])
def namegender():
    if method =='POST':
        both = str(request.data.decode("UTF-8"))
        ls = both.split(",")
        gender =ls[0]
        first_letter=ls[1]
        response2 = requests.post('http://nameapp_service3_1:5000/name', both).text
        #response2 = requests.get('http://nameapp_service3_1:5000/name').text
        name = response2
        check = [name, gender]
        listToStr = ' '.join([str(elem) for elem in check])
    else:

        response = requests.get('http://nameapp_service2_1:5000/gender').text
        gender_genderid = int(response)
        list = ['Boy', 'Girl', 'Neutral']
        gender = list[gender_genderid]
        gender_genderid = str(response)

        response2 = requests.post('http://nameapp_service3_1:5000/name', gender_genderid).text
        #response2 = requests.get('http://nameapp_service3_1:5000/name').text
        name = response2
        check = [name, gender]
        listToStr = ' '.join([str(elem) for elem in check])
    return(listToStr)
