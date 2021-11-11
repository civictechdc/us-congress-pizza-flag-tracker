import pytest
import cv2
from io import BytesIO
# from qrtools.qrtools import QR
from app import flask_app
from OrderController import get_qrcode
import io
import numpy as np
from cachelib import file

from models import OrderModel, StatusModel
from util import table_record_to_json


class TestUtils():
    def test_table_record_to_json(self):
        order = OrderModel(1,"ma",1,"x","k")
        status = StatusModel(1,"x",1,"b")
        order.status = status
        t = table_record_to_json(order)
        print("t", t)


    @pytest.mark.skip(reason="function works, but test does not.  openCV is an issue, so may delete this test.")
    def test_qrcode(self):
        qrcodeValue = "https://example.com/A43X2Q3"
        # with app.test_client() as c:
        #     response = c.get('/qrcode?value=' + qrcodeValue)
        #     imgData = BytesIO(response.data)
        #     imgData.seek(0)
        #     data = np.fromstring(imgData.getvalue(), dtype=np.uint8)
        #     cv2Img = cv2.imdecode(data, 0)
        #     detector = cv2.QRCodeDetector()
        #     data, bbox, straight_qrcode = detector.detectAndDecode(cv2Img)
        #     assert data == qrcodeValue

   


