from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(50), nullable=False)

    electives = db.relationship('UserElective', back_populates='user')
