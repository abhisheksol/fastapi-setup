# app/models.py
from email.policy import default

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship



# User

class UserModel(Base):

    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key= True,
        default= uuid.uuid4
    )
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)

    books = relationship("Book", back_populates="user")

    



class Book(Base):
    __tablename__ = "books"

    id = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4
        , primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="books")
    price = Column(Float, nullable=False)


class Product(Base):
    __tablename__ = "products"

    # uuid id
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)


# loan case 

class CaseManagementModel(Base):
    __tablename__ = "casemanagement"

    id = Column(
        UUID(as_uuid=True),
        primary_key= True,
        default= uuid.uuid4
    ) 
    loan_amt= Column(Float, nullable=False, default=0)
    loan_duration= Column(Integer, nullable=False, default=0)



    