def init_status_table(statuses_list,db):
    from models import StatusModel
    for status in statuses_list:
        id = status["id"]
        status_federal_office_code = status["status_federal_office_code"]
        sequence_num = status["sequence_num"]
        description = status["description"]
        status = StatusModel(id,status_federal_office_code,sequence_num,description)
        db.session.add(status)