# 📝 FastAPI Auth API

> REST API для регистрации и логина пользователей.
> Реализовано с использованием **FastAPI**, **SQLModel** и **PostgreSQL**.

---

## 🚀 Возможности

✅ Регистрация пользователя (`POST /register`)
✅ Авторизация по логину и паролю (`POST /login`)
✅ Асинхронное взаимодействие с базой PostgreSQL
✅ Простое тестирование через Postman

---

## 🧰 Стек технологий

- 🌐 [FastAPI](https://fastapi.tiangolo.com/)
- 🐘 [PostgreSQL](https://www.postgresql.org/)
- 🔄 [SQLModel](https://sqlmodel.tiangolo.com/)
- ⚡ [Uvicorn](https://www.uvicorn.org/)
- 🧠 [Pydantic](https://docs.pydantic.dev/)
- 📦 [asyncpg](https://magicstack.github.io/asyncpg/)

---

## 🛠️ Установка и запуск

```bash
# 📁 Клонируй репозиторий
git clone https://github.com/dunanhub/auth_api.git
cd auth_api
```

```bash
# 🧪 Создай виртуальное окружение

# Для Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Для Windows
python -m venv .venv
.venv\Scripts\activate
```

```bash
# 📦 Установи зависимости
pip install -r requirements.txt
```

```env
# ⚙️ Настрой файл .env
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/auth_api
```

> 💡 Убедись, что база данных `notes_db` существует в PostgreSQL и PostgreSQL-сервер запущен.

```bash
# 🚀 Запусти FastAPI приложение
uvicorn app.main:app --reload
```

---

## 📬 Примеры API-запросов

### ➕ POST `/register` — Регистрация:

```http
POST http://localhost:8000/register
```

```json
{
  "username": "user",
  "password": "1234"
}
```

✅ Ответ:

```json
{
  "id": 1,
  "username": "user"
}
```

### ➕ POST `/login` — Логин:

```http
POST http://localhost:8000/login
```

```json
{
  "username": "user",
  "password": "1234"
}
```

✅ Ответ:

```json
{
  "message": "Login successful",
  "username": "user"
}
```

---

## 📂 Структура проекта

```
auth_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes.py
├── .env
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚖️ Лицензия

Этот проект лицензирован под MIT. См. файл [LICENSE](./LICENSE) для подробностей.
