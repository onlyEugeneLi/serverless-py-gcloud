from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_home_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<title>Input Form</title>" in response.text

def test_submit():
    response = client.post("/submit", data={"user_input": "Test input"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Thank you for participating!" in response.text
    assert "Test input" in response.text

def test_submit_too_long_input():
    long_input = "a" * 65  # 65 characters, which is too long
    response = client.post("/submit", data={"user_input": long_input})
    assert response.status_code == 422  # Bad Request, default error code from FastAPI
    assert response.headers["content-type"] == "application/json"