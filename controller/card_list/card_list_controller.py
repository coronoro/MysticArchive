
from litestar import Controller, get
from sqlalchemy import select

from models.card_list import CardList


class CardListController(Controller):
    path = "/card-lists"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[CardList]:
        return list(await db_session.scalars(select(CardList)))
