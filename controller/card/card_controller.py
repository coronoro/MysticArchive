
from litestar import Controller, get
from litestar.pagination import ClassicPagination
from sqlalchemy import select

from models.card import Card


class CardController(Controller):
    path = "/cards"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ClassicPagination[Card]:
        return list(await db_session.scalars(select(Card)))
