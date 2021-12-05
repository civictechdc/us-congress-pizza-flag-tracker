def add_statuses(statuses_list, db):
    print("Adding statuses")
    from models import StatusModel
    for status in statuses_list:
        id = status["id"]
        sequence_num = status["sequence_num"]
        description = status["description"]
        active_status = status["active_status"]
        status_code = status["status_code"]
        status = StatusModel(id=id,sequence_num=sequence_num,description=description,active_status=active_status,status_code=status_code)
        db.session.add(status)

    db.session.commit()