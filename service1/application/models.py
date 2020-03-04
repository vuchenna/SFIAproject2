from application import db


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value=db.Column(db.String(10), nullable=False, unique=True)
    gender-id = db.Column(db.Integer, db.ForeignKey('gender.id'),nullable=False)

    def __repr__(self):
        return''.join([
            'Baby Name: ', self.value])

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value=(db.Column(db.String(4), nullable=False, unique=False)

    def __repr__(self):
        return''.join([
            'Gender: ', self.value])

