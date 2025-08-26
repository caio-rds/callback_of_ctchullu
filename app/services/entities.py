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
                    id=str(entity['_id']),
                    name=entity['name'],
                    type=entity['type'],
                    first_appearance=entity['first_appearance'],
                    habitat=entity['habitat'],
                    description=entity['description'],
                    associated_books=entity['associated_books'],
                    titles=entity['titles'] if 'titles' in entity else None,
                ))
        return entities

    @staticmethod
    async def get_entity(_id: str) -> ResponseEntity | None:
        if consult := await repository.get_entity_by_id(ObjectId(_id)):
            return ResponseEntity(
                id=str(consult['_id']),
                name=consult['name'],
                type=consult['type'],
                first_appearance=consult['first_appearance'],
                habitat=consult['habitat'],
                description=consult['description'],
                associated_books=consult['associated_books'],
                titles=consult['titles'] if 'titles' in consult else None,
            )
        return None