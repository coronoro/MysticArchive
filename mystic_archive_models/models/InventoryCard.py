from django.db import models

import CreateUpdateModel


class InventoryCard(CreateUpdateModel):
    amount = models.IntegerField()

    class Meta:
        abstract = True
