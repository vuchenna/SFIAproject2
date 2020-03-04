from application import db
from application.models import Gender
import pandas as pd

db.drop_all()
db.create_all()



data = pd.read_csv('../bngender2.csv')
print(data)

for index, row in data.iterrows():
    gender = Gender(value=row[0])
    db.session.add(gender)
db.session.commit()

