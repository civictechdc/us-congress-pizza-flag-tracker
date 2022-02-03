import app
from config import flask_app

from src.auth.auth_controller import derive_token_from_username

# We set this flag as true to theoretically get more debug info from the test--if these tests fail without it, python will just throw an error, but of course we want to capture the error rather than just throw it.
flask_app.testing = True


class TestAuth:
    def test_orders(self):
        username = "FED-ADMIN"
        password = "FED-ADMIN-1010"
        token = derive_token_from_username(username)
        response = flask_app.test_client().get(
            "/api/orders",
            headers={"x-access-tokens": token},
            content_type="application/json",
        )
        assert response.status_code == 200

    def test_if_not_is_admin_cannot_add_user(self):
        username = "MA-01"
        token = derive_token_from_username(username)
        print("token:", token)
        response = flask_app.test_client().post(
            "/api/users/create",
            headers={
                "x-access-tokens": token,
                "Content-type": "application/json",
            },
            json={
                "username": "ASDFASDF001",
                "password": "ASDFASDF",
                "office_code": "MA-01",
                "is_admin": "N",
                "can_create_update_delete_orders": "N",
                "can_update_password_for": "SELF",
                "can_update_status_for": "MA-01",
            },
        )
        print("response:", response)
        assert response.status_code == 401
