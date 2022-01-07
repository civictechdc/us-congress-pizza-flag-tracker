from config import flask_app
import WebController
import UserController
import src.auth.auth_controller as auth_controller
import OrderController
import OfficeController
import StatusController

# add routes below®

routes = [
    ["/api", OrderController.index, "GET"],
    ["/api/orders/create", OrderController.create_order, "POST"],
    ["/api/orders", OrderController.get_orders, "GET"],
    ["/api/orders/<uuid>", OrderController.get_order_by_uuid, "GET"],
    ["/api/orders/<uuid>", OrderController.delete_order_by_uuid, "DELETE"],
    ["/api/order_num/<order_number>", OrderController.get_order_by_order_number, "GET"],
    ["/api/info", WebController.info, "GET"],
    ["/api/orders/<uuid>", OrderController.update_order, "PUT"],
    ["/api/scan/<uuid>", OrderController.update_order_status, "PUT"],
    ["/api/signin", auth_controller.login_user, "POST"],
    ["/api/qrcode/<uuid>", OrderController.send_file_qrcode, "GET"],
    ["/api/states", OfficeController.get_all_states, "GET"],
    ["/api/state_offices/<state>", OfficeController.get_offices_by_state, "GET"],
    ["/api/statuses", StatusController.get_statuses, "GET"],
    ["/api/users/create", UserController.create_user, "POST"],
]

for route in routes:
    flask_app.add_url_rule(route[0], view_func=route[1], methods=[route[2]])
