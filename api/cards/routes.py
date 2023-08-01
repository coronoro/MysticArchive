from litestar import get
from sqlalchemy.ext.asyncio import AsyncSession

from api.cards.serializers import CardListType, serialize_card


@get("/")
async def get_card_list(transaction: AsyncSession) -> CardListType:
    # return [serialize_card(card) for card in await get_card_list(transaction)]
    return  await get_card_list(transaction)

