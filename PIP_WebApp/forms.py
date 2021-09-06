from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')


class AddStudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    stream = StringField('Stream', validators=[DataRequired()])
    phone_no = StringField('Phone Number', validators=[DataRequired()])
    std_code = StringField('Std Code', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    faculty = StringField('Faculty', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddUniversityForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    acronym = StringField('Acronym', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCollegeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    acronym = StringField('Acronym', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    university = StringField('University', validators=[DataRequired()])
    submit = SubmitField('Submit')
