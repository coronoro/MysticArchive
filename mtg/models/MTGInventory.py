from mystic_archive_models.models import MAUser
from mystic_archive_models.models.Inventory import Inventory
from django.db import models


class MTGInventory(Inventory):
    owner = models.ForeignKey(MAUser, on_delete=models.CASCADE)


    class Meta:
        db_table = 'mtg_inventory'