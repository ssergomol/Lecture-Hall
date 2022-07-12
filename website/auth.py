from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return render_template("log_in.html")

@auth.route('/signup')
def signup():
	return render_template("sign_up.html")