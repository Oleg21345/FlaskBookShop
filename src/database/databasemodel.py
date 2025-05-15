from .BaseModel import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from src.flask_engine.app_config import bcrypt
from src.flask_engine.app_config import login_manager
from src.database.BaseModel import async_ses
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    with async_ses as session:
        return session.query(User).get(int(user_id))

class User(Base, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    password_main: Mapped[str]
    budget: Mapped[int] = mapped_column(default=1000)

    @property
    def pritty_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]}.{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}"

    @property
    def password(self):
        return self.password_main

    @password.setter
    def password(self, plain_text_password):
        self.password_main = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    def check_password_hash(self, attempted_password):
        return bcrypt.check_password_hash(self.password_main, attempted_password)

class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_book: Mapped[str] = mapped_column(String(200))
    autor_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    discription: Mapped[str] = mapped_column(String(500))
    price: Mapped[int]

    autor: Mapped["User"] = relationship("User", backref="books")







