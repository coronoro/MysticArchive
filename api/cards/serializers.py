from typing import Any

from models.card import Card

CardType = dict[str, Any]
CardListType = [CardType]

def serialize_card(card: Card) -> CardType:
    return {"name": card.name}