from app import db
from datetime import datetime


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
# relationships 
    colleges = db.relationship('College', backref='university')# one2many
    students = db.relationship('Student', backref='university')# one2many
    streams = db.relationship("Stream", backref='university')# one2many

    def __repr__(self):
        return f'id = {self.id}: {self.name}, {self.created_at}'


class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
# relationships
    university = db.Column(db.String(255), db.ForeignKey("university.name"))# many2one
    university_id = db.Column(db.Integer,  db.ForeignKey("university.id"))# many2one
    students = db.relationship('Student', backref='college')# one2many
    streams = db.relationship("Stream", backref='college')# one2many
    
    def __repr__(self):
        return f'id = {self.id}: {self.name}, {self.created_at}'


class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    name = db.Column(db.String(255))

# relationships
    college = db.Column(db.String(255), db.ForeignKey("college.name"))# many2one
    college_id = db.Column(db.Integer,  db.ForeignKey("college.id"))# many2one
    university_id = db.Column(db.Integer,  db.ForeignKey("university.id"))# many2one
    courses = db.relationship('Course', backref='stream')# one2many
    students = db.relationship('Student', backref='stream')# one2many

    def __repr__(self):
        return f'id = {self.id}: {self.name}, {self.created_at}'


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    grade = db.Column(db.Float)
    result = db.Column(db.String(24))# Pass or Fail
# relationships
    college = db.Column(db.String(255), db.ForeignKey("college.name"))# many2one
    college_id = db.Column(db.Integer,  db.ForeignKey("college.id"))# many2one
    stream = db.Column(db.String(255), db.ForeignKey("stream.name"))# many2one
    stream_id = db.Column(db.Integer,  db.ForeignKey("stream.id"))# many2one
    university_id = db.Column(db.Integer,  db.ForeignKey("university.id"))# many2one
    student_id = db.Column(db.String(255), db.ForeignKey("student.id"))# one2one
    marksheet_id = db.Column(db.Integer, db.ForeignKey("marksheet.id"))# one2one

    def __repr__(self):
        return f'id = {self.id}: {self.name}, {self.created_at}'


class Marksheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    gpa = db.Column(db.Float)
# relationships
    courses = db.relationship('Course', backref='marksheet')# one2many
    student_id = db.Column(db.Integer, db.ForeignKey("student.id")) # one2one

    def __repr__(self):
        return f'id = {self.id}: {self.student_id}, {self.created_at}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(10))
    std_code = db.Column(db.String(8))
# relationships
    marksheet_id = db.Column(db.Integer, db.ForeignKey("marksheet.id")) # one2one
    courses = db.relationship('Course', backref='student')# one2many
    university = db.Column(db.String(255), db.ForeignKey("university.name"))# many2one
    university_id = db.Column(db.Integer,  db.ForeignKey("university.id"))# many2one
    college = db.Column(db.String(255), db.ForeignKey("college.name"))# many2one
    college_id = db.Column(db.Integer,  db.ForeignKey("college.id"))# many2one
    stream = db.Column(db.String(255), db.ForeignKey("stream.name"))# many2one
    stream_id = db.Column(db.Integer,  db.ForeignKey("stream.id"))# many2one


    def __repr__(self):
        return f'id = {self.id}: {self.name} {self.surname}, {self.created_at}'
