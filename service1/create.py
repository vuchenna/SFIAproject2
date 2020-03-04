from application.models import Name
import pandas as pd
from application import db

db.drop_all()
db.create_all()



data = pd.read_csv('../babynames.csv')
data.columns=['name','gender']

data2 = pd.read_csv('../bngender.csv')
data2.columns=['gender']

for index, row in data.iterrows():
    names = Name(babyname =row[0], gender=row[1])
    db.session.add(names)
for index, row in data2.iterrows():
    gender = Gender(gender = row[0])
    db.session.add(gender)
db.session.commit()

