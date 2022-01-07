import flask


def info():
    headers = flask.request.headers
    return "Request headers:\n" + str(headers)