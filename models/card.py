from select import select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import CardSetCard, DatabaseModel


class Card(DatabaseModel):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    collector_number: Mapped[str]
    image: Mapped[str]

    sets: Mapped[list[CardSetCard]] = relationship()


async def get_card_list(session: AsyncSession) -> list[Card]:
    query = select(Card)
    result = await session.execute(query)
    return result.scalars().all()
