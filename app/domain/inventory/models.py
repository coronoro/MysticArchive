from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import Optional
from sqlalchemy import ForeignKey

from app.settings.db import orm


class InventoryCard(orm.DatabaseModel):
    __tablename__ = "inventory_cards"
    left_id: Mapped[int] = mapped_column(ForeignKey("inventories.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)

    # additional attributes
    proxy: Mapped[Optional[bool]]
    count: Mapped[int]


class Inventory(orm.DatabaseModel):
    __tablename__ = "inventories"

    cards: Mapped[list[InventoryCard]] = relationship()

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="inventory")

    # password: Mapped[str]
