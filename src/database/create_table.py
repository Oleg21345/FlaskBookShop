from .BaseModel import engine, Base

def create_table():
    with engine.begin() as conn:
        Base.metadata.create_all(conn)

def drop_tabl():
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
