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
    password = PasswordField('Password', validators=[DataRequired(8)])
    role=RadioField('Role', choices=[('teacher','teacher'),('student','student')])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')


class AddNewBookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    #price = IntegerField('Price')
    #image= StringField('Image')
    author_name = IntegerField('Author Name')
    published_year= StringField('Published Year')
    upload = FileField("Please select an image to upload", validators=[InputRequired()])
    #file = FileField("File")
    submit = SubmitField('add_book')

class ItemForm(FlaskForm):
    book_id = HiddenField(validators=[DataRequired()])
    quantity = HiddenField(validators=[DataRequired()])

class CreateAssignmentForm(FlaskForm):
    student_ids=StringField('Student Id', validators=[DataRequired()])
    upload = FileField("Please select a file to upload", validators=[InputRequired()])
    maximum_marks=IntegerField('maximum marks')
    assignment_topic=StringField('Assignment Topic', validators=[DataRequired()])
    submit = SubmitField('Create Assignment')