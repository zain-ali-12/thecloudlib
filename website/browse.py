from flask import Blueprint, render_template
from flask_login import login_required, current_user

browse = Blueprint("browse", __name__)

@browse.route("/by_user")
@login_required
def browse_by_user():
    postdata = current_user.posts[0]
    return render_template("browse.html", user=current_user, postdata=postdata)