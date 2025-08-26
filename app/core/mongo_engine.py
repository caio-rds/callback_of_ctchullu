import pymongo
import os

database = pymongo.MongoClient(os.getenv("MONGO_URI")).get_database("ctchullu")