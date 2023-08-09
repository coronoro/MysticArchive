from sqlalchemy.orm import Mapped
from models import DatabaseModel


class CardSet(DatabaseModel):
    __tablename__ = "card_sets"

    name: Mapped[str]
    code: Mapped[str]
