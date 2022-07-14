from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Section
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
	parent = Section.query.filter_by(id=1).first()
	return render_template("home.html", user=current_user, parent_section=parent)

@views.route('/info')
def info():
	return render_template("info.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
	parent = Section.query.filter_by(id=1).first()
	return render_template("profile.html", user=current_user, parent_section=parent)

@views.route('/add_lecture', methods=['GET', 'POST'])
@login_required
def add_lecture():
	if request.method == 'POST':
		title = request.form.get('title')
		parent_title = request.form.get('parent-section')
		data = request.form.get('lecture-text')        
		
		section = Section.query.filter_by(title=title).first()
		parent_section = Section.query.filter_by(title=parent_title).first()
		
		if not (title and parent_title and data):
			flash('Заполните все поля', category='error')
		elif not parent_section:
			flash('Категории с таким названием не существует', category='error')
		elif section:
			flash('Документ c таким названием уже существует', category='error')
		elif len(data) < 1:
			flash('Документ должен содержать хотя бы 1 символ', category='error')
		else:
			new_section = Section(parent_id=parent_section.id, title=title, 
								  data=data, user_id=current_user.id)
			db.session.add(new_section)
			db.session.commit()
			flash('Новый документ успешно создан!', category='success')
			sections = Section.query.all()
			for section in sections:
				print(f'\n\n{section.id} {section.parent_id} {section.title} {section.data} {section.user_id}\n')
				print(f"{section.title} - Children: {section.children}\n\n")
			return redirect(url_for('views.profile'))

	parent = Section.query.filter_by(id=1).first()
	return render_template("add_lecture.html", user=current_user, parent_section=parent)

@views.route("/lectures/<id>", methods=['GET'])
def lectures(id):
    if int(id) == 1:
        return redirect(url_for("views.home"))
    parent = Section.query.filter_by(id=id).first()
    return render_template("lecture.html", user=current_user, parent_section=parent)
