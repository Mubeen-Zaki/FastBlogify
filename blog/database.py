from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Creating the engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
connect_args = {"check_same_thread" : False} #Allows multi-threading with the same connection to the same db(which is restricted in fastapi)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

Base = declarative_base()
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    session = session_factory()
    try:
        yield session
    finally:
        session.close()