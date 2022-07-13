from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("home.html", user=current_user)

@views.route('/info')
def info():
    return render_template("info.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)


# @views.route('/info/<pep>')
# def info_pep(pep):
#     print("\n\n\n", pep, "\n\n\n")
#     return render_template("info.html")