from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')


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


class AddStreamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCourseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    stream = StringField('Stream', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    student_id = StringField('Student_ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddStudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone_no = StringField('Phone Number', validators=[DataRequired()])
    std_code = StringField('Std Code', validators=[DataRequired()])
    stream = StringField('Stream', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    university = StringField('University', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    search_target = StringField('What', validators=[DataRequired()])
    search_reference = StringField('How', validators=[DataRequired()])
    search_input = StringField('Input', validators=[DataRequired()])
    submit = SubmitField('Submit')
