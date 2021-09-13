from app import app, db
from flask import render_template, url_for, flash, redirect

import models
import forms


# *********************************************************** Universities ****************************************************************
@app.route('/')
@app.route('/universities')
def universities():
    universities = models.University.query.all()
    return render_template('universities.html', universities=universities)


@app.route('/adduniversity', methods=['GET', 'POST'])
def adduniversity():
    form = forms.AddUniversityForm()
    if form.validate_on_submit():
        university = models.University(name=form.name.data, 
                                acronym=form.acronym.data, 
                                address=form.address.data,
                                location=form.location.data, 
                                )
        db.session.add(university)
        db.session.commit()
        flash('University added')
        return redirect(url_for('universities'))
    return render_template('add/adduniversity.html', form=form)


@app.route('/edit_university/<int:university_id>', methods=['GET', 'POST'])
def edit_university(university_id):
    form = forms.AddUniversityForm()
    university = models.University.query.get(university_id)
    print(university)
    if university:
        if form.validate_on_submit():
            university.name = form.name.data
            university.acronym = form.acronym.data
            university.address = form. address.data
            university.location = form.location.data

            db.session.commit()
            flash('University updated')
            return redirect(url_for('universities'))
        form.name.data = university.name
        form.acronym.data = university.acronym
        form.address.data = university.address
        form.location.data = university.location
        return render_template('edit/edit_university.html', form=form, university_id=university_id)
    flash(f'University with id {university_id} does not exit')
    return redirect(url_for('universities'))


@app.route('/delete_university/<int:university_id>', methods=['GET', 'POST'])
def delete_university(university_id):
    form = forms.DeleteForm()
    university = models.University.query.get(university_id)
    if university:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(university)
                db.session.commit()
                flash('University deleted')
            return redirect(url_for('universities'))
        return render_template('delete/delete_university.html', form=form, university_id=university_id, acronym=university.acronym)
    flash(f'University with id {university_id} does not exit')
    return redirect(url_for('universities'))


# *********************************************************** Colleges ****************************************************************
@app.route('/colleges')
def colleges():
    colleges = models.College.query.all()
    return render_template('colleges.html', colleges=colleges)


@app.route('/addcollege', methods=['GET', 'POST'])
def addcollege():
    form = forms.AddCollegeForm()
    if form.validate_on_submit():
        university = db.session.query(models.University).filter(models.University.name == form.university.data)[0]
        college = models.College(name=form.name.data, 
                                acronym=form.acronym.data, 
                                address=form.address.data,
                                location=form.location.data, 
                                university_id=university.id,
                                university=university
                                )
# add code to determine university id
        db.session.add(college)
        db.session.commit()
        flash('College added')
        return redirect(url_for('colleges'))
    return render_template('add/addcollege.html', form=form)


@app.route('/edit_college/<int:college_id>', methods=['GET', 'POST'])
def edit_college(college_id):
    form = forms.AddCollegeForm()
    college = models.College.query.get(college_id)
    print(college)
    if college:
        if form.validate_on_submit():
            university = db.session.query(models.University).filter(models.University.name == form.university.data)[0]
            college.name = form.name.data
            college.acronym = form.acronym.data
            college.address = form. address.data
            college.location = form.location.data
            college.university = university
            college.university_id = university.id

            db.session.commit()
            flash('College updated')
            return redirect(url_for('colleges'))
        form.name.data = college.name
        form.acronym.data = college.acronym
        form.university.data = college.university.name
        form.address.data = college.address
        form.location.data = college.location
        return render_template('edit/edit_college.html', form=form, college_id=college_id)
    flash(f'College with id {college_id} does not exit')
    return redirect(url_for('colleges'))


@app.route('/delete_college/<int:college_id>', methods=['GET', 'POST'])
def delete_college(college_id):
    form = forms.DeleteForm()
    college = models.College.query.get(college_id)
    if college:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(college)
                db.session.commit()
                flash('College deleted')
            return redirect(url_for('colleges'))
        return render_template('delete/delete_college.html', form=form, college_id=college_id, acronym=college.acronym)
    flash(f'College with id {college_id} does not exit')
    return redirect(url_for('colleges'))


# *********************************************************** Streams ****************************************************************
@app.route('/streams')
def streams():
    streams = models.Stream.query.all()
    return render_template('streams.html', streams=streams)


