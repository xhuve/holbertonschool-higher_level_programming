#!/usr/bin/python3
"""Learning SQLAlchemy"""

if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
        )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = session.query(State).order_by(State.id).first()
        if query is None:
            print("Nothing")
        else:
            print(f"{query.id}: {query.name}")
