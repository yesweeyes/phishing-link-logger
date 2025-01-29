from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app, origins="*")
logs = []

@app.route('/log', methods=['POST'])
def log_click():
    data = request.json
    user_agent = data.get('userAgent', 'Unknown')
    ip_address = request.headers.get('x-forwarded-for', request.remote_addr)
    timestamp = str(datetime.datetime.now())
    referrer = data.get('referrer', 'Unknown')
    screen_resolution = data.get('screenResolution', 'Unknown')
    timezone = data.get('timezone', 'Unknown')
    language = data.get('language', 'Unknown')
   
    log_entry = {
        "IP Address": ip_address,
        "User Agent": user_agent,
        "Time": timestamp,
        "Referrer": referrer,
        "Screen Resolution": screen_resolution,
        "Timezone": timezone,
        "Language": language
    }
   
    logs.append(log_entry)
    return jsonify({"message": "Logged", "data": logs}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Server is running"}), 200

# Modified catch-all route to return a 404 response
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return jsonify({"error": "Not found"}), 404

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# For Vercel deployment
application = app