from application import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(20), nullable=False, unique=True)
    genderno = db.Column(db.Integer, nullable=False, unique=False)



    def __repr__(self):
        return''.join([ 'Baby Name: ',  self.value])

