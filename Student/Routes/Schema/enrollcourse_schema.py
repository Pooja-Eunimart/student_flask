course_schema={
    'required':['courseName'],
    'properties':{
        'courseName':{'type':'string','required':'true'}
    }

}
update_course_schema={
    'required':['courseName','newCourse'],
    'properties':{
        'courseName':{'type':'string','required':'true'},
        'newCourse':{'type':'string', 'required':'true'}
    }

}