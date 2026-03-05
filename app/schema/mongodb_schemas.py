# app/schemas.py
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr

class Mongo_BookCreate(BaseModel):
    title: str
    author: str
    price: float


class Mongo_BookResponse(Mongo_BookCreate):
    id: Optional[str]

    model_config = {
        "from_attributes": True
    }

