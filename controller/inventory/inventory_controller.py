
from litestar import Controller, get, post
from litestar.pagination import ClassicPagination
from sqlalchemy import select, UUID

from models.card import Card
from models.inventory import Inventory


class InventoryController(Controller):
    path = "/inventories"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ClassicPagination[Inventory]:
        return list(await db_session.scalars(select(Inventory)))

    @get('/{inventory_id:uuid}')
    async def get_inventory(self, db_session: "AsyncSession", db_engine: "AsyncEngine", inventory_id:UUID) -> Inventory:
        return await db_session.query(Inventory).get(inventory_id)

    @post('/{inventory_id:uuid}/')
    async def add_card(self, db_session: "AsyncSession", db_engine: "AsyncEngine", inventory_id:UUID, card_id:UUID) -> Inventory:
        card = await db_session.query(Card).get(card_id)

        return await db_session.query(Inventory).get(inventory_id)
