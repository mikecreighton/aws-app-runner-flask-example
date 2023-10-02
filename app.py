import os
from dotenv import load_dotenv
import requests
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

load_dotenv()

# initialize openai with my key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@view_config(
    route_name='home',
    renderer='templates/home.jinja2'
)
def home(request):
    return {'dynamic_variable': 'Sup homies'}

def healthcheck(request):
    return Response('OK')

@view_config(
    route_name='openai_test',
    renderer='templates/home.jinja2'
)
def openai_test(request):
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
    response = requests.post(request_url, json=request_data, headers=request_headers)
    json_response = response.json()
    message_content = json_response['choices'][0]['message']['content']

    return {'dynamic_variable': message_content}

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('healthcheck', '/healthcheck')
        config.add_view(healthcheck, route_name='healthcheck')
        config.add_route('openai_test', '/openai')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()