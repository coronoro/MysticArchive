from sqlalchemy.orm import Mapped

from models.base import Base


class CardSet(Base):

    name: Mapped[str]
    identifier: Mapped[str]