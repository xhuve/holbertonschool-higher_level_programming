from sqlalchemy import sa, String
from sqlalchemy.orm import Mapped, mapped_colum
from sqlalchemy.ext.declarative import declarative_base

db = sa.create_engine("mysql://root:root@localhost:3306/hbtn_0e_6_usa")

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id: Mapped[int] = mapped_colum(primay_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_colum(String(128), nullable=False) 