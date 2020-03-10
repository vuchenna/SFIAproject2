from application import app, db
import requests
from sqlalchemy import select

@app.route('/namegender', methods=['GET', 'POST'])
def namegender():
    response = requests.get('http://nameapp_service2_1:5000/gender').text
    gender_genderid = int(response)
    list = ['Boy', 'Girl', 'Neutral']
    gender = list[gender_genderid]
    gender_genderid = str(response)

    #response2 = requests.post('http://nameapp_service3_1:5000/name', gender_genderid).text
    response2 = requests.get('http://nameapp_service3_1:5000/name').text
    name = response2
    check = [name, gender]
    listToStr = ' '.join([str(elem) for elem in check])
    return(listToStr)


@app.route('/nameboy', methods=['GET', 'POST'])
def nameboy():
    response = requests.get('http://nameapp_service2_1:5000/gender/boy').text
    boy = str(response)
    #genderid = int(reponse)
    #list = ['Boy', 'Girl', 'Neutral']
    #gender = list[genderid]
    #genderid = str(response)

    response2 = requests.get('http://nameapp_service3_1:5000/namebyboy').text
    name =  response2
    check = [name, boy]
    listToStr = ' '.join([str(elem) for elem in check])
    return(listToStr)

@app.route('/namegirl', methods=['GET', 'POST'])
def namegirl():
    response = requests.get('http://nameapp_service2_1:5000/gender/girl').text
    girl = str(response)
    #genderid = int(reponse)
    #list = ['Boy', 'Girl', 'Neutral']
    #gender = list[genderid]
    #genderid = str(response)

    response2 = requests.get('http://nameapp_service3_1:5000/namebygirl').text
    name =  response2
#    check = [name,girl]
    check = str(name + ' ' + girl)
  #  listToStr = ' '.join([str(elem) for elem in check])
    return str(check)

