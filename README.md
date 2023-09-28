# aws-app-runner-flask-example

## First attempt in App Runner config

1. Run Flask directly: `flask run -h 0.0.0.0 -p 8080`

## Second attempt in App Runner config

1. Add gunicorn to requirements.
2. Use this to run the app: `gunicorn --bind=0.0.0.0:8080 app:app`