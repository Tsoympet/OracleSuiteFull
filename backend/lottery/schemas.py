from pydantic import BaseModel
from typing import List, Dict

class LotteryFavoriteItem(BaseModel):
    game_id: str

    class Config:
        orm_mode = True

class LotteryFavoritesResponse(BaseModel):
    favorites: List[LotteryFavoriteItem]

class LotteryPrediction(BaseModel):
    game_id: str
    total_draws_used: int
    main_number_scores: Dict[int, float]
    bonus_number_scores: Dict[int, float]
    notes: List[str]
