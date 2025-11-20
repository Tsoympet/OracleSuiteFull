from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from core.db import Base
from core.auth.models import User

class LotteryFavorite(Base):
    __tablename__ = "lottery_favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    game_id = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "game_id", name="uq_lottery_favorite_user_game"),
    )

    user = relationship("User", backref="lottery_favorites")
