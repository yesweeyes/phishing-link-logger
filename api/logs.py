from flask import jsonify

logs = []

def handler(request):
    return jsonify(logs)
