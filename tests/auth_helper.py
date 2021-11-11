import base64

from AuthActions import AuthActions

def get_token(username, password):
    login_response = AuthActions.login_user(username, password)
    user_pw_token = login_response["accessToken"].encode();
    return user_pw_token



