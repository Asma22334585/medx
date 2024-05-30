from flask import Flask, render_template, request, bcrypt, session, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash
from models.user import USER
from models.doctor import DOCTOR
from models.engine import db_storage

app = Flask(__name__, template_folder='templates')



@app.route('/signup_user', methods=['GET', 'POST'])
def signup_user():
    if request.method == 'GET':
        return render_template('signup_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fullname = request.form.get('fullname')
        dob = request.form.get('dob')
        blood_group = request.form.get('blood_group')
        genotype = request.form.get('genotype')
        allergies = request.form.get('allergies')
        weight = request.form.get('weight')
        location = request.form.get('location')

        hashed_password = bcrypt.generate_password_hash(password)

        user = USER(username=username, password=hashed_password, fullname=fullname, dob=dob, blood_group=blood_group, genotype=genotype, allergies=allergies, weight=weight, location=location)
        user.new()
        save()
        return redirect(url_for('login'))

@app.route('/signup_doc', methods=['GET', 'POST'])
def signup_doc():
    if request.method == 'GET':
        return render_template('signup_doc.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        location = request.form.get('location')
        speciality = request.form.get('speciality')
        license = request.form.get('license')
        status = request.form.get('status')
        availability = request.form.get('availability')

        hashed_password = bcrypt.generate_password_hash(password)

        doctor = DOCTOR(username=username, password=hashed_password, fullname=fullname, email=email, location=location, speciality=speciality, license=license, status=status, availability=availability)
        doctor.new()
        save()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = USER.query.filter(USER.username == username).first()
        doctor = DOCTOR.query.filter(DOCTOR.username == username).first()

        if (bcrypt.check_password_hash(user.password, password)):
            login_user(user)
            return redirect(url_for('dash_usr.html'))

        if (bcrypt.check_password_hash(doctor.password, password)):
            login_user(doctor)
            return redirect(url_for('dash_doc.html'))

        if not user and not doctor:
            flash('Login failed')

@app.route('/logout')
def logout():
    logout_user()
    redirect(url_for('home'))