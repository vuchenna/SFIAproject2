from application import db


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value= db.Column(db.String(4), nullable=False, unique=True)

    def __repr__(self):
        return''.join([ 'Gender ID: ', str(self.id), '\r\n', 'Gender: ', self.value])

