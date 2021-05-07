import pytest
import cv2
from io import BytesIO
# from qrtools.qrtools import QR
from app import app
from controllers import get_qrcode
import io
class TestUtils():
    def test_qrcode(self):
        qrcodeValue = "https://example.com/A43X2Q3"
        with app.test_client() as c:
            response = c.get('/qrcode?value=' + qrcodeValue)
            imgData = response.data
            img = BytesIO(imgData);            ## For sanity's sake
            with open("test.jpeg","wb") as f: ## Excel File
                f.write(img.getvalue())   ## Conversion to TextIOWrapper
            cv2Img = cv2.imread("test.jpeg")
            detector = cv2.QRCodeDetector()
            data, bbox, straight_qrcode = detector.detectAndDecode(cv2Img)
            assert data == qrcodeValue

   


