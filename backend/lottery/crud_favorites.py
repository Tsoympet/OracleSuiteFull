from sqlalchemy.orm import Session
from typing import List
from .models import LotteryFavorite

def get_favorites_for_user(db: Session, user_id: int) -> List[LotteryFavorite]:
    return db.query(LotteryFavorite).filter(LotteryFavorite.user_id == user_id).all()

def add_favorite(db: Session, user_id: int, game_id: str) -> LotteryFavorite:
    fav = db.query(LotteryFavorite).filter(
        LotteryFavorite.user_id == user_id,
        LotteryFavorite.game_id == game_id
    ).first()
    if fav:
        return fav
    fav = LotteryFavorite(user_id=user_id, game_id=game_id)
    db.add(fav)
    db.commit()
    db.refresh(fav)
    return fav

def remove_favorite(db: Session, user_id: int, game_id: str) -> None:
    fav = db.query(LotteryFavorite).filter(
        LotteryFavorite.user_id == user_id,
        LotteryFavorite.game_id == game_id
    ).first()
    if fav:
        db.delete(fav)
        db.commit()
