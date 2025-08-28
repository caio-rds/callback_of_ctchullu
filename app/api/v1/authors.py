from http.client import HTTPException

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.services.authors import AuthorsService
from app.models.authors import ResponseAuthors

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseAuthors | None)
async def get_author_by_id(_id: str):
    if consult := await AuthorsService.get_author_by_id(_id):
        return consult
    raise HTTPException(status_code=404, detail="Author not found")

@router.get("/", response_model=list[ResponseAuthors], response_model_exclude_none=True)
async def get_authors():
    if consult := await AuthorsService.get_authors():
        return consult
    raise HTTPException(status_code=404, detail="No authors found")