import pytest

class TestUtils():
    # Create test that `Util.getQRCode('any_string')`
    # # returns PNG for the qr code from 
    # `?root_url:/show/any_string` route
    #  (we can build on early Feb experiment)
    def test_qrcode(self):
        # https://stackoverflow.com/questions/26363613/how-to-test-send-file-flask
        with open(self.dir + '/img/wikipedia.png', 'rb') as img1:
        img1StringIO = BytesIO(img1.read())

    response = self.app.post('/qrcode',
                             content_type='multipart/form-data',
                             data={'photo': (img1StringIO, 'img1.jpg')},
                             follow_redirects=True)
    img1StringIO.seek(0)
    assert response.data == imgStringIO.read()