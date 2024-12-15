from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import app
from class_db import *


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/logging', methods=["GET"])
def logging():

    return render_template('logging.html')


@app.route('/contacts', methods=["GET"])
def contacts():
    return render_template('contacts.html')


@app.route('/excursion', methods=["GET"])
def excursion():
    return render_template('excursion.html', messages=Excursion.query.all())


@app.route('/school', methods=["GET"])
def school():
    return render_template('school.html')


@app.route('/student', methods=["GET"])
def student():
    return render_template('student.html')


#авторизация
@app.route('/login', methods=["GET", "POST"])
def login_page():
    return render_template('logging.html')


@app.route('/logout', methods=["GET", "POST"])
def logout():
    # login = request.form.get('login')
    # password = request.form.get('password')
    #
    # if login and password:
    #     user = Users.query.filter_by(login=login).first()
    #
    #     if user and check_password_hash(user.password, password):
    #         login_user(user)
    #
    #         next_page = request.args.get('next')
    #
    #         return redirect(next_page)
    #     else:
    #         flash('Login or password is not correct')
    # else:
    #     flash('Please fill login and password fields')
    pass



#@app.route('/api/city', method=["POST", "GET"])
#def get_city():
    #cities = City.query.all()


def add_excursion():
    id = request.form['Id']
    fio = request.form['FIO']
    address = request.form['Address']
    phone = request.form['Phone']
    xclass = request.form['Class']
    count = request.form['Count']
    date = request.form['Data']

    db.session.add(Excursion(id, fio, address, phone, xclass, count, date))
    db.session.commit()

    # return redirect(url_for('main'))


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
