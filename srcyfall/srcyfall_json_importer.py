import json

from app.domain.card.models import Card


def import_scryfall_cards(json_file):
    with open(json_file, encoding="utf8") as file:
        datas = json.load(file)
        for data in datas:
            Card.query.

srcyfall_file = "./oracle-cards-20240210220205.json"

import_scryfall_cards(srcyfall_file)
