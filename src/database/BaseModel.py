from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///books.db", echo=False)

Session = sessionmaker(bind=engine)

async_ses = Session()

class Base(DeclarativeBase):
    pass


