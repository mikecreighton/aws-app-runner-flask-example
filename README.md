# aws-app-runner-flask-example

## First attempt in App Runner config

1. Run Flask directly: `flask run -h 0.0.0.0 -p 8080`.

## Second attempt in App Runner config

1. Add gunicorn to requirements.txt.
2. The build command is `pip install -r requirements.txt`.
3. Use this as the start command in App Runner: `gunicorn --workers=4 --bind=0.0.0.0:8080 app:app`.
4. Make sure the port is set to 8080.

## Current findings at this point

- As soon as we include the `openai` SDK, everything breaks when deploying App Runner.
- Otherwise, both run commands work just fine.
- We do want to push on gunicorn, however, since that's really meant for a production deployment.