from photo_gallery_flask import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(1000000))


class metadata(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    sub_title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    uploaded_img = db.Column(db.LargeBinary)

    def __init__(self, title, sub_title, category, uploaded_img):
        self.title = title
        self.sub_title = sub_title
        self.category = category
        self.uploaded_img = uploaded_img
