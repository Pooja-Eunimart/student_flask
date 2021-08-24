
from Student import db

from sqlalchemy.orm import backref
from enum import unique


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(20), nullable=False)
    student_idd = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __repr__(self):
        return f"Course('{self.course_name}')"
    