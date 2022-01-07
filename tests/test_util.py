import random

import pytest
# qrcode related imports

# import cv2
# from io import BytesIO
# # from qrtools.qrtools import QR
# from flask import json
# from app import flask_app
# from OrderController import get_qrcode
# import io
# import numpy as np

from cachelib import file

from src.order.order_actions import OrderActions
from src.status.status_actions import StatusActions

from src.status.status_model import StatusModel
from src.order.order_model import OrderModel
from src.util import table_record_to_json


class TestUtils():
    def test_table_record_to_json(self):
        unique_number = random.randint(1, 1000000)
        order_number = unique_number
        usa_state = "MA"
        order_statuses: [StatusModel] = StatusActions.get_statuses()
        order_status = order_statuses[0]
        home_office_code = "FED-ADMIN"
        order = OrderActions.create(order_number=order_number, usa_state=usa_state,
                                    home_office_code=home_office_code, order_status=order_status)
        json = table_record_to_json(order)
        assert (json["usa_state"] == order.usa_state)
        assert (json["status"]["description"] == order_status.description)

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
