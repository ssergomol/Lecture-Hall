from . import db 
from flask_login import UserMixin 


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    title = db.Column(db.String(150))
    data = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    children = db.relationship('Section')
       
       
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    status = db.Column(db.String(150))
    rank = db.Column(db.Integer)
    sections = db.relationship('Section')