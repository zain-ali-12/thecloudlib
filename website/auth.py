from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User, db
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from .models import Subject, Qualification

auth = Blueprint("auth", __name__)


@auth.route("/sign-in", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        email = request.form.get("email").lower()
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user is not None:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Logged in!")
                return redirect(url_for("views.dashboard"))
            else:
                flash("Incorrect password")
        else:
            flash("Email does not exist")
        
        return render_template("sign_in.html") 


@auth.route("/forgot", methods=["GET", "POST"])
def forgot_password():
    return render_template("forgot_password.html")


@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("sign_up.html")
    elif request.method == "POST":
        email = request.form.get("email").lower()
        username = request.form.get("username")
        password = request.form.get("password")
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("This email already belongs to an account, do you wish to log in?", category="error")
        elif username_exists:
            flash("Username already taken", category="error")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("User created!")
            login_user(new_user, remember=True)
            return redirect(url_for("views.dashboard", user=new_user))
        return render_template("sign_up.html")


@auth.route("/edit-profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'GET':
        return render_template('edit_profile.html', user=current_user, subjects=Subject.query.all(), qualifications=Qualification.query.all())
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        role = request.form['role']
        qualification = request.form['qualification']
        subjects = request.form.getlist(['subject[]'])
        print(request.form.keys(), "  subject: ", request.form['subject[]'])
        return redirect(url_for("views.dashboard"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))

        
