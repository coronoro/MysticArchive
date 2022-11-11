from enum import Enum

from django.db import models

import CreateUpdateModel


class Card(CreateUpdateModel):
    name = models.CharField(255)
    foil = models.BooleanField()

    image = models.CharField()

    class Meta:
        abstract = True


