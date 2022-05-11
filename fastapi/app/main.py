from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def hello_world():
    api_key = os.getenv('API_KEY')
    return {"bunnyshell-neo": "awesome", "api_key": api_key}
