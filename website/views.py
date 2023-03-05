from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Post, Subject, Qualification

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    print(current_user.is_authenticated)
    return render_template("home.html", user=current_user)


@views.route("/view")
@views.route("/view/<post_id>")
@login_required
def view_material():
    post_id = 0
    posts = Post.query.all()
    return render_template("view.html",user=current_user, post_id=post_id, posts=posts, subjects=Subject, qualifications=Qualification)

@views.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)
