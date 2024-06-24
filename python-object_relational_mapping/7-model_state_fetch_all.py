#!/usr/bin/python3
"""Learning SQLAlchemy"""

from model_state import Base, State
from sys import argv
from sqlalchemy import Select, create_engine



if __name__ == '__main__':
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    select_query = Select(State).order_by(State.c.id)

    with engine.connect() as conn:
        for row in conn.execute(select_query):
            print(row)
