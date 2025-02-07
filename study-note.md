# Project Progress Documentation

This file documents key takeaways along the learning journey.

## Python Project Setup

### FastAPI
Fastapi import FastAPI

### Environment settings
Auto path setting: 
```
BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_PATH = BASE_DIR / '.env'
```
Reference file: [env.py](./src/env.py)

.env
System setting: 
```
MODE = config("MODE", cast=str, default="Test”)
```
if .env not found, use default.

Reference file: [main.py](./src/main.py)

### Cache environment settings
`From functors import lru_cache`

Reference file: [env.py](./src/env.py) line 13

### Command line shortcut
RAV package
```
scripts:
  runserver: uvicorn src.main:app --reload
```

Command: `rav run runserver`

### Web implementation

Uvicorn

`uvicorn src.main:app --reload`

### Testing

Testing object  `from fastapi.testclient import TestClient`

Testing execution package `pytest`

Reference file: [tests.py](./src/tests.py)

## Docker and Containerising Python Apps

Steps

1. Pick image from hub.docker.com: slim is preferred
1. `COPY` files to container: `COPY local_folder destination_file`
1. Set working directory `WORKDIR /app/`. Sometimes `WORKDIR /opt/app/`
1. Run command lines. `RUN cmd-line` (cannot activate virtual environment. Can only interact with shell commands)
1. Run the app. `CMD ["./entrypoint.sh"]`

Reference file: [Dockerfile](Dockerfile)


Last update above: 2025-2-7
