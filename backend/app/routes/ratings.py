from fastapi import APIRouter
from app.models import Rating
from app.database import ratings_collection

router = APIRouter(tags=["Ratings"])

@router.post("/rate-movie")
def rate_movie(data: Rating):
    ratings_collection.insert_one(data.dict())
    return {"message": "Rating saved"}
