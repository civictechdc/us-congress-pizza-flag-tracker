def init_office_table(office_codes_list,db):
    from models import OfficeModel
    for state_offices in office_codes_list:
        usa_state = state_offices["usa_state"]
        for office_code in state_offices["office_code"]:
            # TODO(tdk): we may not need uuids, discuss
            # theUuid = str(uuid.uuid4())
            office = OfficeModel(usa_state, office_code)
            db.session.add(office)