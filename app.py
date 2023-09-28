import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, Response

load_dotenv()

# initialize openai with my key
# openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='', static_folder='./static')

@app.route('/')
def home():
    # return render_template('index.html')
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)