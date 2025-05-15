from pydantic import BaseModel


class SBooksAdd(BaseModel):
    name: str
    autor: str


class SBooks(SBooksAdd):
    id: int


class USerADD(BaseModel):
    username: str
    age: int
    password_main: str

class Users(SBooksAdd):
    id: int








