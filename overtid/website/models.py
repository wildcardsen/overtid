from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    notes = db.relationship('Note')
    user_Time = db.relationship('UserTime')
    project_Type = db.relationship('ProjectType')


class UserTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    start_time = db.Column(db.DateTime(timezone=True), default=func.now())
    end_time = db.Column(db.DateTime(timezone=True), default=func.now())
    project_type = db.Column(db.Integer, db.ForeignKey('projectType.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class ProjectType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectType = db.Column(db.String(150))
    creationDate = db.Column(db.DateTime(timezone=True), default=func.now())
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    lastModified = db.Column(db.DateTime(timezone=True), default=func.now())
    lastModifier = db.Column(db.Integer, db.ForeignKey('user.id'))
    startDate = db.Column(db.DateTime(timezone=True), default=func.now())
    endDate = db.Column(db.DateTime(timezone=True), default=func.now())
    user_Time1 = db.relationship('UserTime')
