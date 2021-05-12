import pytest
import cv2
from io import BytesIO
# from qrtools.qrtools import QR
from app import app
from controllers import get_qrcode
import io
import numpy as np
from cachelib import file
class TestUtils():
    def test_qrcode(self):
        qrcodeValue = "https://example.com/A43X2Q3"
        with app.test_client() as c:
            response = c.get('/qrcode?value=' + qrcodeValue)
            imgData = BytesIO(response.data)
            imgData.seek(0)
            data = np.fromstring(imgData.getvalue(), dtype=np.uint8)
            cv2Img = cv2.imdecode(data, 0)
            detector = cv2.QRCodeDetector()
            data, bbox, straight_qrcode = detector.detectAndDecode(cv2Img)
            assert data == qrcodeValue

   


