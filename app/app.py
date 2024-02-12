from litestar import Litestar

from app.domain.card.controllers import CardController
from app.domain.card_list.controllers import CardListController
from app.domain.card_set.controllers import CardSetController
from app.domain.inventory.controllers import InventoryController
from app.domain.user.controllers import UserController
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyPlugin


async def on_startup() -> None:
    """Initializes the database."""
    # async with sqlalchemy_config.create_engine().begin() as conn:
    # await conn.run_sync(DatabaseModel.metadata.create_all)


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string="sqlite+aiosqlite:///mysticArchive.sqlite", session_config=session_config
)  # Create 'async_session' dependency.

app = Litestar(
    [CardController, CardSetController, UserController, InventoryController, CardListController],
    on_startup=[on_startup],
    plugins=[SQLAlchemyPlugin(config=sqlalchemy_config)],
)
