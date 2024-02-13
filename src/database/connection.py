"""Файл для работы с подключением к базе данных."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Базовый класс, от которого наследуются все модели SQLAlchemy."""
    


class DataBaseConnection(object):
    """Класс для подключения к бд."""

    def __init__(self, url: str, echo: bool = False):
        """
        Устанавливает соединение с базой данных при создании экземпляра класса.

        Args:
            url (str): URL для соединения с базой данных.
            echo (bool): Указывает, следует ли выводить все SQL-запросы в консоль.

        Examples:
            db_conn = DataBaseConnection(url="sqlite+aiosqlite:///example.db", echo=True)
        """
        self.engine = create_engine(
            url=url,
            echo=echo,
        )

        self.session_maker = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    def get_session(self) -> Session:
        """
        Возвращает сессию SQLAlchemy для выполнения запросов к базе данных.

        Returns: Session: сессия SQLAlchemy.
        """
        with self.session_maker() as session:
            return session


db_conn = DataBaseConnection(
    url='sqlite:///src/database/db_data/db.sqlite3',
    echo=False,
)
