from django.db import models

import CreateUpdateModel
import MAUser


class Inventory(CreateUpdateModel):
    user = models.ForeignKey(MAUser)

    class Meta:
        abstract = True
