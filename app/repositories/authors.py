from bson import ObjectId

from app.core.mongo_engine import database

class AuthorsRepository:
    def __init__(self):
        self.collection = database['authors']

    async def get_all_authors(self):
        return list(self.collection.find())

    async def get_author_by_id(self, location_id: ObjectId):
        return self.collection.find_one({"_id": location_id})