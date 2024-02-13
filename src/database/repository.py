from sqlalchemy import select, update
from sqlalchemy.orm import Session

from src.database.models import BlockList, SupportRequest


def add_user_to_block_list(session: Session, user_id: int) -> BlockList:
    """
    Добавляет пользователя в блокировку
    """
    blocklist = BlockList(user_id=user_id)
    session.add(blocklist)
    session.commit()
    return blocklist

def add_support_request(
        session: Session,
        message_from_user_id: int,
        message_from_support_id: int,
        user_id: int) -> SupportRequest:
    """
    Добавляет запрос поддержки
    """
    support_request = SupportRequest(
        message_from_support_id=message_from_support_id,
        message_from_user_id=message_from_user_id,
        user_id = user_id
    )
    session.add(support_request)
    session.commit()
    return support_request

def get_info_about_ticket(session: Session, message_from_support_id: int):
    """
    Получает информацию о тикете
    """
    ticket = session.execute(
        select(SupportRequest).where(
            SupportRequest.message_from_support_id == message_from_support_id
        )
    ).scalar_one_or_none()
    return ticket




