from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/movies", tags=["Movies"])

df = pd.read_csv("../dataset/top10K-TMDB-movies.csv")

@router.get("/")
def get_movies():
    return df[['title', 'genre', 'vote_average']].head(50).to_dict(orient="records")

@router.get("/{title}")
def movie_details(title: str):
    movie = df[df['title'] == title]
    if movie.empty:
        return {"message": "Movie not found"}
    return movie.to_dict(orient="records")[0]
