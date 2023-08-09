from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models import DatabaseModel, InventoryCard


class Inventory(DatabaseModel):
    __tablename__ = "inventories"

    cards: Mapped[list[InventoryCard]] = relationship()

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="inventory")

    # password: Mapped[str]
