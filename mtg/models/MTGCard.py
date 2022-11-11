from enum import Enum
from mystic_archive_models.models import Card
from django.db import models

class Color(Enum):
    WHITE = 'w'
    BLACK = 'b'
    RED = 'r'
    GREEN = 'g'
    BLUE = 'u'

class Rarity(Enum):
    COMMON = 'c'
    UNCOMMON = 'u'
    RARE = 'r'

class MTGCard(Card):
    name = models.CharField(255)
    colors = models.JSONField(default=[])
    rarity = models.CharField(max_length=1, choices=Rarity)
    foil = models.BooleanField()
    text = models.TextField()

    image = models.CharField()

    type_line = models.TextField()

    power = models.CharField(4)
    toughness = models.CharField(4)
    mana_cost = models.CharField(255)

    class Meta:
        db_table = 'mtg_cards'
