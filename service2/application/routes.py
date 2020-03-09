from application import app, db
from application.models import Gender
#from application.forms import GenerateForm
import random,requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/gender', methods=['GET', 'POST'])
def gender():

    id = random.randint(0,2)
    #gender = Gender.query.filter_by(id=id).first()
    #g = str(gender.id)
    g = str(id)
    return g
   #return(selectgender)
