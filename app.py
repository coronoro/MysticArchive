from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar
from litestar.datastructures import State
from litestar.exceptions import ClientException, NotFoundException
from litestar.status_codes import HTTP_409_CONFLICT
from litestar.contrib.sqlalchemy.plugins import SQLAlchemySerializationPlugin, SQLAlchemyInitPlugin, \
    SQLAlchemyAsyncConfig
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


async def provide_transaction(db_session: AsyncSession) -> AsyncGenerator[AsyncSession, None]:
    try:
        async with db_session.begin():
            yield db_session
    except IntegrityError as exc:
        raise ClientException(
            status_code=HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


db_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///todo.sqlite")


app = Litestar(
    [],
    dependencies={"transaction": provide_transaction},
    plugins=[SQLAlchemySerializationPlugin(),
             SQLAlchemyInitPlugin(db_config),
             ],
)
