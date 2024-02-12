from litestar import Controller, get
from litestar.pagination import ClassicPagination
from sqlalchemy import select

from app.domain.card_list.models import CardList


class CardListController(Controller):
    path = "/card-lists"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ClassicPagination[CardList]:
        return list(await db_session.scalars(select(CardList)))
