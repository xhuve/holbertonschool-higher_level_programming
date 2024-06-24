#!/usr/bin/python3
"""Learning SQLAlchemy"""




if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import Select, create_engine

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    select_query = Select(State).order_by(State.c.id)

    print(select_query)

    with engine.connect() as conn:
        print(conn.execute(select_query).fetchall())
