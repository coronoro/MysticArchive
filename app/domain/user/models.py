from sqlalchemy.orm import Mapped, relationship
from app.domain.inventory.models import Inventory
from app.settings.db import orm


class User(orm.DatabaseModel):
    __tablename__ = "users"

    name: Mapped[str]
    mail: Mapped[str]
    inventory: Mapped["Inventory"] = relationship(back_populates="owner")

    # password: Mapped[str]
