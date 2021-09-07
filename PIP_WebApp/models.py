from app import db


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    #colleges = db.relationship('College', backref=db.backref("university"))
    #streams = db.relationship("Stream", backref=db.backref("university"))
    #students = db.relationship('Student', backref=db.backref("university"))

    def __repr__(self):
        return f'{self.name} {self.location}: {self.id}'


class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    #university_id = db.Column(db.String(255),  db.ForeignKey("university.id"))
    #students = db.relationship('Student', backref=db.backref("college"))
    #streams = db.relationship("Stream", backref=db.backref("college"))
    
    def __repr__(self):
        return f'{self.name} {self.university}: {self.id}'


class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    #college_id = db.Column(db.String(255),  db.ForeignKey("college.id"))
    #university_id = db.Column(db.String(255),  db.ForeignKey("university.id"))
    #students = db.relationship('Student', backref=db.backref("stream"))
    #courses = db.relationship('Course', backref=db.backref("stream"))

    def __repr__(self):
        return f'{self.name}: {self.id}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    stream = db.Column(db.String(255), nullable=False)
    phone_no = db.Column(db.String(10))
    std_code = db.Column(db.String(4))
    college = db.Column(db.String(255), nullable = False)
    faculty = db.Column(db.String(255), nullable = False)
    #marksheet = db.relationship('Marksheet', backref=db.backref("student"))
    #marksheet_id = db.Column(db.Integer, db.ForeignKey("marksheet.id"))
    #university_id = db.Column(db.String(255), db.ForeignKey("university.id"))
    #college_id = db.Column(db.String(255),  db.ForeignKey("college.id"))
    #stream_id = db.Column(db.String(255),  db.ForeignKey("stream.id"))

    #courses = db.relationship('Course', backref=db.backref("student"))
    


    def __repr__(self):
        return f'{self.name} {self.surname}: {self.id}'


class Marksheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255))
    student_surname = db.Column(db.String(255))
    gpa = db.Column(db.Float)
    semester = db.Column(db.Integer)
    # courses = db.relationship('courses', backref=db.backref("marksheet"))
    # student = db.relationship('Student', backref=db.backref("marksheet"))
    # student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    def __repr__(self):
        return f'{self.student_name} {self.student_surname}: {self.id}'


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    grade = db.Column(db.Float)
    result = db.Column(db.String(24)) # Pass or Fail
    # marksheet_id = db.Column(db.Integer, db.ForeignKey("marksheet.id"))

    def __repr__(self):
        return f'{self.name}: {self.id}'
