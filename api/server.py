from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)

# Allow all origins (you can specify specific origins here if needed)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logs = []  # Store logs in memory (resets every deployment)

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

    logs.append(log_entry)
    return jsonify({"message": "Logged", "data": logs}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

# Required for Vercel deployment - entry point
def handler(request):
    return app(request, None)
