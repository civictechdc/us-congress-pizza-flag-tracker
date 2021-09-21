from flask import jsonify, request
# from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import app
from models import UserModel
import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "a valid token is missing"})
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = UserModel.query.filter_by(name=data["bane"]).first()
        except:
            return jsonify({"message": "token is invalid"})

        return f(current_user, *args, **kwargs)

    return decorator
