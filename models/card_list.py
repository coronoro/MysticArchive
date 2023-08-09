from sqlalchemy.orm import Mapped
from models import DatabaseModel



class CardList(DatabaseModel):
    __tablename__ = "card_lists"

    name: Mapped[str]
    collector_number: Mapped[str]
    image: Mapped[str]
