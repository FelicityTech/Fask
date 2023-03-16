from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)

# Model


class Owner(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='owner')


class Pet(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
