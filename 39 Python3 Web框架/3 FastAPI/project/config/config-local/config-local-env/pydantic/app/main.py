# app/main.py
from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "database_url": settings.database_url,
        "api_key": settings.api_key
    }
