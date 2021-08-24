from flask import *
from flask_sqlalchemy import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_json_schema import JsonSchema
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:pooja@localhost/college'
app.config['SECRET_KEY'] = 'NJ234e56t7tfvhyi86t5r4e54678ijhbg'


schema = JsonSchema(app)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)


from Student.Routes import Registration, EnrollCourse
from Student.Utils import logger
