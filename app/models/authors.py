from pydantic import BaseModel

class ResponseAuthors(BaseModel):
    id: str
    name: str
    birth_year: int
    death_year: int
    nationality: str
    description: str
    works: list[str]