from pydantic import BaseModel

class ResponseGrimmories(BaseModel):
    id: str
    name: str
    author: str
    first_appearance: str
    language: str
    description: str
    status: str
    associated_locations: list[str]