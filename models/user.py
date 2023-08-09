from sqlalchemy.orm import Mapped, relationship
from models import DatabaseModel


class User(DatabaseModel):
    __tablename__ = "users"

    name: Mapped[str]
    mail: Mapped[str]
    inventory: Mapped["Inventory"] = relationship(back_populates="owner")

    # password: Mapped[str]
