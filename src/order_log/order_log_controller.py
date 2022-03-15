# from flask import render_template, request

from config import db
from src.order_log.order_log_actions import LogActions
# from src.order.order_actions import OrderActions 
# import io

def get_logs():
    order_logs = LogActions.get_all_logs()
    return order_logs

def get_all_order_logs_by_order_number(order_number):
    get_all_logs_by_order_number = LogActions.get_all_order_logs_by_order_number(order_number)
    return get_all_logs_by_order_number

def search_order_progress(order_number):
    #log order progress in sequentional order
    return 
