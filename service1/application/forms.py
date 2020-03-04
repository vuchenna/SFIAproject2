from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtfirms.validators import DataRequired, Length,EqualTo,ValidationError


Class GenerateForm(FlaskForm):
    gender = SelectField('Boy or Girl?',
            validators [
                DataRequired()
            ], choices = [("BOY", "Boy"), ("GIRL", "Girl"), ("NONE", "None")]


    alphabet = SelectField('First Letter',
            validators [
            ], choices = [(
                "A", "A"),
                ("B", "B"),
                ("C", "C"),
                ("D", "D"),
                ("E", "E"),
                ("F", "F"),
                ("G", "G"),
                ("H", "H"),
                ("I", "I"),
                ("J", "J"),
                ("K", "K"),
                ("L", "L"),
                ("M", "M"),
                ("N", "N"),
                ("O", "O"),
                ("P", "P"),
                ("Q", "Q"),
                ("R", "R"),
                ("S", "S"),
                ("T", "T"),
                ("U", "U"),
                ("V", "V"),
                ("W", "W"),
                ("X", "X"),
                ("Y", "Y"),
                ("Z", "Z")])
    Submit = SubmitField("Generate")
