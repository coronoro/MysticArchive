from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from controller.card.card_controller import CardController
from controller.card_list.card_list_controller import CardListController
from controller.card_set.card_set_controller import CardSetController
from controller.inventory.inventory_controller import InventoryController
from controller.user.user_controller import UserController
from models.base import DatabaseModel


async def on_startup() -> None:
    """Initializes the database."""
    async with sqlalchemy_config.create_engine().begin() as conn:
        await conn.run_sync(DatabaseModel.metadata.create_all)

sqlalchemy_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///mysticArchive.sqlite")

app = Litestar(
    [CardController, CardSetController, UserController, InventoryController, CardListController],
    on_startup=[on_startup],
    plugins=[SQLAlchemyPlugin(sqlalchemy_config)],
)
