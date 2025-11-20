from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from core.auth.schemas import UserRead
from lottery.game_registry import LOTTERY_GAMES
from .schemas import LotteryPrediction

router = APIRouter(tags=["lottery"])

def get_current_user() -> UserRead:
    return UserRead(id=1, email="demo@example.com")

@router.get("/lottery/games")
async def list_games():
    return LOTTERY_GAMES

@router.get("/lottery/{game_id}/predictions", response_model=LotteryPrediction)
async def get_prediction(game_id: str, db: Session = Depends(get_db), current_user: UserRead = Depends(get_current_user)):
    if game_id not in LOTTERY_GAMES:
        raise HTTPException(status_code=404, detail="Unknown lottery game_id")
    return LotteryPrediction(
        game_id=game_id,
        total_draws_used=100,
        main_number_scores={i: 1.0 for i in range(1, 51)},
        bonus_number_scores={i: 1.0 for i in range(1, 13)},
        notes=["Stub prediction engine – replace with real models."],
    )
