# -*- coding: utf-8 -*-
import traceback
from functools import wraps
from flask import jsonify, request, current_app
from werkzeug.wrappers import Response

from .exceptions import UnauthorizedException


def route(bp, *args, **kwargs):

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    return decorator


def api(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):

            status = 0
            message = ''
            data = None

            try:
                data = f(*args, **kwargs)

                # session timeout
                if isinstance(data, Response):
                    return data

                if isinstance(data, tuple):  # data, message, status
                    if len(data) > 2:
                        status = data[2]
                    if len(data) > 1:
                        message = data[1]
                    data = data[0]
            except UnauthorizedException as ex:
                return ex.message, 403
            except Exception as e:
                status = -1
                message = e.message

                if current_app.debug:
                    traceback.print_exc()

            return jsonify(dict(status=status, data=data, message=message))

        return wrapper

    return decorator
