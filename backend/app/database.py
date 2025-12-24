import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URI")

if not MONGO_URL:
    raise ValueError("MONGO_URI not set in environment")

client = MongoClient(MONGO_URL)
db = client.movieDB

users_collection = db.users
ratings_collection = db.ratings
history_collection = db.history
