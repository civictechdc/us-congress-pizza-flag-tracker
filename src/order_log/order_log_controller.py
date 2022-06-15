from operator import ne
from config import db
from src.order_log.order_log_actions import LogActions
from src.order.order_actions import OrderActions
from src.util import table_to_json


def get_order_logs():
    order_logs = LogActions.get_all_order_logs()
    return {"orders": {"data": table_to_json(order_logs)}}


def get_all_order_logs_by_order_number(order_number):
    order_logs = LogActions.get_all_order_logs_by_order_number(order_number)
    return {"orders": {"data": table_to_json(order_logs)}}


def get_all_orders_by_order_uuid(uuid):
    order_logs = LogActions.get_all_order_logs_by_order_uuid(uuid)
    return {"orders": {"data": table_to_json(order_logs)}}


def get_sorted_order_log_by_order_number(order_number):
    order_logs = LogActions.sort_order_log_by_order_number(order_number)
    return {"orders": {"data": table_to_json(order_logs)}}
