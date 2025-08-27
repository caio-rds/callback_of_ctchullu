from bson import ObjectId

from app.models.entities import ResponseEntity
from app.repositories.entities import EntitiesRepository
repository = EntitiesRepository()


class EntitiesService:

    @staticmethod
    async def get_entities() -> list[ResponseEntity]:
        entities = []
        if consult := await repository.get_all_entities():
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
    async def get_entity(_id: str) -> ResponseEntity | None:
        if consult := await repository.get_entity_by_id(ObjectId(_id)):
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
        return None