from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy.orm import Mapped, relationship


class User(UUIDBase):
    __tablename__ = "users"

    name: Mapped[str]
    mail: Mapped[str]
    inventory: Mapped["Inventory"] = relationship(back_populates="owner")

    # password: Mapped[str]