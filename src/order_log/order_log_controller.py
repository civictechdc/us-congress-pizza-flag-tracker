from operator import ne
from config import db
from src.order_log.order_log_actions import LogActions
from src.order.order_actions import OrderActions
from src.util import table_to_json

def get_order_logs():
    order_logs = LogActions.get_all_order_logs()
    return {"orders":table_to_json(order_logs)}

def get_all_order_logs_by_order_number(order_number):
    order_logs = LogActions.get_all_order_logs_by_order_number(order_number)
    return {"orders": table_to_json(order_logs)}

def search_order_progress(order_number):
    #log order progress in sequentional order
    return 

