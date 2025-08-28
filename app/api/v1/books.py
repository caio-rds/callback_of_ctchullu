from fastapi import APIRouter, HTTPException

from app.services.books import BooksService
from app.models.books import ResponseBooks

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseBooks | None)
async def get_book(_id: str):
    if book := await BooksService.get_book(_id=_id):
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/", response_model=list[ResponseBooks], response_model_exclude_none=True)
async def get_books():
    if books := await BooksService.get_books():
        return books
    raise HTTPException(status_code=404, detail="No books found")
