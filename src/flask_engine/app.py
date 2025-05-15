from flask import render_template, redirect, url_for, flash, request
from .forms.forms_to_register import RegisterForm, LoginForm,BuyForm, SellForm, BookForm
from .app_config import app
from src.database.metod_class import MetodForSql
from flask_login import login_user, logout_user, login_required, current_user
from flask_socketio import send
from .app_config import socketio
from src.mongodatabase.config_mongo import MangoMethod



@app.route("/home")
@app.route("/")
def index():

    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    msg = data.get("msg", "").strip()
    username = current_user.username

    if not msg:
        print("⚠️ Порожнє повідомлення — ігноровано")
        return

    send(data, broadcast=True)
    print(f"✅ Розіслано від {username}: {msg}")

    if username != "Service message":
        try:
            MangoMethod.add_message(username, msg)
            print("💾 Повідомлення збережено")
        except Exception as e:
            print(f"❌ Помилка збереження: {e}")



@app.route("/discuse")
def discussion():
    username = current_user.username

    message = MangoMethod.get_all_message()
    return render_template("discuse_chat/discussion.html", username=username, message=message)


@app.route("/books", methods=["GET", "POST"])
@login_required
async def books_shop():
    buy_form = BuyForm()
    book = MetodForSql.get_books()
    current = current_user.id

    if request.method == "POST":
        buy_book = request.form.get("buy_book")
        if buy_book:
            b_book_object = MetodForSql.get_buy_book(buy_book, current)
            if b_book_object:
                flash(f"Вітаю! Ти купив книгу {b_book_object['name_book']} за {b_book_object['price']}$", category="success")
            else:
                flash("У вас недостатньо монет для покупки цієї книги", category="danger")

        return redirect(url_for("books_shop"))

    if request.method == "GET":
        return render_template("books_discussions.html", book=book, buy_form=buy_form)

@app.route("/post_book", methods=["GET", "POST"])
def post_books():
    form = BookForm()
    if form.validate_on_submit():
        user_book = MetodForSql.creater_book(book_name=form.name_book.data,
                                             disc=form.discription.data, price=form.price.data)

        flash("Ви виклали свою книгу, вітаю!", category="success")
        return redirect(url_for("books_shop"))
    if form.errors != {}:
        for err_message in form.errors.values():
            for err in err_message:
                flash(err, category="danger")

    return render_template("post_book.html", form=form)

@app.route("/sold_book", methods=["GET", "POST"])
def sold_book():
    sold_form = SellForm()
    autor_id = MetodForSql.get_autor_id(current_user.id)
    book = MetodForSql.get_books_for_sell(current_user.id)
    if sold_form.validate_on_submit():
        sell_book = request.form.get("sell_book")
        if sell_book:
            s_book_object = MetodForSql.get_sell_book(sell_book, current_user.id)
            if s_book_object:
                flash(f"Ви продали книгу {s_book_object['name_book']} за {s_book_object['price']}$", category="success")
            else:
                flash("Не вдалося продати книгу. Можливо, вона вже продана.", category="danger")
        return redirect(url_for("sold_book"))

    print(f"Book_id{book}")
    for autor in autor_id:
        print(f"Autor Id{autor.id}")
    return render_template("sell_book.html", book=book, sold_form=sold_form)




@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = MetodForSql.creater_account(username=form.username.data,
                                                age=form.age.data,
                                                password=form.password_main.data)
        login_user(user)
        flash(f"Ви успішно створили акаунт! {user.username}", category="success")
        return redirect(url_for("index"))
    if form.errors != {}:
        for err_message in form.errors.values():
            for err in err_message:
                flash(err, category="danger")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = MetodForSql.get_users(form.username.data)
        if attempted_user and attempted_user.check_password_hash(
                form.password_main.data
        ):
            login_user(attempted_user)
            flash(f"Ви успішно увійшли! {attempted_user.username}", category="success")
            return redirect(url_for("index"))

        else:
            flash("Ім'я або пароль не сходяться", category="danger")


    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("Ви вийшли з акаунту!", category="info")
    return redirect(url_for("index"))

