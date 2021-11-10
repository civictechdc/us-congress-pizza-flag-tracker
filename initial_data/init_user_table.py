

def init_user_table_state_users(office_codes_list, db):
    from models import UserParams # imported here to prevent circular reference
    from UserActions import UserActions # imported here to prevent circular reference

    state_office_codes_list = [
        offices for offices in office_codes_list if offices["usa_state"] != "FED"]

    for state_offices in state_office_codes_list:

        params = UserParams()
        params.can_update_password_for = "NONE"
        params.is_admin = "N"

        for office_code in state_offices["office_code"]:
            params.password = office_code + "-1010"

            params.username = office_code
            params.office_code = office_code
            params.can_update_status_for = office_code
            # UserActions.create(params)

            # Admin users
            params.username = office_code + "-ADMIN"
            params.password = office_code + "-ADMIN-1010"
            params.can_update_password_for = office_code
            UserActions.create(params)


def init_user_table_fed_users(users_list, db):
    from models import UserParams, UserModel
    for user in users_list:
        params = UserParams()

        params.username = user["username"]
        params.password = user["password"]
        params.office_code = user["office_code"]
        params.can_create_update_delete_orders = user["can_create_update_delete_orders"]
        params.can_update_status_for = user["can_update_status_for"]
        params.can_update_password_for = user["can_update_password_for"]
        params.is_admin = user["is_admin"]
        UserActions.create(params)
