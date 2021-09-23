from AuthActions import AuthActions
from config import app


@app.route("/signin", methods=["POST"])
def login_user():
    response = AuthActions.login_user()
    return response