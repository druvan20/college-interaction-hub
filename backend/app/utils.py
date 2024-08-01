from flask import jsonify

def create_response(data=None, message=None, status_code=200):
    response = {
        'status': 'success' if status_code == 200 else 'error',
        'message': message,
        'data': data
    }
    return jsonify(response), status_code
