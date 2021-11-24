import traceback
from datetime import datetime

from flask import jsonify
from werkzeug.exceptions import HTTPException

from config import flask_app


@flask_app.errorhandler(Exception)
def handle_exceptions_for_app(e: HTTPException):
    code = 500
    response = None
    if isinstance(e, HTTPException):
        code = e.code
        response = e.response
        print("Response", e.response)
    print("Code:", code)
    print(traceback.print_exc())
    print("Message:",str(e))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print()
    return jsonify(error=str(e)), code, response