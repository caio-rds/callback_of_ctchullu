from fastapi import APIRouter

from app.services.authors import AuthorsService
from app.models.authors import ResponseAuthors

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseAuthors | None)
async def get_author_by_id(_id: str):
    return await AuthorsService.get_author_by_id(_id)

@router.get("/", response_model=list[ResponseAuthors], response_model_exclude_none=True)
async def get_authors():
    return await AuthorsService.get_authors()