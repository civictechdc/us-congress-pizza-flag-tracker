from flask import render_template, request, send_file

from config import flask_app, qrcode, db
from src.log.log_actions import LogActions
from src.order.order_actions import OrderActions 
import io

def log_new_order(usa_state, idbased_order_number, home_office_code, order_status_id):
    log_order = LogActions.log(usa_state, idbased_order_number, home_office_code, order_status_id)
    return log_order

def update_order_log(order):
    log_update = LogActions.update(order)
    return

def get_logs():
    logs = LogActions.get_all_logs()
    return logs

def get_all_order_logs_by_order_number(order_number):
    return

def search_order_progress(order_number):
    return
