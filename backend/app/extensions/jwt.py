from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt  # , get_jwt_identity
from flask import jsonify


def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            # user = get_jwt_identity()
            claims = get_jwt()
            if claims["role"] not in required_role:
                return jsonify(msg="Access forbidden: Insufficient role"), 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper
