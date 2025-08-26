from app.core.mongo_engine import database

class EntitiesRepository:
    def __init__(self):
        self.collection = database['entities']

    async def get_all_entities(self):
        return list(self.collection.find())

    async def get_entity_by_id(self, entity_id):
        return self.collection.find_one({'_id': entity_id})