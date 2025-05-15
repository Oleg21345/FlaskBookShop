
import random
from typing import Optional
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

class Category(BaseModel):
    user_id: int
    name: str
    mess: str

class MessageUser(BaseModel):
    user_id: int
    username: str
    user_mess: Optional[str] = None

# Підключення до MongoDB (синхронне)
client = MongoClient("mongodb://localhost:27017")
db = client["message"]
mess_collection = db["mess"]

# Ініціалізація (фейкова для симетрії з async)
def init_db():
    print("✅ MongoDB ініціалізовано (синхронно)")

class MangoMethod:

    # Лог для перевірки виклику функції
    call_count = 0

    @staticmethod
    def add_message(username: str, user_mess: str):
        MangoMethod.call_count += 1
        try:
            print(f"👉 Починаємо додавання повідомлення... Виклик №{MangoMethod.call_count}")
            user_id = random.randint(1, 10000)
            user = {
                "user_id": user_id,
                "username": username,
                "user_mess": user_mess
            }
            mess_collection.insert_one(user)
            print("✅ Повідомлення збережено")
        except Exception as err:
            print(f"❌ Сталась помилка: {err}")

    @staticmethod
    def get_all_message():
        try:
            messages = list(mess_collection.find())
            return messages
        except Exception as err:
            print(f"❌ Сталась помилка: {err}")
            return []




# class Category(BaseModel):
#     user_id: int
#     name: str
#     mess: str
#
#
# class Message_User(Document):
#     user_id: int
#     username: str
#     user_mess: Optional[str] = None
#
#     class Settings:
#         name = "mess"
#
# client = AsyncIOMotorClient("mongodb://localhost:27017")
#
# async def init_db():
#     await init_beanie(database=client["message"], document_models=[Message_User])
#     print("✅ MongoDB ініціалізовано")
#
# class MangoMethod:
#
#     @staticmethod
#     async def add_message(username, user_mess):
#         try:
#             print("👉 Починаємо додавання повідомлення...")
#             user_id = random.randint(1, 10000)
#             user_1 = Message_User(user_id=user_id, username=username, user_mess=user_mess)
#             await user_1.insert()
#             print("✅ Повідомлення збережено")
#         except Exception as err:
#             print(f"❌ Сталась помилка: {err}")
#
#     @staticmethod
#     async def get_all_message():
#          try:
#              data = await Message_User.find_all().to_list()
#              return data
#
#          except Exception as err:
#              print(f"Сталась помилка: {err}")
#              return []
#



# if __name__ == "__main__":
#     async def main():
#         await init_db()
#         await MangoMethod.add_message("Oleg", "He guys!")
#
#     asyncio.run(main())




