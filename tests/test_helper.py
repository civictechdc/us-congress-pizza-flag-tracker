def dict_keyvalue_or_default (dict, key_value, default):
    if key_value in dict:
        return dict[key_value]
    return default