
from litestar import Controller, get
from sqlalchemy import select

from models.card_set import CardSet


class CardSetController(Controller):
    path = "/card-sets"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[CardSet]:
        return list(await db_session.scalars(select(CardSet)))
