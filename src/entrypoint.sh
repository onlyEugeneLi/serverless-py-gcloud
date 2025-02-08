#!/bin/bash

APP_PORT=${PORT:-8000}

cd /app/

# For anaconda virtual environment
# conda run -n cloud gunicorn -k uvicorn.workers.UvicornWorker src.main:app --blind "0.0.0.0"${APP_PORT}

# For python venv
# Implementing the web application
/opt/py38/bin/gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind "0.0.0.0:${APP_PORT}"