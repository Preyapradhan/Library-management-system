from flask import request, jsonify
from functools import wraps

tokens = {"admin": "12345"}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in tokens.values():
            return jsonify({"message": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated
