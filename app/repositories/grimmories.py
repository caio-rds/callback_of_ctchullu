from bson import ObjectId
from app.core.mongo_engine import database

class GrimmoriesRepository:
    def __init__(self):
        self.collection = database['grimmories']

    async def get_all_grimmories(self):
        return list(self.collection.find())

    async def get_grimmory_by_id(self, grimmory_id: ObjectId):
        return self.collection.find_one({"_id": grimmory_id})
