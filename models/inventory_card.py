from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models import DatabaseModel


class InventoryCard(DatabaseModel):
    __tablename__ = "inventory_cards"
    left_id: Mapped[int] = mapped_column(ForeignKey("inventories.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)

    # additional attributes
    proxy: Mapped[Optional[bool]]
    count: Mapped[int]
