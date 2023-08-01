from select import select
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Card(Base):
    __tablename__  = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]



async def get_card_list(session: AsyncSession) -> list[Card]:
    query = select(Card)
    result = await session.execute(query)
    return result.scalars().all()