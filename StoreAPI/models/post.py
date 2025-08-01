from pydantic import BaseModel

#Data Models

class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# class UserPost(BaseModel):
#     body: str
#     id: Optional[int] = int