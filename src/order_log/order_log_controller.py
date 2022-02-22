from flask import render_template, request, send_file

from config import flask_app, qrcode, db
from src.order_log.order_log_actions import LogActions
from src.order.order_actions import OrderActions 
import io

def get_logs():
    logs = LogActions.get_all_logs()
    return logs

def get_all_order_logs_by_order_number(order_number):
    return

def search_order_progress(order_number):
    return
