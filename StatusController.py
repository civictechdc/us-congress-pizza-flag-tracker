from StatusActions import StatusActions


def get_statuses():
    return {"statuses": table_to_json(StatusActions.get_statuses())}
