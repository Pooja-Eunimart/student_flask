from Student import app, schema
from flask import request
from Student.Services.EnrollCourse.enrollcourse import EnrollCourse
from Student.Routes.Schema.enrollcourse_schema import course_schema, update_course_schema
from flask_json_schema import JsonValidationError

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return ({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})

enrollCourse = EnrollCourse()

@app.route('/register_course',methods=['POST'])
@schema.validate(course_schema)
def register_course():
    return enrollCourse.register_course(request)

@app.route('/show_courses',methods=['GET'])
def show_courses():
    return enrollCourse.show_courses()

@app.route('/show_student',methods=['POST'])
@schema.validate(course_schema)
def show_student():
    return enrollCourse.show_student(request)

@app.route('/update_course',methods=['POST'])
@schema.validate(update_course_schema)
def update_course():
    return enrollCourse.update_course(request)

@app.route('/delete_course',methods=['POST'])
@schema.validate(course_schema)
def delete_course():
    return enrollCourse.delete_course(request)