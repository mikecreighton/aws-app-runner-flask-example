import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, Response

load_dotenv()

# initialize openai with my key
# openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='', static_folder='./static')

@app.route('/')
def home():
    return render_template('index.html', dynamic_variable="Hello world!")

# @app.route('/openai')
# def openai_test():

#     completion = openai.ChatCompletion.create(
#             model='gpt-3.5-turbo',
#             max_tokens=128,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are a helpful AI assistant."
#                 },
#                 {
#                     "role":"user",
#                     "content": "How are you doing today?"
#                 },
#             ],
#             temperature=0.9)
#     message_content = completion.choices[0].message.content
#     return jsonify({"message": message_content})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)