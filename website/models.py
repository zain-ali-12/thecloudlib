from . import db
from flask_login import UserMixin
from sqlalchemy import func

user_subject = db.Table('user_subject',
    db.Column('user', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('subject', db.String(4), db.ForeignKey('subject.id'), primary_key=True)
)

subject_qualification = db.Table('subject_qualification',
    db.Column('qualification', db.String(15), db.ForeignKey('qualification.id'), primary_key=True),
    db.Column('subject', db.String(4), db.ForeignKey('subject.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    role = db.Column(db.String(100))
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    subjects = db.relationship('Subject', secondary=user_subject,  backref='user')


class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    resource_type = db.Column(db.String(200))
    topic = db.Column(db.String(200))
    title = db.Column(db.String(200))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    file_type = db.Column(db.String(10))
    feedback = db.relationship('Feedback', backref='post', passive_deletes=True)
    subject = db.Column(db.String(4), db.ForeignKey('subject.id', ondelete="CASCADE"), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


class Feedback(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(500))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


class Qualification(db.Model, UserMixin):
    id = db.Column(db.String(15), primary_key=True)


class Subject(db.Model, UserMixin):
    id = db.Column(db.String(4), primary_key=True)
    subject_name = db.Column(db.String(200))
    posts = db.relationship('Post', backref='Subject', passive_deletes=True)
    qualifications = db.relationship('Qualification', secondary=subject_qualification, backref='Subject')
