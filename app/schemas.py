# app/schemas.py

from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    price: float


class BookResponse(BookCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class product(BaseModel):
    name: str
    price: float
    description: str


class productResponse(product):
    id: int

    model_config = {
        "from_attributes": True
    }