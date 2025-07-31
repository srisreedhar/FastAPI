from fastapi import FastAPI
from os import environ
from datetime import datetime,UTC



app = FastAPI()

@app.get("/")
def home():
    return {
        "api_version": "1.0",
        "time": datetime.now(tz=UTC),
        "os": environ["OS"],
        "user": environ["USERNAME"],
        "intel-arch": environ["PROCESSOR_ARCHITECTURE"],
    }