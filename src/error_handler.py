import json
import traceback
from datetime import datetime

from flask import jsonify
from werkzeug.exceptions import HTTPException

from config import flask_app

"""Called for unhandled exceptions.  Best practices: 
  - handle code exceptions by catching the exception, raising a new exception, and not handling the custom exception.  
  - handle error conditions (password does not match) by raising an exception and not handling the new exception.
  
Prints information about the error in the console for the server process and returns an http response.python

Unhandled exceptions can be:
 - explicity raised messages (raise ValueError("Must be a number").  In this case, e.code will correspond to the 
 specific value associated with ValueError and e.toString will be "Must be a number".  
 - code errors that are not handled, such as divide by zero and no data found if no exception handling.  See best 
 practices for avoiding this.  e.code and str(e) in these cases are determined by Python.

:param e: Explicit or implicit unhandled exception raised in code.  Key values for the exception are e.code and 
e.toString() (the string value of e).  See best practices for how to specify string value.
:returns An http response.  The response set back to the calling application will have the following values:
  - http_response.code derived based on exception raised.  
  - http_response.response.body.error_msg is set to the value of e.toString()
  - ==> NOTE: In JavaScript, json.stringify will not show the http_response.response attribute
"""


@flask_app.errorhandler(Exception)
def handle_exceptions_for_app(e: HTTPException):
    code = 500
    if e.code:
        code = e.code
    response_var = None
    if e.response:
        response_var["error_msg"] = str(e)
    else:
        response_var = {"error_msg": str(e)}
    print("Code:", code)
    print("Response: ", response_var)  
    print(traceback.print_exc())
    now = datetime.now()
    text_msg = json.dumps(response_var)
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print()
    return flask_app.response_class(
        response=response_var.err_message, status=code, mimetype="application/json"
    )
