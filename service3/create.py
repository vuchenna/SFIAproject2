from application import db
from application.models import Name
import pandas as pd

db.drop_all()
db.create_all()

data = pd.read_csv('../babynames2.csv')
#print(data)

for index, row in data.iterrows():
    name = Name(value=row[0], genderno=row[1])
    db.session.add(name)

db.session.commit()
