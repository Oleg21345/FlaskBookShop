from .BaseModel import async_ses
from .databasemodel import User, Books
from sqlalchemy import select

class MetodForSql:

    @classmethod
    def creater_account(cls, username: str, age: int, password: str):
        with async_ses as session:
            user = User(username=username, age=age, password=password)

            session.add(user)

            session.commit()
            session.refresh(user)
            return user # Це об'єкт класу User

    @classmethod
    def creater_book(cls, book_name: str, price: int, disc: str):
        with async_ses as session:
            book = Books(name_book=book_name, discription=disc, price=price)

            session.add(book)

            session.commit()
            session.refresh(book)
            return book # Це об'єкт класу User


    @classmethod
    def get_users(cls, data):
        with async_ses as session:
            stmt = select(User).filter(User.username==data)
            users = session.execute(stmt)
            user = users.scalars().first()
            return user # Щоб зробити lofin_user в нього має обов'язково передаватися об'єкт
            # а не якийсь його параметр, моя помилка була що я передавав тільки username або
            # тільки user.id


    @classmethod
    def get_books(cls):
        with async_ses as session:
            query = select(Books).filter_by(autor_id=None)
            result = session.execute(query)
            res = result.scalars().all()
            return res

    @classmethod
    def get_books_for_sell(cls, current):
        with async_ses as session:
            query = select(Books).filter_by(autor_id=current)
            result = session.execute(query)
            res = result.scalars().all()
            return res

    @classmethod
    def get_buy_book(cls, buy_book, current_id):
        with async_ses as session:
            query = select(Books).filter_by(name_book=buy_book)
            result = session.execute(query)
            res = result.scalars().first()

            user_query = select(User).filter_by(id=current_id)
            user_result = session.execute(user_query)
            current_user = user_result.scalars().first()

            print(current_user)
            if res:
                if current_user.budget < res.price:
                    return None
                else:
                    res.autor_id = current_user.id
                    current_user.budget -= res.price

                    session.commit()
                    session.flush()


                    return {"name_book": res.name_book, "price": res.price}

            return None

    @classmethod
    def get_sell_book(cls, sell, current_id):
        with async_ses as session:
            query = select(Books).filter_by(name_book=sell)
            result = session.execute(query)
            res = result.scalars().first()

            user_query = select(User).filter_by(id=current_id)
            user_result = session.execute(user_query)
            current_user = user_result.scalars().first()

            print(current_user)
            if res:
                res.autor_id = None
                print(res.price)
                print(current_user.budget)
                current_user.budget += res.price


                session.commit()
                session.flush()

                return {"name_book": res.name_book, "price": res.price}

            return None

    @classmethod
    def get_autor_id(cls, curr):
        with async_ses as session:
            query = select(Books).filter_by(autor_id=curr)
            result = session.execute(query)
            res = result.scalars().all()
            return res