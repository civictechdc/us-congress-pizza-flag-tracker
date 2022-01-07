import app
from config import flask_app

from src.auth.auth_controller import derive_token_from_username


class TestAuth:
    def test_orders(self):
        username = "FED-ADMIN"
        password = "FED-ADMIN-1010"
        token = derive_token_from_username(username)
        response = flask_app.test_client().get(
            '/api/orders',
            headers={"x-access-tokens": token},
            content_type='application/json',
        )
        assert response.status_code == 200

    def test_if_not_is_admin_cannot_add_user(self):
        username = "FED-AOC"
        token = derive_token_from_username(username)
        response = flask_app.test_client().post(
            '/api/users/create',
            headers={"x-access-tokens": token},
            content_type='application/json',
        )
        assert response.status_code == 401

