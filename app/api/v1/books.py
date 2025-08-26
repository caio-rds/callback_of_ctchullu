from fastapi import APIRouter

from app.services.books import BooksService
from app.models.books import ResponseBooks

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseBooks | None)
async def get_book(_id: str):
    return await BooksService.get_book(_id=_id)

@router.get("/", response_model=list[ResponseBooks], response_model_exclude_none=True)
async def get_books():
    return await BooksService.get_books()
