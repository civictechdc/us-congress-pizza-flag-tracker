import bcrypt
from util import get_http_response

from models import UserModel, UserParams
from util import table_record_to_json
from AuthController import get_token_with_username

class AuthActions:
    @classmethod
    def login_user(cls, username: str, password: str):
        user = UserModel.query.filter_by(username=username).first()
        if not user:
            return get_http_response("Invalid username.", 401)

        if not bcrypt.checkpw(password.encode(), user.password):
            return get_http_response("Invalid password.  Try logging in again.", 401)

        ret_val = table_record_to_json(user)
        ret_val["accessToken"] = get_token_with_username(user.username)
        return ret_val



