from bson import ObjectId
from app.core.mongo_engine import database

class BooksRepository:
    def __init__(self):
        self.collection = database['books']

    async def get_all_books(self):
        return list(self.collection.find())

    async def get_book_by_id(self, book_id: ObjectId):
        return self.collection.find_one({"_id": book_id})
