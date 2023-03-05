from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
from .models import Post
from . import db
from random import randint

handle_posts = Blueprint("handle_posts", __name__)


@handle_posts.route("/upload", methods=["GET", "POST"])
@login_required
def upload_file():
    if request.method == "GET":
        return render_template("upload.html", user=current_user)
    else:
        post_id = randint(1, 1000000000000000)
        while True:
            if Post.query.filter_by(id=post_id).first() is not None:
                post_id = randint(1, 1000000000000000)
                print(IndexError)
            else:
                break
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        subject = request.form.get("subject")
        resource_type = request.form.get("resource_type")
        topic = request.form.get("topic")
        title = request.form.get("title")
        file_type = file.filename.split('.')[1]
        new_post = Post(id=post_id, subject=subject, resource_type=resource_type, topic=topic, title=title,
                        file_type=file_type, author=current_user.id)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(f"website/static/media/content/posts/{post_id}.{file.filename.split('.')[1]}")
            file.save(filename.replace("_", "/"))
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('views.dashboard'))
