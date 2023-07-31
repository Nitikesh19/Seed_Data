
def str_to_bool(bool_str):
    if not bool_str:
        return False
    return bool_str.lower() in ['true', '1', 't', 'y', 'yes']
