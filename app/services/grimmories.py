from bson import ObjectId

from app.models.grimmories import ResponseGrimmories
from app.repositories.grimmories import GrimmoriesRepository
repository = GrimmoriesRepository()

class GrimmoriesService:

    @staticmethod
    async def get_grimmories() -> list[ResponseGrimmories]:
        grimmories = []
        if consult := await repository.get_all_grimmories():
            for grimmory in consult:
                grimmories.append(ResponseGrimmories(
                    id=str(grimmory['_id']),
                    name=grimmory['name'],
                    author=grimmory['author'],
                    first_appearance=grimmory['first_appearance'],
                    language=grimmory['language'],
                    description=grimmory['description'],
                    status=grimmory['status'],
                    associated_locations=grimmory['associated_locations'],
                ))
        return grimmories

    @staticmethod
    async def get_grimmory(_id: str) -> ResponseGrimmories | None:
        if consult := await repository.get_grimmory_by_id(ObjectId(_id)):
            return ResponseGrimmories(
                id=str(consult['_id']),
                name=consult['name'],
                author=consult['author'],
                first_appearance=consult['first_appearance'],
                language=consult['language'],
                description=consult['description'],
                status=consult['status'],
                associated_locations=consult['associated_locations'],
            )
        return None
