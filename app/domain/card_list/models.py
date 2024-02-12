from advanced_alchemy.base import UUIDBase
from sqlalchemy.orm import Mapped

from app.settings.db import orm


class CardList(orm.DatabaseModel):
    __tablename__ = "card_lists"

    name: Mapped[str]
    collector_number: Mapped[str]
    image: Mapped[str]
