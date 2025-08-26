from bson import ObjectId

from app.models.books import ResponseBooks
from app.repositories.books import BooksRepository
repository = BooksRepository()

class BooksService:

    @staticmethod
    async def get_books() -> list[ResponseBooks]:
        books = []
        if consult := await repository.get_all_books():
            for book in consult:
                books.append(ResponseBooks(
                    id=str(book['_id']),
                    title=book['title'],
                    year=book['year'],
                    type=book['type'],
                    description=book['description'],
                    notes=book['notes'],
                ))
        return books

    @staticmethod
    async def get_book(_id: str) -> ResponseBooks | None:
        if consult := await repository.get_book_by_id(ObjectId(_id)):
            return ResponseBooks(
                id=str(consult['_id']),
                title=consult['title'],
                year=consult['year'],
                type=consult['type'],
                description=consult['description'],
                notes=consult['notes'],
            )
        return None
