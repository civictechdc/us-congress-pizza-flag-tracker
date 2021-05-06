import pytest
from io import BytesIO
# from qrtools.qrtools import QR
from controllers import get_qrcode
# class TestUtils():
#     # Create test that `Util.getQRCode('any_string')`
#     # # returns PNG for the qr code from 
#     # `?root_url:/show/any_string` route
#     #  (we can build on early Feb experiment)
#     def test_qrcode(self):
#         # https://stackoverflow.com/questions/26363613/how-to-test-send-file-flask
#         with open('/Users/ethanstrominger/projects/us-congress-pizza-flag-tracker/tests' + '/img/wikipedia.png', 'rb') as img1:
#             img1StringIO = BytesIO(img1.read())

#         response = self.app.psost('/qrcode',
#                              content_type='multipart/form-data',
#                              data={'photo': (img1StringIO, 'img1.jpg')},
#                              follow_redirects=True)
#         img1StringIO.seek(0)
#         assert response.data == imgStringIO.read()

class TestUtils():
    pass
    # Create test that `Util.getQRCode('any_string')`
    # returns PNG for the qr code from 
    # `?root_url:/show/any_string` route
    #  (we can build on early Feb experiment)
    # data = 'team-work'
    # pngFile = get_qrcode(data)
    # print("jhello",print(type(pngFile)))
    # print(pngFile)
    # temporarylocation="testout.png"
    # with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
    #     out.write(pngFile.read())                ## Read bytes into file
    # qr = qrtools.QR()
    # my_QR = qr.decode(temporarylocation)
   
   


