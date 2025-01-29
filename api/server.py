from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
LOG_FILE = "logs.json"

# Load logs from file
def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            return json.load(file)
    return []

# Save logs to file
def save_logs(logs):
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

@app.route('/log', methods=['POST'])
def log_click():
    data = request.json
    user_agent = data.get('userAgent', 'Unknown')
    ip_address = request.headers.get('x-forwarded-for', request.remote_addr)
    timestamp = str(datetime.datetime.now())

    log_entry = {
        "IP Address": ip_address,
        "User Agent": user_agent,
        "Time": timestamp
    }

    logs = load_logs()
    logs.append(log_entry)
    save_logs(logs)

    return jsonify({"message": "Logged", "data": logs}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = load_logs()
    return jsonify(logs)

# Required for Vercel
def handler(event, context):
    return app(event, context)
