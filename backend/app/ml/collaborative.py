import pandas as pd
from surprise import Dataset, Reader, SVD
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.movie_ai
ratings = pd.DataFrame(list(db.ratings.find({}, {"_id":0})))

reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(
    ratings[['user_id','movie_title','rating']], reader
)

trainset = data.build_full_trainset()
model = SVD()
model.fit(trainset)

def predict_rating(user_id, movie_title):
    return model.predict(user_id, movie_title).est
