from fastapi import APIRouter
from app.recommender import recommend_movie

router = APIRouter(prefix="/recommend", tags=["Recommendations"])


@router.get("/{movie_title}")
def get_recommendations(movie_title: str):
    return recommend_movie(movie_title)
