import OfficeActions

def get_all_states():
    return {"states": OfficeActions.get_states()}


def get_offices_by_state(state):
    return {state: OfficeActions.get_offices_by_state(state)}

