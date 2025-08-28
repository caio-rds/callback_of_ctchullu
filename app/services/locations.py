from bson import ObjectId
from bson.errors import InvalidId

from app.models.locations import ResponseLocation
from app.repositories.locations import LocationsRepository
repository = LocationsRepository()

class LocationsService:

    @staticmethod
    async def get_locations() -> list[ResponseLocation]:
        locations = []
        if consult := await repository.get_all_locations():
            for location in consult:
                locations.append(ResponseLocation(
                    id=str(location.get('_id')),
                    name=location.get('name'),
                    type=location.get('type'),
                    description=location.get('description'),
                    associated_stories=[f"api/v1/books/{story_id}" for story_id in location.get('associated_stories', [])],
                    notable_places=location.get('notable_places'),
                ))
        return locations

    @staticmethod
    async def get_location(_id: str) -> ResponseLocation | None:
        if not ObjectId.is_valid(_id):
            return None

        try:
            object_id = ObjectId(_id)
            if consult := await repository.get_location_by_id(object_id):
                return ResponseLocation(
                    id=str(consult.get('_id')),
                    name=consult.get('name'),
                    type=consult.get('type'),
                    description=consult.get('description'),
                    associated_stories=[f"api/v1/books/{story_id}" for story_id in
                                        consult.get('associated_stories', [])],
                    notable_places=consult.get('notable_places'),
                )
        except InvalidId:
            return None
        return None