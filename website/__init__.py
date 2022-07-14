from turtle import title
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "ucwewvelhvghs nldfgksgeorh"
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)
 
	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Section
 
	create_database(app)
	
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.login_message = "Выполните вход, чтобы получить доступ к странице"
	login_manager.login_message_category = "error"
	login_manager.init_app(app)
	
	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))
	return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        from .models import User, Section
        with app.app_context():
            new_section = Section(title="Лекции", parent_id=None, data=None, user_id=None)
            db.session.add(new_section)
            db.session.commit()
        print('Database created!')
