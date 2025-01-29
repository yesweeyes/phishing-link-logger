# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import datetime

# # app = Flask(__name__)
# # CORS(app, origins="*")
# # logs = []

# # @app.route('/api/log', methods=['POST'])
# # def log_click():
# #     data = request.json
# #     user_agent = data.get('userAgent', 'Unknown')
# #     ip_address = request.headers.get('x-forwarded-for', request.remote_addr)
# #     timestamp = str(datetime.datetime.now())
# #     referrer = data.get('referrer', 'Unknown')
# #     screen_resolution = data.get('screenResolution', 'Unknown')
# #     timezone = data.get('timezone', 'Unknown')
# #     language = data.get('language', 'Unknown')

# #     log_entry = {
# #         "IP Address": ip_address,
# #         "User Agent": user_agent,
# #         "Time": timestamp,
# #         "Referrer": referrer,
# #         "Screen Resolution": screen_resolution,
# #         "Timezone": timezone,
# #         "Language": language
# #     }

# #     logs.append(log_entry)
# #     return jsonify({"message": "Logged", "data": logs}), 200

# # @app.route('/api/logs', methods=['GET'])
# # def get_logs():
# #     return jsonify(logs)

# # @app.route('/', methods=['GET'])
# # def home():
# #     return "<p>Hello, World!</p>"

# # def handler(request, *args, **kwargs):
# #     return app(request, *args, **kwargs)

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def home():
    return "Hello, Vercel!"

if __name__ == '__main__':
    app.run(debug=True)
