import pytest
import random
from flask import request
from src.auth import auth_controller

from src.auth.auth_controller import get_current_user, set_authorize_current_user 
from src.auth.auth_privileges import check_is_admin
from src.user.user_controller import self_update_password
from src.user.user_actions import UserActions
from src.user.user_model import UserParams
from src.util import table_record_to_json

#How to set user for current session in test
#Will reseaerch JWT 
class TestUserControllers():
    def test_self_update_password():
        new_user_params = UserParams()

        new_user_params.username = "Test_Admin" + str(random.randint(1,1000))
        new_user_params.password = "1234"
        new_user_params.office_code = "AA-01"
        new_user_params.can_create_update_delete_orders = "Y"
        new_user_params.can_update_status_for = "self"
        new_user_params.can_update_password_for = "self"
        new_user_params.is_admin = "Y"
    
        new_user = UserActions.create(new_user_params)

        assert (True)
