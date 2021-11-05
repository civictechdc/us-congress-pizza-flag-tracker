from config import flask_app
import WebController
import UserController
import AuthController
import OrderController
import OfficeController
import StatusController

# add routes below®
routes = [
    ["/api", OrderController.index, "GET"],
    ["/api/orders/create", OrderController.create_order, "POST"],
    ["/api/orders", OrderController.get_orders, "GET"],
    ["/api/orders/<uuid>", OrderController.get_order_by_uuid, "GET"],
    ["/api/order_num/<order_number>", OrderController.get_order_by_order_number, "GET"],
    ["/api/info", WebController.info, "GET"],
    ["/api/orders/<uuid>", OrderController.update_order, "PUT"],
    ["/api/login", AuthController.login_user, "POST"],
    ["/api/qrcode/<uuid>", OrderController.send_file_qrcode, "GET"],
    ["/api/states", OfficeController.get_all_states, "GET"],
    ["/api/state_offices/<state>",OfficeController.get_offices_by_state,"GET"],
    ["/api/statuses",StatusController.get_statuses,"GET"],
    ["/api/users/create", UserController.create_user, "POST"]
  ]

for route in routes:
    print ("route", route)
    flask_app.add_url_rule(route[0], view_func=route[1], methods=[route[2]])
    flask_app.add_url_rule