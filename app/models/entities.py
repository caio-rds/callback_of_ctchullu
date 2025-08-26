from pydantic import BaseModel


class ResponseEntity(BaseModel):
    id: str
    name: str
    type: str
    first_appearance: str
    habitat: str
    description: str
    associated_books: list[str]
    titles: list[str] | None = None