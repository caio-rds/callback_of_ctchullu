from pydantic import BaseModel

class ResponseLocation(BaseModel):
    id: str
    name: str
    type: str
    description: str
    associated_stories: list[str]
    notable_places: list[str] | None = None