from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class BlockList(Base):
    __tablename__ = 'blocklist'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
