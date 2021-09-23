from UserActions import UserActions
from config import app


@app.route("/signin", methods=["POST"])
def login_user():
    response = UserActions.login_user()
    return response