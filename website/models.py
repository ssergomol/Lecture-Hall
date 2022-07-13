from . import db 
from flask_login import UserMixin 


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(150))
    data = db.Column(db.String(100000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    status = db.Column(db.String(150))
    rank = db.Column(db.Integer)