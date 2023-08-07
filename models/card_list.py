from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy.orm import Mapped


class CardList(UUIDBase):
    __tablename__ = "card-lists"

    name: Mapped[str]
    collector_number: Mapped[str]
    image: Mapped[str]