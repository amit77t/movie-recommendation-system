from fastapi import APIRouter, HTTPException
from app.models import UserRegister, UserLogin
from app.database import users_collection
from app.auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegister):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hash_password(user.password)
    })
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"email": user.email})
    return {"token": token}
