
from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class CardSetCard(UUIDBase):
    __tablename__ = "card_set_cards"

    left_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(ForeignKey("card_sets.id"), primary_key=True)

    #additional attributes

