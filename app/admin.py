# app/admin.py
from sqladmin import Admin, ModelView
from app.database import engine
from app.models import Book

class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.title, Book.author, Book.price]

def setup_admin(app):
    admin = Admin(app, engine)
    admin.add_view(BookAdmin)
