from app import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import models
import forms

# *********************************************************** Students ****************************************************************
@app.route('/')
@app.route('/students')
def students():
    students = models.Student.query.all()
    return render_template('students.html', students=students)


@app.route('/addstudent', methods=['GET', 'POST'])
def addstudent():
    form = forms.AddStudentForm()
    if form.validate_on_submit():
        student = models.Student(name=form.name.data, 
                                surname=form.surname.data, 
                                created_at=datetime.utcnow(),
                                address=form.address.data,
                                stream=form.stream.data,
                                phone_no=form.phone_no.data,
                                std_code=form.std_code.data,
                                college=form.college.data,
                                faculty=form.faculty.data,
                                )
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
            student.name = form.name.data
            student.surname = form.surname.data
            student.date = datetime.utcnow()
            student.address = form. address.data
            student.stream = form.stream.data
            student.phone_n = form.phone_no.data
            student.std_code = form.std_code.data
            student.college = form.college.data
            student.faculty = form.faculty.data
            db.session.commit()
            flash('Student updated')
            return redirect(url_for('students'))
        form.name.data = student.name
        form.surname.data = student.surname
        form.address.data = student.address
        form.stream.data = student.stream
        form.phone_no.data = student.phone_no
        form.std_code.data = student.std_code
        form.college.data = student.college
        form.faculty.data = student.faculty
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


# *********************************************************** Universities ****************************************************************
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
                                created_at=datetime.utcnow(),
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
            university.date = datetime.utcnow()
            university.address = form. address.data
            university.location = form.location.data

            db.session.commit()
            flash('University updated')
            return redirect(url_for('universities'))
        form.name.data = university.name
        form.acronym.data = university.acronym
        form. address.data = university.address
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
        college = models.College(name=form.name.data, 
                                acronym=form.acronym.data, 
                                created_at=datetime.utcnow(),
                                address=form.address.data,
                                location=form.location.data, 
                                university=form.university.data
                                )
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
            college.name = form.name.data
            college.acronym = form.acronym.data
            college.date = datetime.utcnow()
            college.address = form. address.data
            college.location = form.location.data
            college.university = form.university.data

            db.session.commit()
            flash('College updated')
            return redirect(url_for('colleges'))
        form.name.data = college.name
        form.acronym.data = college.acronym
        form.university.data = college.university
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


# *********************************************************** MarkSheet ****************************************************************
@app.route('/marksheets')
def marksheets():
    marksheets = models.Marksheet.query.all()
    return render_template('marksheets.html', marksheets=marksheets)


