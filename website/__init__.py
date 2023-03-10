from flask import Flask, render_template
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

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    from .auth import auth
    from .handle_posts import handle_posts
    from .views import views
    from .browse import browse
    app.register_blueprint(handle_posts, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(browse, url_prefix="/browse")
    app.add_template_filter(str)
    app.add_template_filter(len)

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
    if not path.exists(f"instance/{DB_NAME}"):
        with app.app_context():
            db.create_all()
            update_qualifications(app, db)
            update_subjects(app, db)
            # from .init_db import update_qualifications
            # update_qualifications(app, db)
        print("created database")


def update_qualifications(app, db):
    from .models import Qualification
    quals = ['IGCSE', "AS-Level", "A-Level"]
    with app.app_context():
        for i in quals:
            db.session.add(Qualification(id=i))
            db.session.commit()


def update_subjects(app, db):
    from .models import Subject, Qualification
    with open('subs.csv', 'r') as f:
        csv_data = [data[:-1] for data in f.readlines()][1:]
        for data in csv_data:
            subject_id, subject_name, qualification = data.split(",")
            new_subject = Subject(id=subject_id, subject_name=subject_name)
            # with app.app_context():
            db.session.add(new_subject)
            db.session.commit()
            for qual in qualification.split(" "):
                new_subject.qualifications.append(Qualification.query.filter_by(id=qual).first())
                db.session.commit()
