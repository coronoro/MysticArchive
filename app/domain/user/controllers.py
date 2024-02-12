from litestar import Controller, get, post
from sqlalchemy import select

from app.domain.user.models import User


class UserController(Controller):
    path = "/users"

    @get()
    async def get_list(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[User]:
        return list(await db_session.scalars(select(User)))

    @post("/register")
    async def register(self, db_session: "AsyncSession", db_engine: "AsyncEngine") -> User:
        await db_session.scalars()
        return
