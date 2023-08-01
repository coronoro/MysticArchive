from litestar import get, Controller
from sqlalchemy.ext.asyncio import AsyncSession

from api.cards.serializers import CardListType
from models.card import get_card_list


class CardController(Controller):
    path = "/cards"

    @get()
    async def get_card_list(transaction: AsyncSession) -> CardListType:
        # return [serialize_card(card) for card in await get_card_list(transaction)]
        return await get_card_list(transaction)
