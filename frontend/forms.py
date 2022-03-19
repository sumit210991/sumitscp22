from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, RadioField, FileField

from wtforms.validators import DataRequired, InputRequired
#from flask_wtf.file import FileField,FileRequired
#from flask_wtf.file import FileField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role=RadioField('Role', choices=[('teacher','teacher'),('student','student')])
    submit = SubmitField('Register')


class AddNewBookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    price = IntegerField('Price')
    image= StringField('Image')
    upload = FileField("Please select an image to upload", validators=[InputRequired()])
    #file = FileField("File")
    submit = SubmitField('add_book')

class ItemForm(FlaskForm):
    book_id = HiddenField(validators=[DataRequired()])
    quantity = HiddenField(validators=[DataRequired()])
