from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Publication(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(150))
	path = db.Column(db.String(512))
	text = db.Column(db.String(100000))
	imgs = db.Column(db.String(100000))
	date = db.Column(db.DateTime(timezone=True), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	username = db.Column(db.String(150))
	status = db.Column(db.Integer)  ## 0 - admin, 1 - teacher, 2 - student
	publications = db.relationship('Publication')
		