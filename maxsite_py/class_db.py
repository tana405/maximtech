from app import db, log_manager
from flask_login import UserMixin


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


class Users(db.Model, UserMixin):
    iden = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        pass


@log_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
