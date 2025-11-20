from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from core.auth.schemas import UserRead
from .schemas import LotteryFavoritesResponse, LotteryFavoriteItem
from .crud_favorites import get_favorites_for_user, add_favorite, remove_favorite

router = APIRouter(tags=["lottery-favorites"])

def get_current_user() -> UserRead:
    return UserRead(id=1, email="demo@example.com")

@router.get("/lottery/favorites", response_model=LotteryFavoritesResponse)
async def list_lottery_favorites(
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
):
    favs = get_favorites_for_user(db, current_user.id)
    return LotteryFavoritesResponse(
        favorites=[LotteryFavoriteItem(game_id=f.game_id) for f in favs]
    )

@router.post("/lottery/favorites/{game_id}", response_model=LotteryFavoritesResponse)
async def add_lottery_favorite(
    game_id: str,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
):
    add_favorite(db, current_user.id, game_id)
    favs = get_favorites_for_user(db, current_user.id)
    return LotteryFavoritesResponse(
        favorites=[LotteryFavoriteItem(game_id=f.game_id) for f in favs]
    )

@router.delete("/lottery/favorites/{game_id}", response_model=LotteryFavoritesResponse)
async def remove_lottery_favorite_endpoint(
    game_id: str,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
):
    remove_favorite(db, current_user.id, game_id)
    favs = get_favorites_for_user(db, current_user.id)
    return LotteryFavoritesResponse(
        favorites=[LotteryFavoriteItem(game_id=f.game_id) for f in favs]
    )
