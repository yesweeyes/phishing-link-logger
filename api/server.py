from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import datetime

app = Flask(__name__)

CORS(app, origins="*") 

logs = []  

@app.route('/log', methods=['POST'])
def log_click():
    data = request.json

    # Extracting data from the request
    user_agent = data.get('userAgent', 'Unknown')
    ip_address = request.headers.get('x-forwarded-for', request.remote_addr)  # Get the user's IP address
    timestamp = str(datetime.datetime.now())  # Get the current timestamp
    referrer = data.get('referrer', 'Unknown')
    screen_resolution = data.get('screenResolution', 'Unknown')
    timezone = data.get('timezone', 'Unknown')
    language = data.get('language', 'Unknown')

    # Create the log entry
    log_entry = {
        "IP Address": ip_address,
        "User Agent": user_agent,
        "Time": timestamp,
        "Referrer": referrer,
        "Screen Resolution": screen_resolution,
        "Timezone": timezone,
        "Language": language
    }

    # Append the log entry to the logs list
    logs.append(log_entry)

    # Return the logs data in the response
    return jsonify({"message": "Logged", "data": logs}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)  # Return all logs when a GET request is made

# This is required for Vercel to work properly (you can keep it as is)
def handler(request):
    return app(request, None)

if __name__ == "__main__":
    app.run()  
