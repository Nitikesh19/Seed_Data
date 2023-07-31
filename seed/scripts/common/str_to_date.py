from datetime import datetime


def str_to_date(date_str):
    if not date_str:
        return None
    datetime_object = datetime.strptime(date_str, '%d/%m/%Y')
    return datetime_object
