from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from application.models import Users
from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )

    password = PasswordField('Password',
            validators=[
                DataRequired()

            ]
        )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AddForm(FlaskForm):
    gender = StringField('gender',
            validators=[
                DataRequired(),
                Length(min=3, max=4)
            ]
        )
    name = StringField('name',
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ])


class RegistrationForm(FlaskForm):

    first_name = StringField('First Name',
            validators=[
                DataRequired(),
                Length(min=2,max=30)
            ])
    last_name = StringField('Last Name',
            validators=[
                DataRequired(),
                Length(min=3, max=30)
            ])



    email = StringField('Email',
            validators = [
               DataRequired(),
                Email()
            ]
        )
    password = PasswordField('Password',
            validators = [
                DataRequired(),
            ]
        )

    confirm_password = PasswordField('Confirm Password',
            validators = [
                DataRequired(),
                EqualTo('password')
            ]
        )

    submit = SubmitField('Sign Up')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')




class GenerateForm(FlaskForm):
    gender = SelectField('Boy or Girl?',
            validators=[
                DataRequired()
            ], choices = [("BOY", "Boy"), ("GIRL", "Girl"), ("NONE", "None")], default="NONE")

    alphabet = SelectField('First Letter',choices = [
                   ("N/A", "N/A"),
                    ("A", "A"),
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
                    ("Z", "Z")], default="N/A")
    submit = SubmitField("Generate")
