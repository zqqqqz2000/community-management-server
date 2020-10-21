from typing import *
from flask import request
from global_var import s


def login_check(func: Callable[[int], str]):
    def inner_func():
        username = None
        data = request.get_json(silent=True)
        if 'token' in data:
            token = data['token']
            try:
                u_dict = s.loads(token)
                username = u_dict['username']
            except Exception as ignore:
                ...
        return func(username)
    inner_func.__name__ = func.__name__
    return inner_func
