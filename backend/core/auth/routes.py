from fastapi import APIRouter
from .schemas import UserRead

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me", response_model=UserRead)
async def get_me():
    return UserRead(id=1, email="demo@example.com")
