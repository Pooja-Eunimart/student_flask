import re
from Student import app, db, schema
from flask_json_schema import JsonValidationError
from flask import request
from Student.Services.Registration.registration import Registration
from Student.Routes.Schema.schema import signup_schema, login_schema

db.create_all()

registration=Registration()

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return ({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})



@app.route('/signup', methods=['POST'])
@schema.validate(signup_schema)
def signup():    
    request_data = request.get_json()
    email = request_data['email']
    name = request_data['name']
    password = request_data['password']
    return registration.signup(email,name,password)
    

@app.route('/login',methods=['POST'])
@schema.validate(login_schema)
def login():
    request_data=request.get_json()
    email=request_data['email']
    password=request_data['password']
    return registration.login(email,password)

@app.route('/logout')
def logout():
    return registration.logout()


