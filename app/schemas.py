# app/schemas.py

from uuid import UUID
from pydantic import BaseModel, EmailStr

class BookCreate(BaseModel):
    title: str
    author: str
    price: float


class BookResponse(BookCreate):
    id: UUID

    model_config = {
        "from_attributes": True
    }


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str


class productResponse(ProductCreate):
    # uuid: str
    id: UUID
    

    model_config = {
        "from_attributes": True
    }


class CaseMangementCreate(BaseModel):
    loan_amt : float
    loan_duration: int

    
class CaseManagementResponse(CaseMangementCreate):
    id: UUID

    model_config ={
        "from_attributes" : True
    }


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr

    model_config = {"from_attributes": True}


class Token(BaseModel):   
    access_token: str
    token_type: str