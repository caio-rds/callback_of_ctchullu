from app.core.mongo_engine import database

class LocationsRepository:
    def __init__(self):
        self.collection = database['locations']

    async def get_all_locations(self):
        return list(self.collection.find())

    async def get_location_by_id(self, location_id):
        return self.collection.find_one({'_id': location_id})