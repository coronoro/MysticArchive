from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO

from app.domain.card_list.models import CardList
from app.settings import dto

__all__ = ["CardListDTO"]


class CardListDTO(SQLAlchemyDTO[CardList]):
    config = dto.config(
        backend="sqlalchemy",
        exclude={
            "members.team",
            "members.user",
            "members.created_at",
            "members.updated_at",
            "members.id",
            "members.user_name",
            "members.user_email",
            "invitations",
            "pending_invitations",
        },
        max_nested_depth=1,
    )
