from sqlalchemy import sa, String
from sqlalchemy.orm import Mapped, mapped_colum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id: Mapped[int] = mapped_colum(primay_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_colum(String(128), nullable=False) 