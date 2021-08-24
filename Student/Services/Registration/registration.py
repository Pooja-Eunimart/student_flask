from Student.Models.student import Student
from Student import db, bcrypt
from flask_login import login_user,current_user,logout_user
from Student.Utils.errorhandler import handle_error

class Registration:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Registration, cls).__new(cls)
        return cls._instance

    @handle_error
    def signup(email,name,password):
        if current_user.is_authenticated:
            return {'message':'user already logged in '}
        else:
            hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
            student = Student(email=email,name=name,password=hashed_pass)
            db.session.add(student)
            db.session.commit()
            return {'message':'success'}

    @handle_error
    def login(e,password):
        if current_user.is_authenticated:
            return {'message':'user already logged in '}
        else:
            student=Student.query.filter_by(email=e).first()
        
            if(student and bcrypt.check_password_hash(student.password, password)):
                message={'message':'login successful'}
                login_user(student)
                return message
            else:
                message={'message':'user not found'}
                return message

    @handle_error
    def logout():
        if current_user.is_authenticated:
            logout_user()
            message={'message':'successfull logout'}
            
        else:
            message={'message':'No user is logged in'}
        return message