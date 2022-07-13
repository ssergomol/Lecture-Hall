from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("home.html")

@views.route('/info')
def info():
    return render_template("info.html")

@views.route('/profile')
def profile():
    return render_template("profile.html")
