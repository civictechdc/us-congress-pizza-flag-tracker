from xxlimited import new
from src.order_log import order_log_model
from src.order_log.order_log_model import OrderLogModel
from config import db
import uuid

class LogActions:
    @classmethod
    def create_order_log(cls, order_uuid, usa_state, order_number, home_office_code, order_status_id):
        previous_order_log_uuid = LogActions.get_order_log_uuid(order_number)
        order_log_count = LogActions.get_last_order_count(order_number)
        logUuid = str(uuid.uuid4())
        new_log = OrderLogModel(logUuid = logUuid, order_number = order_number, order_log_count = order_log_count, previous_order_log_uuid = previous_order_log_uuid, order_uuid = order_uuid, usa_state = usa_state, home_office_code =home_office_code, order_status_id= order_status_id)
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @classmethod
    def get_order_log_uuid(cls, order_number):
        order_logs = OrderLogModel.query.filter(OrderLogModel.order_number == order_number).all()
        current_order_log_uuid = None
        max_order_count = 0
        order_logs_len = len(order_logs)
        for order in order_logs:
            if order_logs_len == 1:
                current_order_log_uuid = order.uuid
            elif order.order_log_count > max_order_count:
                max_order_count = order.order_log_count
                current_order_log_uuid = order.uuid
        return current_order_log_uuid 

    @classmethod
    def get_last_order_count(cls, order_number):
        order_logs = OrderLogModel.query.filter(OrderLogModel.order_number == order_number).all()
        new_order_log_number = 1
        for order in order_logs:
            if not order_logs:
                return new_order_log_number
            elif order.order_log_count == 1 or order.order_log_count > 1:
                new_order_log_number += 1
        return new_order_log_number

    @classmethod
    def sort_order_log_by_order_number(order_number):
        order_logs = OrderLogModel.query.filter(OrderLogModel.order_number == order_number).all()
        order_logs_len = len(order_logs)
        for i in range(0, order_logs_len):
            for j in range (i + 1, order_logs_len):
                if order_logs[i] > order_logs[j]:
                    temp = order_logs[i]
                    order_logs[i] = order_logs[j]
                    order_logs[j] = temp
        return order_logs

    @classmethod
    def get_all_order_logs(cls):
        order_logs = OrderLogModel.query.all()
        return order_logs
    
    @classmethod
    def get_all_order_logs_by_order_number(cls, order_number):
        order_logs = OrderLogModel.query.filter(OrderLogModel.order_number==order_number).all()
        return order_logs

        