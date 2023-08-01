from litestar import get, Controller
from sqlalchemy.ext.asyncio import AsyncSession

from models.card import get_card_list, Card


class CardController(Controller):
    path = "/cards"

    @get()
    async def get_card_list(transaction: AsyncSession) -> list[Card]:
        return await get_card_list(transaction)
