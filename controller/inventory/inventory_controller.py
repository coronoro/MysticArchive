
from litestar import Controller, get
from sqlalchemy import select

from models.inventory import Inventory


class InventoryController(Controller):
    path = "/inventories"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[Inventory]:
        return list(await db_session.scalars(select(Inventory)))
