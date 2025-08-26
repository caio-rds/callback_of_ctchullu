from pydantic import BaseModel

class ResponseBooks(BaseModel):
    id: str
    title: str
    year: int
    type: str
    description: str
    notes: str