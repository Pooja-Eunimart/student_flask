from Student import db, login_manager
from sqlalchemy.orm import backref
from enum import unique
from flask_login import UserMixin

@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(int(student_id))

class Student(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', backref='students', lazy=True)

    def __repr__(self):
        return f"User('{self.email}','{self.name}')"
    
    