# FlaskBookShop

A full-featured **online book shop** built with **Flask**, **MongoDB**, and **SQLAlchemy**, featuring real-time chat functionality and secure user authentication.

---

## 🚀 Features

- 🧑‍🤝‍🧑 **Authentication & Authorization**
  - User registration, login, logout.
  - Password hashing using **Flask-Bcrypt**.
  - Session management via **Flask-Login**.

- 📚 **Book Management**
  - Browse, search, and view books.
  - Admin panel for managing books (optional).

- 💬 **Real-time Chat**
  - Implemented using **Flask** + **MongoDB**.
  - Users can chat in real-time.
  - Messages are stored in **MongoDB** for persistence.

- 🗄️ **Database**
  - **MongoDB** for chat messages.
  - **SQLAlchemy (PostgreSQL/MySQL/SQLite optional)** for book and user data.

- 📝 **Forms**
  - User input and validation using **Flask-WTF** and **WTForms**.

- 🔒 **Security**
  - Password hashing (**Flask-Bcrypt**).
  - CSRF protection via **Flask-WTF**.
  - Secure session management.

- 🎨 **Frontend**
  - HTML templates using **Jinja2**.
  - Template filters and macros for reusable components.

---

## 🛠 Technologies & Libraries

- **Backend**: Flask 3.1  
- **Authentication & Security**: Flask-Bcrypt, Flask-Login, Flask-WTF  
- **Database**: SQLAlchemy (for main app), MongoDB (for chat)  
- **Forms**: WTForms  
- **Templating**: Jinja2, MarkupSafe  
- **Others**: Pydantic, Annotated-types, Typing-extensions, Werkzeug  

---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/Oleg21345/FlaskBookShop.git
cd FlaskBookShop
