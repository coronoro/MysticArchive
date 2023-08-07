from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models.card import Card
from models.inventory_card import InventoryCard


class Inventory(UUIDBase):
    __tablename__ = "inventories"

    cards: Mapped[list[InventoryCard]] = relationship()

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="inventory")


    # password: Mapped[str]