@app.route('/addstream', methods=['GET', 'POST'])
def addstream():
    form = forms.AddStreamForm()
    if form.validate_on_submit():
        college_id = db.session.query(models.College).filter(models.College.name == form.college.data)[0].id
        college = college=db.session.query(models.College).filter(models.College.name == form.college.data)[0]
        university_id=db.session.query(models.College).filter(models.College.id == college_id)[0].university_id
        university=db.session.query(models.University).filter(models.University.id == university_id)[0]
        stream = models.Stream(name=form.name.data,
                            college_id=college_id,
                            college=college,
                            university_id=university_id,
                            university=university
                            )
# add code to determine college and university id from college
        db.session.add(stream)
        db.session.commit()
        flash('Stream added')
        return redirect(url_for('streams'))
    return render_template('add/addstream.html', form=form)


@app.route('/edit_stream/<int:stream_id>', methods=['GET', 'POST'])
def edit_stream(stream_id):
    form = forms.AddStreamForm()
    stream = models.Stream.query.get(stream_id)
    print(stream)
    if stream:
        if form.validate_on_submit():
            college_id = db.session.query(models.College).filter(models.College.name == form.college.data)[0].id
            college = db.session.query(models.College).filter(models.College.name == form.college.data)[0]
            university_id = db.session.query(models.College).filter(models.College.id == college_id)[0].university_id
            university = db.session.query(models.University).filter(models.University.id == university_id)[0]
            stream.name = form.name.data
            stream.college_id = college_id
            stream.college = college
            stream.university_id = university_id
            stream.university = university

# add code to determine college and university ids from college
            db.session.commit()
            flash('Stream updated')
            return redirect(url_for('streams'))
        form.name.data = stream.name
        form.college.data = stream.college.name
        return render_template('edit/edit_stream.html', form=form, stream_id=stream_id)
    flash(f'Stream with id {stream_id} does not exit')
    return redirect(url_for('streams'))


@app.route('/delete_stream/<int:stream_id>', methods=['GET', 'POST'])
def delete_stream(stream_id):
    form = forms.DeleteForm()
    stream = models.Stream.query.get(stream_id)
    if stream:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(stream)
                db.session.commit()
                flash('Stream deleted')
            return redirect(url_for('streams'))
        return render_template('delete/delete_stream.html', form=form, stream_id=stream_id)
    flash(f'Stream with id {stream_id} does not exit')
    return redirect(url_for('streams'))


# *********************************************************** Courses ****************************************************************
@app.route('/courses')
def courses():
    courses = models.Course.query.all()
    return render_template('courses.html', courses=courses)


@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    form = forms.AddCourseForm()
    if form.validate_on_submit():
        college = db.session.query(models.College).filter(models.College.name == form.college.data)[0]
        college_id = college.id
        university_id = db.session.query(models.College).filter(models.College.id == college_id)[0].university_id
        university = db.session.query(models.University).filter(models.University.id == university_id)[0]
        stream = db.session.query(models.Stream).filter(
            models.Stream.name == form.stream.data and models.Stream.College_id==college_id)[0]
        stream_id = stream.id
        course = models.Course(name = form.name.data,
                            student_id = form.student_id.data,
                            grade = form.grade.data,
                            university_id=university_id,
                            college=college,
                            college_id=college_id,
                            stream=stream,
                            stream_id=stream_id
        )
# add code to determine marksheet form student id                            )
# add code to determine college, university and stream ids from college and stream
# add code to determine result: pass or fail
        db.session.add(course)
        db.session.commit()
        flash('Course added')
        return redirect(url_for('courses'))
    return render_template('add/addcourse.html', form=form)
    

