from app import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import models
import forms

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
    return render_template('addstudent.html', form=form)


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
        form. address.data = student.address
        form.stream.data = student.stream
        form.phone_no.data = student.phone_no
        form.std_code.data = student.std_code
        form.college.data = student.college
        form.faculty.data = student.faculty
        return render_template('edit_student.html', form=form, student_id=student_id)
    flash(f'Student with id {student_id} does not exit')
    return redirect(url_for('students'))


@app.route('/delete/<int:student_id>', methods=['GET', 'POST'])
def delete(student_id):
    form = forms.DeleteTaskForm()
    student = models.Student.query.get(student_id)
    if student:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(student)
                db.session.commit()
                flash('Student deleted')
            return redirect(url_for('students'))
        return render_template('delete.html', form=form, student_id=student_id, name=student.name, surname=student.surname)
    flash(f'Student with id {student_id} does not exit')
    return redirect(url_for('students'))


@app.route('/universities')
def universities():
    universities = models.University.query.all()
    return render_template('university.html', universities=universities)


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
    return render_template('adduniversity.html', form=form)
