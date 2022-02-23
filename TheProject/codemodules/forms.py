from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField,FileField,SelectField,EmailField
from wtforms.validators import DataRequired,EqualTo,Length,Email


class CreateUser(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired(),Length(max=120)])
    username = StringField('Username', validators = [DataRequired(),Length(min=4,max=20)])
    email = EmailField('Email address', validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired(),Length(min=8),EqualTo("password2",message="Password must match")])
    password2 = PasswordField("Confirm Password",validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    
class EditUser(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired(),Length(max=120)])
    username = StringField('Username', validators = [DataRequired(),Length(min=4,max=20)])
    email = StringField("Email",validators = [DataRequired(),Length(min=4,max=120)])
    bio = StringField("Bio",validators=[Length(min=10,max=400)])
    profile_picture = FileField("Your profile picture")
class addClothing(FlaskForm):
    types = ["hat","shirt","jacket","gloves","pants","shorts","shoes","socks"]
    type = SelectField(u'Field name', choices = types, validators = [DataRequired()])
    description = StringField("description")
    picture = FileField("Clothing picture",validators = [DataRequired()])