def add_office_codes(office_codes_list, db):
    from models import OfficeModel
    for state_offices in office_codes_list:
        usa_state = state_offices["usa_state"]
        for office_code in state_offices["office_code"]:
            office = OfficeModel(usa_state, office_code)
            db.session.add(office)