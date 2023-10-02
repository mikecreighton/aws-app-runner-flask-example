import os
import pprint
from dotenv import load_dotenv
from flask import Flask, render_template
import requests
using_gunicorn = os.getenv('DEPLOYED_WITH_GUNICORN')
using_gunicorn = using_gunicorn == 'True'

if using_gunicorn:
    import grequests

load_dotenv()

# initialize openai with my key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='', static_folder='./static')

@app.route('/')
def home():
    return render_template('index.html', dynamic_variable="Sup homies")

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
    json_response = response.json()
    message_content = json_response['choices'][0]['message']['content']
    return render_template('index.html', dynamic_variable=message_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)