import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify, make_response, render_template
# from flask_cors import CORS

load_dotenv()

using_gunicorn = os.getenv('DEPLOYED_WITH_GUNICORN')
using_gunicorn = using_gunicorn == 'True'
if using_gunicorn:
    import grequests

# initialize openai with my key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='', static_folder='./static')
# CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('home.html', dynamic_variable="Sup homies.")

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

@app.route('/openai')
def openai_test():
    request_url = 'https://api.openai.com/v1/chat/completions'
    request_data = {
        'model': 'gpt-3.5-turbo',
        'temperature': 0.7,
        'max_tokens': 256,
        'messages': [
            {
                'role': 'system',
                'content': 'You are a helpful AI assistant who loves using emojis.',
            },
            {
                'role': 'user',
                'content': 'Hello, how are you today?'
            }
        ]
    }
    request_headers = {
        'Authorization': 'Bearer ' + OPENAI_API_KEY,
        'Content-Type': 'application/json'
    }
    if using_gunicorn:
        req = grequests.post(request_url, json=request_data, headers=request_headers)
        response = grequests.map([req])[0]
    else:
        response = requests.post(request_url, json=request_data, headers=request_headers)
    # print(response)
    json_response = response.json()
    message_content = json_response['choices'][0]['message']['content']
    # message_content = "Just a test."
    return render_template('home.html', dynamic_variable=message_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
