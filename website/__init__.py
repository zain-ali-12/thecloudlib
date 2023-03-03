from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "w-wH&nfO@@2D0Hd4)!q(A)xnvA7-jV*$p*k625$T@eu76Ts6cEQXu-@uq32y2O00iCfX)"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .auth import auth
    from .handle_posts import handle_posts
    from .views import views
    from .browse import browse
    app.register_blueprint(handle_posts, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(browse, url_prefix="/browse")

    from .models import User, Post

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.signin"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        with app.app_context():
            db.create_all()
        print("created database")
