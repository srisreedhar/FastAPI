from fastapi import FastAPI
from os import environ
from datetime import datetime, UTC
from typing import Annotated, Optional

from pydantic import BaseModel


app = FastAPI()

# Data Models

class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# class UserPost(BaseModel):
#     body: str
#     id: Optional[int] = int



# store data
post_table = {}


# App Ping - Home Page
@app.get("/info")
def info():
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
    return {"endpoints": endpoints}



@app.post("/",response_model=UserPost)
def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table) # get length and assign as id
    new_post_data = {**data,"id":last_record_id}
    # push the post to post table
    post_table[last_record_id] = new_post_data
    return new_post_data

