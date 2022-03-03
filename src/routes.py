from config import flask_app
from src import WebController
from src.user import user_controller
import src.auth.auth_controller as auth_controller
from src.order import order_controller
from src.office import office_controller
from src.status import status_controller

# add routes below®

routes = [
    ["/api", order_controller.index, "GET"],
    ["/api/orders/create", order_controller.create_order, "POST"],
    ["/api/orders", order_controller.get_orders, "GET"],
    ["/api/orders/<uuid>", order_controller.get_order_by_uuid, "GET"],
    ["/api/orders/<uuid>", order_controller.delete_order_by_uuid, "DELETE"],
    ["/api/order_num/<order_number>", order_controller.get_order_by_order_number, "GET"],
    ["/api/info", WebController.info, "GET"],
    ["/api/orders/<uuid>", order_controller.update_order, "PUT"],
    ["/api/scan/<uuid>", order_controller.update_order_status, "PUT"],
    ["/api/signin", auth_controller.login_user, "POST"],
    ["/api/users/get", user_controller.get_all_users, "GET"],
    ["/api/qrcode/<uuid>", order_controller.send_file_qrcode, "GET"],
    ["/api/states", office_controller.get_all_states, "GET"],
    ["/api/state_offices/<state>", office_controller.get_offices_by_state, "GET"],
    ["/api/statuses", status_controller.get_statuses, "GET"],
    ["/api/users/create", user_controller.create_user, "POST"],
    ["/api/users/self/update/password",user_controller.self_update_password,"POST"],
    ["/api/users/admin/update/password",user_controller.admin_update_password,"POST"],
]

for route in routes:
    flask_app.add_url_rule(route[0], view_func=route[1], methods=[route[2]])
