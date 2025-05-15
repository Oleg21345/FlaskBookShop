import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import Length, EqualTo, NumberRange, DataRequired,  ValidationError
from src.database.databasemodel import User
from src.database.BaseModel import async_ses
from sqlalchemy import select


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        with async_ses as session:
            user_cheack = username_to_check.data
            stmt = select(User).filter_by(username=user_cheack )
            res = session.execute(stmt)
            user = res.scalars().first()
            if user:
                raise ValidationError("Таке ім'я користувача вже зайняте! Будь ласка спробуйте ввести інше")

        if not user_cheack .isalpha():
            raise ValidationError("Ім'я користувача може містити лише літери.")

        if not user_cheack.isalpha():
            raise ValidationError("Ім'я користувача має починатися з великої літери.")

        if not user_cheack [0].isupper():
            raise ValidationError("Ім'я користувача повинно починатися з великої літери.")

    def validate_password_main(self, password_to_check):
        pas = password_to_check.data
        if not re.search(r"[A-Z]", pas):
            raise ValidationError("Ваш пароль має в собі утримувати хоча б одну велику літеру")


    username = StringField(label="Ім'я", validators=[Length(min=2, max=30, message="Ім'я має бути не менше 2 і не більше 30 символів"),DataRequired(message="Поле імені пусте:(")])
    age = IntegerField(label="Роки", validators=[NumberRange(min=7, max=120, message="Вам не може бути стільки років"),DataRequired(message="Поле років пусте:(")])
    password_main = PasswordField(label="Пароль", validators= [Length(min=8, max=64, message="Пароль надто короткий"),DataRequired(message="Поле паролю пусте:(")])
    password_conf = PasswordField(label="Повторити пароль",validators=[EqualTo("password_main", message="Паролі не співпадають"), DataRequired(message="Поле паролю пусте:(")])
    submit = SubmitField(label="Підтвердити")


class BookForm(FlaskForm):
    name_book = StringField(label="Назва книги", validators=[Length(min=3, max=200, message="Назва книги має бути не менше 3 і не більше 200 символів!")])
    discription = TextAreaField(label="Опис", validators=[Length(max=500, message="Опис має бути не більше 500 символів!")])
    price = IntegerField(label="Ціна", validators=[NumberRange(min=100)])
    submit = SubmitField(label="Підтвердити")

class LoginForm(FlaskForm):

    username = StringField(label="Ім'я", validators=[DataRequired()])
    password_main = PasswordField(label="Пароль", validators=[DataRequired()])
    submit = SubmitField(label="Увійти")

class BuyForm(FlaskForm):
    submit = SubmitField(label="Купити")

class SellForm(FlaskForm):
    submit = SubmitField(label="Продати")
