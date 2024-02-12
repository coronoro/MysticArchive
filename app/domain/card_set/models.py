from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.settings.db import orm


class CardSet(orm.DatabaseModel):
    __tablename__ = "card_sets"

    name: Mapped[str]
    code: Mapped[str]


class CardSetCard(orm.DatabaseModel):
    __tablename__ = "card_set_cards"

    left_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(ForeignKey("card_sets.id"), primary_key=True)
