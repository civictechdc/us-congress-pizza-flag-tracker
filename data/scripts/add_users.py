

def add_state_office_users(office_codes_list, db):
    print("Adding office users and encrypting password")
    from src.user.user_model import UserParams  # imported here to prevent circular reference
    # imported here to prevent circular reference
    from src.user.user_actions import UserActions

    state_office_codes_list = [
        offices for offices in office_codes_list if offices["usa_state"] != "FED"]

    for state_offices in state_office_codes_list:

        params = UserParams()
        params.can_update_password_for = "NONE"
        params.can_create_update_delete_orders = "N"
        params.is_admin = "N"

        for office_code in state_offices["office_code"]:
            params.password = office_code + "-1010"

            params.username = office_code
            params.office_code = office_code
            params.can_update_status_for = office_code
            UserActions.create(params)

            # Admin users
            params.username = office_code + "-ADMIN"
            params.password = office_code + "-ADMIN-1010"
            params.can_update_password_for = office_code
            UserActions.create(params)
        db.session.commit()

def add_fed_users(users_list, db):
    print("Adding FED users and encrypting password")

    from src.user.user_model import UserParams
    from src.user.user_actions import UserActions
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

    db.session.commit()

