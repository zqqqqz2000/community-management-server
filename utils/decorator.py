from typing import *
from flask import request
from global_var import s


def login_check(func: Callable[[Dict], str]):
    def inner_func():
        data = request.get_json(silent=True)
        if 'token' in data:
            token = data['token']
            try:
                u_dict = s.loads(token)
            except Exception as ignore:
                ...
        return func(u_dict)
    inner_func.__name__ = func.__name__
    return inner_func
