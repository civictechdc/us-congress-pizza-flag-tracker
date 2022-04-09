from werkzeug.exceptions import Unauthorized

from src.auth.auth_controller import get_current_user
from src.order.order_actions import OrderActions


def check_is_admin():
    if not is_admin():
        raise Unauthorized("Unauthorized.  Admin privileges required.")


def check_update_order_allowed():
    if not is_update_order_allowed():
        raise Unauthorized(
            "Unauthorized.  Create/update/delete order privileges required.")


def check_update_status_allowed(order: OrderActions):
    if not is_update_status_allowed(order):
        raise Unauthorized(
            "Unauthorized.  Update status privileges must be ALL or " + order.home_office_code)


def get_current_office():
    return get_current_user().office_code
    
def is_admin():
    return get_current_user().is_admin == "Y"


def is_logged_in():
    if not get_current_user():
        return False
    return True


def is_update_order_allowed():
    return get_current_user().can_create_update_delete_orders == "Y"


def is_update_status_allowed(order):
    return \
        get_current_user().can_update_status_for == "ALL" or \
        get_current_user().can_update_status_for == order.home_office_code
