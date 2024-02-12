from select import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.card_set.models import CardSetCard
from app.settings.db import orm


class Card(orm.DatabaseModel, orm.SlugKey):
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
