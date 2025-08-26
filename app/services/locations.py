from bson import ObjectId

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
                    id=str(location['_id']),
                    name=location['name'],
                    type=location['type'],
                    description=location['description'],
                    associated_stories=location['associated_stories'],
                    notable_places=location['notable_places'] if 'notable_places' in location else None,
                ))
        return locations

    @staticmethod
    async def get_location(_id: str) -> ResponseLocation | None:
        if consult := await repository.get_location_by_id(ObjectId(_id)):
            return ResponseLocation(
                id=str(consult['_id']),
                name=consult['name'],
                type=consult['type'],
                description=consult['description'],
                associated_stories=consult['associated_stories'],
                notable_places=consult['notable_places'] if 'notable_places' in consult else None,
            )
        return None