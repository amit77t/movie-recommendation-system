from fastapi import APIRouter
import pandas as pd

import os

router = APIRouter(prefix="/movies", tags=["Movies"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "top10K-TMDB-movies.csv")

df = pd.read_csv(DATASET_PATH)

@router.get("/")
def get_movies():
    return df[['title', 'genre', 'vote_average']].head(50).to_dict(orient="records")

@router.get("/{title}")
def movie_details(title: str):
    movie = df[df['title'] == title]
    if movie.empty:
        return {"message": "Movie not found"}
    return movie.to_dict(orient="records")[0]
