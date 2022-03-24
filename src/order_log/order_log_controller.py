from operator import ne
from config import db
from src.order_log.order_log_actions import LogActions
from src.order.order_actions import OrderActions

def log_new_order(order_num):
    new_order_log = OrderActions.get_order_by_order_number(order_num)
    get_previous_order_log_id = None
    #get_previous_order_log_id = LogActions.get_order_log_id(order_num) This query is returning a NoneType error
    previous_order_log_id = get_previous_order_log_id
    print(new_order_log.order_status_id)
    order_uuid = new_order_log.uuid
    order_number = new_order_log.order_number
    usa_state = new_order_log.usa_state
    home_office_code = new_order_log.home_office_code
    order_status_id = new_order_log.order_status_id
    new_log = LogActions.log(previous_order_log_id = previous_order_log_id, order_number = order_number, order_uuid = order_uuid, usa_state = usa_state, home_office_code = home_office_code, order_status_id = order_status_id)
    return new_log

def get_logs():
    order_logs = LogActions.get_all_logs()
    return order_logs

def get_all_order_logs_by_order_number(order_number):
    get_all_logs_by_order_number = LogActions.get_all_order_logs_by_order_number(order_number)
    return get_all_logs_by_order_number

def search_order_progress(order_number):
    #log order progress in sequentional order
    return 
