from typing import Optional

from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models.card import Card


class InventoryCard(UUIDBase):
    __tablename__ = "inventory_cards"
    left_id: Mapped[int] = mapped_column(ForeignKey("inventories.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)

    #additional attributes
    proxy: Mapped[Optional[bool]]
    count: Mapped[int]

