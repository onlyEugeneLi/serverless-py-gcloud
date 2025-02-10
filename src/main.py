import os
from fastapi import FastAPI
from src.env import config 
import json

# Hardcode: MODE = "dev"
# MODE = os.environ.get("MODE") or "abc" # abc - default value
MODE = config("MODE", cast=str, default="Test")
USERNAME = config("USERNAME", cast=str, default="Unknown")
USERID = config("USERID", cast=int, default=000000)
# MODE is a made up variable. It can other things such as PORT, USERNAME, PASSWORD, etc.

app = FastAPI()

@app.get("/") # GET -> HTTP Method
def home_page():
    # for API services
    # JSON-ready dict -> json.dumps({"Hello": "World"})
    # return {"Hello": "World", "mode": MODE}
    response = {
        "Hello": "World",
        "Description": "This is my first cloud deployment using FastAPI",
        "Platform": "Google Cloud Run",
        "mode": MODE,
        "username": USERNAME,
        "userid": USERID
    }
    # return json.dumps(response, indent=4)
    return response