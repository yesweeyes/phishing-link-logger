from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

logged_data = []

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

    logged_data.append(log_entry)

    return jsonify({"message": "Logged", "data": logged_data}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logged_data)

# Required for Vercel to recognize Flask app
def handler(event, context):
    return app(event, context)
