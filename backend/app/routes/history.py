from fastapi import APIRouter
from app.database import history_collection

router = APIRouter(prefix="/user", tags=["History"])

@router.get("/history/{user_id}")
def history(user_id: str):
    return list(history_collection.find({"user_id": user_id}, {"_id":0}))
