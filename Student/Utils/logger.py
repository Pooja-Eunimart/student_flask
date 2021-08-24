import logging
from Student import app
from flask import request
logging.basicConfig(filename='data.log',level=logging.INFO)
log=logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.before_request 
def before_request_callback(): 
    logging.info(request.get_json())
    #print(request.json())

@app.after_request 
def after_request_callback( response ): 
    logging.info(response.get_data().decode("utf-8"))
    return response
