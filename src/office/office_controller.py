from src.office import office_actions


def get_all_states():
    return {"states": office_actions.get_states()}


def get_offices_by_state(state):
    return {state: office_actions.get_offices_by_state(state)}

