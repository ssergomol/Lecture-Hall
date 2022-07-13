from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Вход выполнен успешно!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Неверный пароль, попробуйте ещё раз', category='error')
        else:
            flash('Такого имени пользователя не существует', category='error')
    
    return render_template("log_in.html", user=current_user)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Такое имя пользователя уже существует', category='error')
        elif len(email) < 4:
            flash('Почта должна содержать более 3 символов', category='error')
        elif len(username) < 2:
            flash('Имя пользователя должно содержать более 1 символа', category='error')
        elif password1 != password2:
            flash('Пароли не совпадают', category='error')
        elif len(password1) < 7:
            flash('Пароль должен содержать более 7 символов', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'), status='Студент', rank=int(0))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Вы успешно зарегистрировались!')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
