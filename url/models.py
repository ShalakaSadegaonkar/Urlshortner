import datetime
from app import db


class Url(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    old = db.Column(db.String(2040))
    new = db.Column(db.String(5), unique=True)
