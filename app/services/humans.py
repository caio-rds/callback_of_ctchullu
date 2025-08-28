from bson import ObjectId
from bson.errors import InvalidId

from app.models.entities import ResponseEntity
from app.repositories.humans import HumansRepository

repository = HumansRepository()


class HumansService:

    @staticmethod
    async def get_humans() -> list[ResponseEntity]:
        entities = []
        if consult := await repository.get_all_humans():
            for entity in consult:
                entities.append(ResponseEntity(
                    id=str(entity.get('_id')),
                    name=entity.get('name'),
                    type=entity.get('type'),
                    first_appearance=f"api/v1/books/{entity.get('first_appearance')}",
                    habitat=entity.get('habitat'),
                    description=entity.get('description'),
                    associated_books=[f"api/v1/books/{book_id}" for book_id in entity.get('associated_books', [])],
                    titles=entity.get('titles', None)
                ))
        return entities

    @staticmethod
    async def get_human(_id: str) -> ResponseEntity | None:
        if not ObjectId.is_valid(_id):
            return None

        try:
            object_id = ObjectId(_id)
            if consult := await repository.get_human(object_id):
                return ResponseEntity(
                    id=str(consult.get('_id')),
                    name=consult.get('name'),
                    type=consult.get('type'),
                    first_appearance=f"api/v1/books/{consult.get('first_appearance')}",
                    habitat=consult.get('habitat'),
                    description=consult.get('description'),
                    associated_books=[f"api/v1/books/{book_id}" for book_id in consult.get('associated_books', [])],
                    titles=consult.get('titles', None)
                )
        except InvalidId:
            return None
        return None