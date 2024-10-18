"""Models for database"""
from typing import Annotated

from sqlalchemy import BigInteger, ForeignKey, String, text, Numeric, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_40 = Annotated[str, 40]


class Base(DeclarativeBase):
    """Base class for all models"""
    type_annotation_map = {
        str_40: String(40)
    }


class User(Base):
    """Model for app_user table"""
    __tablename__ = 'app_user'
    user_id: Mapped[int_pk]
    telegram_id: Mapped[int] = mapped_column(BigInteger())

    card: Mapped['User'] = relationship(back_populates='user', cascade='all, delete')


class WordGroup(Base):
    """Model for word_group table"""
    __tablename__ = 'word_group'
    group_id: Mapped[int_pk]
    alias: Mapped[str_40]

    card: Mapped['WordGroup'] = relationship(back_populates='group', cascade='all, delete')


class Card(Base):
    """Model for card table"""
    __tablename__ = 'card'
    card_id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey('app_user.user_id'))
    ru_word: Mapped[str_40]
    en_word: Mapped[str_40]
    group_id: Mapped[int | None] = mapped_column(ForeignKey('word_group.group_id'))
    success_rate: Mapped[float] = mapped_column(Numeric(2, 1), server_default=text('0.0'))
    display_count: Mapped[int] = mapped_column(server_default=text('0'))

    user: Mapped['User'] = relationship(back_populates='card', cascade='all, delete')
    group: Mapped['WordGroup'] = relationship(back_populates='card', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("success_rate >= 0.0", name="check_success_rate_positive"),
        CheckConstraint("display_count >= 0", name="check_countdown_positive"),

    )

