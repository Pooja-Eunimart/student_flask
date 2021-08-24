from Student import db
from Student.Models.course import Course
from flask_login import current_user
from Student.Utils.errorhandler import handle_error
class EnrollCourse:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnrollCourse, cls).__new(cls)
        return cls._instance
    @handle_error
    def register_course(request):
        request_data=request.get_json()
        course_name=request_data['courseName']
        if current_user.is_authenticated:
            course=Course(course_name=course_name,student_idd=current_user.id)
            db.session.add(course)
            db.session.commit()
            message={'message':'course registered successfully'}
        else:
            message={'message':'login needed'}
        return message
    
    @handle_error
    def show_courses():
        di={}
        if current_user.is_authenticated:
            course=current_user.courses
            
            if course:
                
                for c in course:
                    di[c.course_id]=c.course_name;

            else:
                di['message']='no courses found'
                
        else:
            di['message']='login needed'
        return di

    @handle_error
    def show_student(request):
        request_data=request.get_json()
        course_name=request_data['courseName']
        course=Course.query.filter_by(course_name=course_name).all()
        di={}
        if course : 
            l=[]
            for c in course:
                l.append(c.student_idd)
            di['message']='success'
            di[course_name]=l
            return di
        else:
            di['message']='no student found'
            return di
        
    @handle_error
    def update_course(request):
        message={}
        request_data=request.get_json()
        if(current_user.is_authenticated):
            course_name=request_data['courseName']
            course = Course.query.filter_by(course_name=course_name, student_idd=current_user.id).first()
            if course:
                course.course_name=request_data['newCourse']
                
                db.session.commit()
                message['message']='success'
            else:
                message['message']='no data found'
        else:
            message['message']='Login is needed to proceed'
        return message
    
    @handle_error
    def delete_course(request):
        message={}
        if current_user.is_authenticated:
            course=Course.query.filter_by(course_name=request.get_json()['courseName'], student_idd=current_user.id).first()
            if course:
                db.session.delete(course)
                db.session.commit()
                message['message']='success'
            else:
                message['message']='no data found'
        else:
            message['message']='Login needed'
        return message