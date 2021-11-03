from config import flask_app

from tests.test_util import get_token


def test_orders():
    username = "FED-ADMIN"
    password = "FED-ADMIN-1010"
    token = get_token(password, username)
    response = flask_app.test_client().get(
        '/api/orders',
        headers={"x-access-tokens": token},
        content_type='application/json',
    )
    assert response.status_code == 200

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