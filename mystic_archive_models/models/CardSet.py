from django.db import models

import CreateUpdateModel

class CardSet(CreateUpdateModel):
    name = models.CharField()

    # date of release
    release = models.DateTimeField()

    # number of cards the set has
    amount = models.IntegerField()



    class Meta:
        abstract = True