try:
    match 0:
        case _:...
    raise Exception
except* (Exception):
    match 0:
        case _:...
