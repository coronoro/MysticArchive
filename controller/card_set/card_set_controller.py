
from litestar import Controller, get
from litestar.pagination import ClassicPagination
from sqlalchemy import select

from models.card_set import CardSet


class CardSetController(Controller):
    path = "/card-sets"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ClassicPagination[CardSet]:
        return list(await db_session.scalars(select(CardSet)))
