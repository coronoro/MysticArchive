from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy.orm import Mapped


class CardSet(UUIDBase):
    __tablename__ = "card_set"

    name: Mapped[str]
    code: Mapped[str]
