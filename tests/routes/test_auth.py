from config import flask_app

from  AuthController import get_token_from_request
class TestAuth:
    def test_orders(self):
        username = "FED-ADMIN"
        password = "FED-ADMIN-1010"
        token = get_token_from_request(username, password)
        response = flask_app.test_client().get(
            '/api/orders',
            headers={"x-access-tokens": token},
            content_type='application/json',
        )
        assert response.status_code == 200

    def test_if_not_is_admin_cannot_add_user(self):
        username = "FED-AOC"
        password = "FED-AOC-1010"
        token = get_token_from_request(username, password)
        response = flask_app.test_client().post(
            '/api/users/create',
            headers={"x-access-tokens": token},
            content_type='application/json',
        )
        assert response.status_code == 401
# import base64
# # from config2 import app
# from hello_add import app
# # import config
# # app2 = app.test_client()
#
# valid_credentials = base64.b64encode(b"FED-ADMINr:FED-ADMIN-1010").decode("utf-8")
# response = app.test_client().post(
#     "/add/"
#     # headers={"Authorization": "Basic " + valid_credentials}
# )
# print(response.__dict__)
# assert response.status_code == 200