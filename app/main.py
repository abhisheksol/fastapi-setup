# app/main.py
from app.admin import setup_admin

from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import book , case_route, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book API")

app.include_router(book.router)
app.include_router(case_route.router)
app.include_router(auth.router)


setup_admin(app)
