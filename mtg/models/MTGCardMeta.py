from mystic_archive_models import CreateUpdateModel
from django.db import models


class MTGCardMeta(CreateUpdateModel):
    dominant_colors = models.JSONField(default=[])

    class Meta:
        db_table = 'mtg_card_metas'