
from litestar import Controller, get
from sqlalchemy import select

from models.user import User


class UserController(Controller):
    path = "/users"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[User]:
        return list(await db_session.scalars(select(User)))
