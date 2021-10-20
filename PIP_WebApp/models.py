from app import db
from datetime import datetime


class University(db.Model):
    __tablename__ = "university"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    # relationships
    colleges = db.relationship(
        "College", back_populates="university", cascade="all,delete"
    )  # one2many
    students = db.relationship(
        "Student", back_populates="university", cascade="all,delete"
    )  # one2many
    streams = db.relationship(
        "Stream", back_populates="university", cascade="all,delete"
    )  # one2many

    def __repr__(self):
        return f"id = {self.id}: {self.name}, {self.created_at}"


class College(db.Model):
    __tablename__ = "college"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    # relationships
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"))  # many2one
    university = db.relationship("University", back_populates="colleges")
    students = db.relationship(
        "Student", back_populates="college", cascade="all,delete"
    )
    streams = db.relationship("Stream", back_populates="college", cascade="all,delete")
    courses = db.relationship("Course", back_populates="college", cascade="all,delete")

    def __repr__(self):
        return f"id = {self.id}: {self.name}, {self.created_at}"


class Stream(db.Model):
    __tablename__ = "stream"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    # relationships
    college_id = db.Column(db.Integer, db.ForeignKey("college.id"))  # many2one
    college = db.relationship("College", back_populates="streams")
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"))  # many2one
    university = db.relationship("University", back_populates="streams")
    courses = db.relationship(
        "Course", back_populates="stream", cascade="all,delete"
    )  # one2many
    students = db.relationship(
        "Student", back_populates="stream", cascade="all,delete"
    )  # one2many

    def __repr__(self):
        return f"id = {self.id}: {self.name}, {self.created_at}"


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    grade = db.Column(db.Float)
    result = db.Column(db.String(24))  # Pass or Fail
    # relationships
    college_id = db.Column(db.Integer, db.ForeignKey("college.id"))  # many2one
    college = db.relationship("College", back_populates="courses")
    stream_id = db.Column(db.Integer, db.ForeignKey("stream.id"))  # many2one
    stream = db.relationship("Stream", back_populates="courses")
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"))  # many2one
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))  # many2one
    student = db.relationship("Student", back_populates="courses")
    marksheet_id = db.Column(db.Integer, db.ForeignKey("marksheet.id"))  # many2one
    marksheet = db.relationship("Marksheet", back_populates="courses")

    def __repr__(self):
        return f"id = {self.id}: {self.name}, {self.created_at}"


class Marksheet(db.Model):
    __tablename__ = "marksheet"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    gpa = db.Column(db.Float)
    # relationships
    courses = db.relationship(
        "Course", back_populates="marksheet", cascade="all,delete"
    )  # one2many
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))  # one2one
    student = db.relationship("Student", back_populates="marksheets")

    def __repr__(self):
        return f"id = {self.id}: {self.student_id}, {self.created_at}"


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(10))
    std_code = db.Column(db.String(8))
    # relationships
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"))  # many2one
    university = db.relationship("University", back_populates="students")
    college_id = db.Column(db.Integer, db.ForeignKey("college.id"))  # many2one
    college = db.relationship("College", back_populates="students")
    stream_id = db.Column(db.Integer, db.ForeignKey("stream.id"))  # many2one
    stream = db.relationship("Stream", back_populates="students")
    courses = db.relationship(
        "Course", back_populates="student", cascade="all,delete"
    )  # one2many
    marksheets = db.relationship(
        "Marksheet", back_populates="student", cascade="all,delete"
    )  # one2many

    def __repr__(self):
        return f"id = {self.id}: {self.name} {self.surname}, {self.created_at}"
