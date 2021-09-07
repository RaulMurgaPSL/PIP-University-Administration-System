from app import db


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    # streams relation one2many
    # colleges relation one2many

    def __repr__(self):
        return f'{self.name} {self.location}: {self.id}'


class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    acronym = db.Column(db.String(255))
    address = db.Column(db.String(255))
    university = db.Column(db.String(255))
    # streams relation one2many
    # students relation one2many
    
    def __repr__(self):
        return f'{self.name} {self.university}: {self.id}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable = False)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    stream = db.Column(db.String(255), nullable=False)
    phone_no = db.Column(db.String(10))
    std_code = db.Column(db.String(4))
    #marksheet_id = db.Column(db.Integer, nullable=False) Foreign key
    college = db.Column(db.String(255), nullable = False)
    faculty = db.Column(db.String(255), nullable = False)

    def __repr__(self):
        return f'{self.name} {self.surname}: {self.id}'


class Marksheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255))
    student_surname = db.Column(db.String(255))
    gpa = db.Column(db.Float)
    result = db.Column(db.String(24)) # Pass or Fail
    semester = db.Column(db.Integer)
    # student_id (foreign key)


class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # college_id foregin key


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    grade = db.Column(db.Float)
    # marksheet_id foregin key