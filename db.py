from typing import Annotated
from sqlmodel import Session, create_engine
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel

sqlite_name = 'db.sqlite3'
sql_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sql_url)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session,Depends(get_session)]
