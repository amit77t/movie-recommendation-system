from fastapi import APIRouter
from app.recommender import recommend_movie

router = APIRouter(prefix="/recommend", tags=["Recommend"])

@router.get("/{movie_title}")
def recommend(movie_title: str):
    data = recommend_movie(movie_title)
    print("RECOMMEND API OUTPUT:", data)
    return data.to_dict(orient="records") if hasattr(data, "to_dict") else data
