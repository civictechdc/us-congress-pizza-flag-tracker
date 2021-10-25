class mock_request:
    mock_request_json = {}

    @classmethod
    def get_json(cls):
        return mock_request.mock_request_json

