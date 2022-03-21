import pytest
import random
from config import *
from src.user.user_actions import UserActions
from src.user.user_model import UserModel, UserParams


class TestUserActions():
    def test_update_user(self):
        new_user_params = UserParams()

        new_user_params.username = "Test_Admin" + str(random.randint(1,1000))
        new_user_params.password = "1234"
        new_user_params.office_code = "CA-01"
        new_user_params.manage_all_orders = "Y"
        new_user_params.update_all_statuses = "Y"
        new_user_params.view_all_orders = "Y"

        new_user_params.manage_all_users = "Y"
        new_user_params.manage_office_users = "Y"
        new_user_params.update_own_password = "Y"


        new_user_params.can_create_update_delete_orders = "Y"
        new_user_params.can_update_status_for = "self"
        new_user_params.can_update_password_for = "self"
        new_user_params.is_admin = "Y"
    
        new_user = UserActions.create(new_user_params)
        print('new user', new_user.username)

        new_user.office_code = "CA-02"
        new_user = UserActions.update_user(new_user)
        print('new user2', new_user.username)
    

        updated_user = UserActions.get_by_name(new_user.username)
        assert(updated_user.office_code == new_user.office_code)
