import json
import app
from config import flask_app

from src.auth.auth_controller import derive_token_from_username

# We set this flag as true to theoretically get more debug info from the test--if these tests fail without it, python will just throw an error, but of course we want to capture the error rather than just throw it.
flask_app.testing = True


class TestActiveQuery:
    def test_orders_active(self):
        username = "FED-ADMIN"
        token = derive_token_from_username(username)
        response = flask_app.test_client().get(
            "/api/orders?active=true&office_code=FED-MAIL",
            headers={"x-access-tokens": token},
            content_type="application/json",
        )
        statuses_found = {}

        parsed_responses = json.loads(response.data)["orders"]
        for parsed_response in parsed_responses:
            statuses_found[parsed_response["status"]["sequence_num"]] = True
        print("debug statuses found", statuses_found, parsed_responses)

        assert response.status_code == 200
