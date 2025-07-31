from fastapi import FastAPI
from os import environ
from datetime import datetime,UTC
from typing import Annotated, Optional


app = FastAPI()


# App Ping - Home Page
@app.get("/")
def home():
    return {
        "api_version": "1.0",
        "time": datetime.now(tz=UTC),
        "os": environ["OS"],
        "user": environ["USERNAME"],
        "intel-arch": environ["PROCESSOR_ARCHITECTURE"],
    }

# Get all the Endpoints
@app.get("/list-endpoints")
def list_endpoints():
    endpoints = []
    for each_route in app.routes:
        endpoint = [{"path": each_route.path, "methods": list(each_route.methods)}]
        endpoints.append(endpoint)
    return {
        "endpoints": endpoints
        }