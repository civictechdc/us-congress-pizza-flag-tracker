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

from OrderActions import OrderActions
from StatusActions import StatusActions

from models import OrderModel, StatusModel
from util import table_record_to_json


class TestUtils():
    def test_table_record_to_json(self):
        unique_number = random.randint(1, 1000000)
        order_number = unique_number
        usa_state = "MA"
<<<<<<< HEAD
        order_statuses: [StatusModel] = StatusActions.get_statuses()
        order_status = order_statuses[0]
        home_office_code = "FED-ADMIN"
        order = OrderActions.create(order_number=order_number, usa_state=usa_state,
                                    home_office_code=home_office_code, order_status=order_status)
        # description = "The first status"
        # active_status =
        # status = StatusModel(id=unique_number, status_federal_office_code="FED-ADMIN", sequence_num=unique_number,
        #                      description=description, active_status=active_status, status_code=status_code)
        # order.status = status
        json = table_record_to_json(order)
        assert (json["usa_state"] == order.usa_state)
        assert (json["status"]["description"] == order_status.description)
=======
        order_status_id = 1
        home_office_code = "FED-ADMIN"
        order = OrderActions.create(order_number=order_number, usa_state=usa_state,
                                    home_office_code=home_office_code,)
        description = "The first status"
        status = StatusModel(id=unique_number, status_federal_office_code="FED-ADMIN", sequence_num=unique_number,
                             description=description)
        order.status = status
        json = table_record_to_json(order)
        assert (json["usa_state"] == usa_state)
        assert (json["status"]["description"] == description)
>>>>>>> 66fd9f5 (rename order_status to order_status_id)

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
