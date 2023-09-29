# aws-app-runner-flask-example

## First attempt in App Runner config

1. Run Flask directly: `flask run -h 0.0.0.0 -p 8080`

## Second attempt in App Runner config

1. Add gunicorn to requirements.txt.
2. The build command is `pip install -r requirements.txt`
3. Use this as the start command in App Runner: `gunicorn --bind=0.0.0.0:8080 app:app`
4. Make sure the port is set to 8080