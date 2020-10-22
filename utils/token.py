from typing import *
from flask import request
from global_var import s


def with_token(func: Callable[[Optional[Dict]], str]):
    def inner_func():
        u_dict = None
        data = request.get_json(silent=True)
        try:
            if 'token' in data:
                token = data['token']
                u_dict = s.loads(token)
        except Exception as ignore:
            ...
        return func(u_dict)

    inner_func.__name__ = func.__name__
    return inner_func


def tokenize(data: Dict) -> str:
    return s.dumps(data).decode('ascii')
