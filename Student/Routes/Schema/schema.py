from Student.Routes.EnrollCourse import register_course


signup_schema={
    'required':['email','name','password'],
    'properties':{
        'email':{'type':'string', 'required':'true'},
        'name':{'type':'string', 'required':'true'},
        'password':{'type':'string', 'required':'true'}
    }
}

login_schema={
    'required':['email','password'],
    'properties':{
        'email':{'type':'string', 'required':'true'},
        'password':{'type':'string','required':'true'}
    }
}

