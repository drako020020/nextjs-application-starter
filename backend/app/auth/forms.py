from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(Form):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])

class LoginForm(Form):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
