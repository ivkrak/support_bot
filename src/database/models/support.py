from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class SupportRequest(Base):
    __tablename__ = 'support_requests'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # номер обращения
    message_from_user_id: Mapped[int]
    message_from_support_id: Mapped[int]
    user_id: Mapped[int]
