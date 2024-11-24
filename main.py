from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from app import db, app


class City(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True, nullable=False)
    Address = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        pass


class Excursion(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    FIO = db.Column(db.String(50), unique=True, nullable=False)
    Address = db.Column(db.String(60), unique=True, nullable=False)
    Phone = db.Column(db.String(15), unique=True, nullable=False)
    Class = db.Column(db.Integer, nullable=False)
    Count = db.Column(db.Integer, nullable=False)
    Data = db.Column(db.DateTime, unique=True, nullable=False)

    city_id = db.Column(db.Integer, db.ForeignKey('city.Id'), nullable=False)
    city = db.relationship('City', backref=db.backref('CityId'))

    def __repr__(self):
        pass


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


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


#@app.route('/api/city', method=["POST", "GET"])
#def get_city():
    #cities = City.query.all()


# '/add_excursion', method=["POST"]
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

