#!/usr/bin/python3
"""Learning SQL"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Learning SQL"""
    __tablename__ = 'states'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)