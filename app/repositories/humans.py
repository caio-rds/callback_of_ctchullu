from app.core.mongo_engine import database

class HumansRepository:
    def __init__(self):
        self.collection = database['humans']

    async def get_all_humans(self):
        return list(self.collection.find())

    async def get_human(self, location_id):
        return self.collection.find_one({'_id': location_id})