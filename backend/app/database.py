import os
from pymongo import MongoClient 


# Change this if using MongoDB Atlas
MONGO_URL = os.getenv("MONGO_URI")




client = MongoClient(MONGO_URL)
db = client.movie_recommender

users_collection = db.users
ratings_collection = db.ratings
history_collection = db.history
