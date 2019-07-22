from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("confirm Password", validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()



