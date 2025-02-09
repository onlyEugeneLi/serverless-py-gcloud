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

By default, you cannot access the container without exposing the port. 

```
docker run -p 1234:8000 -it empty-py
```

Go inside the container in terminal:

```
docker exec -it a34827407444 /bin/bash
```

`-p` --> port flag

`-it` --> interactive flag

`--name` --> name runtime setting flag

To access container's shell:

- [rav.yaml](rav.yaml)
  ```
  empty-run: docker run -p 1234:8000 --name <name_of_runtime> -it empty-py
  empty-shell: docker exec -it <name_of_runtime> /bin/bash
  ```
- command line
  ```
  rav run empty-run
  rav run empty-shell
  ```

Last update above: 2025-2-7


## CI/CD Pipeline

Github Actions:

Automates deployment processes (to server like Google Cloud, AWS and Azure etc.) by running the change deployment upon every `git push` received to remote repository.

There are standard scripts available on Github for Github Actions setup. 

[Setup docker buildx](https://github.com/docker/setup-buildx-action)

[Setup Google Cloud in Github Actions](https://github.com/google-github-actions/setup-gcloud)

[Authenticate to Google Cloud from Github Actions](https://github.com/google-github-actions/auth?tab=readme-ov-file#sake)

Github Actions Secrets:

Hide the credentials in the project. Abstract them away from code.

```
${{ secrets.SECRET_NAME }}
```