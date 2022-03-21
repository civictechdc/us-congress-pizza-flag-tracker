

def add_state_office_users(office_codes_list, db):
    print("Adding office users and encrypting password")
    from src.user.user_model import UserParams  # imported here to prevent circular reference
    # imported here to prevent circular reference
    from src.user.user_actions import UserActions

    state_office_codes_list = [
        offices for offices in office_codes_list if offices["usa_state"] != "FED"]

    for state_offices in state_office_codes_list:

        params = UserParams()
        params.manage_all_orders = 'N'
        params.update_all_statuses = 'N'
        params.view_all_orders = 'N'
        params.manage_all_users = 'N'

        params.can_update_password_for = "NONE"
        params.can_create_update_delete_orders = "N"
        params.is_admin = "N"

        for office_code in state_offices["office_code"]:

            params.office_code = office_code

            # Non-admin users
            params.username = office_code
            params.manage_office_users = "N"
            params.update_own_password = "N"
            params.password = office_code + "-1010"
            params.can_update_status_for = office_code
            UserActions.create(params)

            # Admin users
            params.username = office_code + "-ADMIN"
            params.password = office_code + "-ADMIN-1010"
            params.manage_office_users = "N"
            params.update_own_password = "N"
            params.can_update_password_for = office_code
            UserActions.create(params)
        db.session.commit()

def add_fed_admin_user():
    from src.user.user_model import UserParams
    from src.user.user_actions import UserActions
    params = UserParams()
    params.username = "FED-ADMIN"
    params.password = "FED-ADMIN-1010"
    params.manage_all_users = "Y"
    params.manage_office_users = "Y"
    params.view_all_orders = "Y"
    params.manage_all_users = "Y"
    params.manage_office_users = "Y"
    params.update_own_password = "Y"
    params.can_update_password_for = "ALL"
    UserActions.create(params)


def add_fed_users(office_codes_list, db):
    print("Adding FED users and encrypting password")

    from src.user.user_model import UserParams
    from src.user.user_actions import UserActions
    add_fed_admin_user()
    for user in office_codes_list:

        params = UserParams()

        params.username = user["username"]
        params.password = params.username + "-1010"
        params.office_code = user["office_code"]
        params.manage_all_orders = user["manage_all_orders"]
        params.update_all_statuses = user["update_all_statuses"]
        params.view_all_orders = user["view_all_orders"]
        params.can_create_update_delete_orders = user["can_create_update_delete_orders"]
        params.can_update_status_for = user["can_update_status_for"]

        params.is_admin = "N"

        params.password = params.username + "-1010"
        params.manage_all_users = "N"
        params.manage_office_users = "N"
        params.update_own_password = "N"
        params.can_update_password_for = "N"
        UserActions.create(params)

        params.username = params.username + "-ADMIN"
        params.password = params.username + "-1010"
        params.manage_all_users = "N"
        params.manage_office_users = "Y"
        params.update_own_password = "Y"
        params.can_update_password_for = params.office_code
        UserActions.create(params)


    db.session.commit()

