from bson import ObjectId
from bson.errors import InvalidId

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
                    id=str(grimmory.get('_id')),
                    name=grimmory.get('name'),
                    author=grimmory.get('author'),
                    first_appearance=grimmory.get('first_appearance'),
                    language=grimmory.get('language'),
                    description=grimmory.get('description'),
                    status=grimmory.get('status'),
                    associated_locations=grimmory.get('associated_locations'),
                ))
        return grimmories

    @staticmethod
    async def get_grimmory(_id: str) -> ResponseGrimmories | None:
        if not ObjectId.is_valid(_id):
            return None

        try:
            object_id = ObjectId(_id)
            if consult := await repository.get_grimmory_by_id(object_id):
                return ResponseGrimmories(
                    id=str(consult.get('_id')),
                    name=consult.get('name'),
                    author=consult.get('author'),
                    first_appearance=consult.get('first_appearance'),
                    language=consult.get('language'),
                    description=consult.get('description'),
                    status=consult.get('status'),
                    associated_locations=consult.get('associated_locations'),
                )
        except InvalidId:
            return None
        return None
