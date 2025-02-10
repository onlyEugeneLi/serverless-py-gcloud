import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.env import config 
from pydantic import BaseModel, constr, StringConstraints, ValidationError
from typing_extensions import Annotated
import json

app = FastAPI()

class UserInput(BaseModel):
    # user_input: constr(max_length=64)
    user_input: Annotated[
                str,
                StringConstraints(
                    max_length=64
                ),
            ]

@app.get("/", response_class=HTMLResponse)
def home_page():
    with open("src/form.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post("/submit", response_class=HTMLResponse)
def submit(user_input: UserInput = Form(...)):
    # Store input
    with open("user_inputs.txt", "a") as file:
        file.write(user_input.user_input + "\n")
    # Instruct user to close the page
    with open("src/thank_you.html", "r") as file:
        thank_you_content = file.read()
    # Replace placeholder with actual user input
    thank_you_content = thank_you_content.replace("{{ user_input }}", user_input.user_input)
    return HTMLResponse(content=thank_you_content)