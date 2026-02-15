from sqlmodel import Session, create_engine, SQLModel
import os.path


sqlite_file_mame = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_mame}"

if not os.path.exists(sqlite_url):
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
