from bson import ObjectId
from bson.errors import InvalidId

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
                    id=str(book.get('_id')),
                    title=book.get('title'),
                    year=book.get('year'),
                    type=book.get('type'),
                    description=book.get('description'),
                    notes=book.get('notes'),
                    author=f"api/v1/authors/{book.get('author_id')}"
                ))
        return books

    @staticmethod
    async def get_book(_id: str) -> ResponseBooks | None:
        if not ObjectId.is_valid(_id):
            return None

        try:
            object_id = ObjectId(_id)
            if consult := await repository.get_book_by_id(object_id):
                return ResponseBooks(
                    id=str(consult.get('_id')),
                    title=consult.get('title'),
                    year=consult.get('year'),
                    type=consult.get('type'),
                    description=consult.get('description'),
                    notes=consult.get('notes'),
                    author=f"api/v1/authors/{consult.get('author_id')}"
                )
        except InvalidId:
            return None
        return None
