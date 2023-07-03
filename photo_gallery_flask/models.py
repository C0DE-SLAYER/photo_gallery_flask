from photo_gallery_flask import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class metadata(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    sub_title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    photo_path = db.Column(db.String(500))