@app.route('/edit_course/<int:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    form = forms.AddCourseForm()
    course = models.Course.query.get(course_id)
    print(course)
    if course:
        if form.validate_on_submit():
            college = db.session.query(models.College).filter(models.College.name == form.college.data)[0]
            college_id = college.id
            university_id = db.session.query(models.College).filter(models.College.id == college_id)[0].university_id
            university = db.session.query(models.University).filter(models.University.id == university_id)[0]
            stream = db.session.query(models.Stream).filter(
                models.Stream.name == form.stream.data and models.Stream.College_id==college_id)[0]
            course.name = form.name.data
            course.student_id = form.student_id.data
            course.grade = form.grade.data
            course.stream_id = stream.id
            course.stream = stream
            course.college_id = college.id
            course.college = college
            course.university_id = university.id
# add code to determine marksheet form student id
# add code to determine college, university and stream ids from college and stream
# add code to determine result: pass or fail
            db.session.commit()
            flash('Course updated')
            return redirect(url_for('courses'))
        form.name.data = course.name
        form.student_id.data = course.student_id
        form.grade.data = course.grade
        form.stream.data = course.stream.name
        form.college.data = course.college.name
        return render_template('edit/edit_course.html', form=form, course_id=course_id)
    flash(f'Course with id {course_id} does not exit')
    return redirect(url_for('courses'))


@app.route('/delete_course/<int:course_id>', methods=['GET', 'POST'])
def delete_course(course_id):
    form = forms.DeleteForm()
    course = models.Course.query.get(course_id)
    if course:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(course)
                db.session.commit()
                flash('Course deleted')
            return redirect(url_for('courses'))
        return render_template('delete/delete_course.html', form=form, course_id=course_id)
    flash(f'Course with id {course_id} does not exit')
    return redirect(url_for('courses'))


# # *********************************************************** MarkSheets ****************************************************************
# @app.route('/marksheets')
# def marksheets():
#     marksheets = models.Marksheet.query.all()
#     return render_template('marksheets.html', marksheets=marksheets)


# # add code to create a marksheet


# *********************************************************** Students ****************************************************************

@app.route('/students')
def students():
    students = models.Student.query.all()
    return render_template('students.html', students=students)


@app.route('/addstudent', methods=['GET', 'POST'])
def addstudent():
    form = forms.AddStudentForm()
    if form.validate_on_submit():
        stream = db.session.query(models.Stream).filter(models.Stream.name == form.stream.data)[0]
        college = db.session.query(models.College).filter(models.College.name == form.college.data)[0]
        university = db.session.query(models.University).filter(models.University.name == form.university.data)[0]
        student = models.Student(name=form.name.data, 
                                surname=form.surname.data,
                                address=form.address.data,
                                phone_no=form.phone_no.data,
                                std_code=form.std_code.data,
                                stream_id = stream.id,
                                stream = stream,
                                college_id = college.id,
                                college = college,
                                university_id = university.id,
                                university = university
                                )
# add code to determine college, university and stream ids
        db.session.add(student)
        db.session.commit()
        flash('Student added')
        return redirect(url_for('students'))
    return render_template('add/addstudent.html', form=form)


@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    form = forms.AddStudentForm()
    student = models.Student.query.get(student_id)
    print(student)
    if student:
        if form.validate_on_submit():
            stream = db.session.query(models.Stream).filter(models.Stream.name == form.stream.data)[0]
            college = db.session.query(models.College).filter(models.College.name == form.college.data)[0]
            university = db.session.query(models.University).filter(models.University.name == form.university.data)[0]
            student.name = form.name.data
            student.surname = form.surname.data
            student.address = form.address.data
            student.stream_id = stream.id
            student.stream = stream
            student.college_id = college.id
            student.college = college
            student.university_id = university.id
            student.university = university
            student.phone_n = form.phone_no.data
            student.std_code = form.std_code.data
# add code to determine college, university and stream ids
            db.session.commit()
            flash('Student updated')
            return redirect(url_for('students'))
        form.name.data = student.name
        form.surname.data = student.surname
        form.address.data = student.address       
        form.phone_no.data = student.phone_no
        form.std_code.data = student.std_code
        form.stream.data = student.stream.name
        form.college.data = student.college.name
        form.university.data = student.university.name
        return render_template('edit/edit_student.html', form=form, student_id=student_id)
    flash(f'Student with id {student_id} does not exit')
    return redirect(url_for('students'))


@app.route('/delete_student/<int:student_id>', methods=['GET', 'POST'])
def delete_student(student_id):
    form = forms.DeleteForm()
    student = models.Student.query.get(student_id)
    if student:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(student)
                db.session.commit()
                flash('Student deleted')
            return redirect(url_for('students'))
        return render_template('delete/delete_student.html', form=form, student_id=student_id, name=student.name, surname=student.surname)
    flash(f'Student with id {student_id} does not exit')
    return redirect(url_for('students'))
