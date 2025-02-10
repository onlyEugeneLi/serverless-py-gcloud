import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.env import config 
import json

# Hardcode: MODE = "dev"
# MODE = os.environ.get("MODE") or "abc" # abc - default value
MODE = config("MODE", cast=str, default="Test")
USERNAME = config("USERNAME", cast=str, default="Unknown")
USERID = config("USERID", cast=int, default=000000)
# MODE is a made up variable. It can other things such as PORT, USERNAME, PASSWORD, etc.

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_page():
    with open("src/template.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post("/submit")
def submit(user_input: str = Form(...)):
    with open("user_inputs.txt", "a") as file:
        file.write(user_input + "\n")
    return {"message": "Input received", "input": user_input}