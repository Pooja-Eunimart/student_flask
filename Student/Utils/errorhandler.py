from flask import jsonify

def handle_error(func):
    def handle(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as err:
            return jsonify("failed")
    handle.__name__ = func.__name__
    return handle