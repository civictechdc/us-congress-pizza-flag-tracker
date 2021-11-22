def add_statuses(statuses_list, db):
    print("Adding statuses")
    from models import StatusModel
    for status in statuses_list:
        id = status["id"]
        status_federal_office_code = status["status_federal_office_code"]
        sequence_num = status["sequence_num"]
        description = status["description"]
        status = StatusModel(id,status_federal_office_code,sequence_num,description)
        db.session.add(status)

    db.session.commit()