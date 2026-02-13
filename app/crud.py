# app/crud.py

from uuid import UUID
from sqlalchemy.orm import Session
from .models import Book, CaseManagementModel, Product
from .schemas import BookCreate, CaseMangementCreate, ProductCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        price=book.price
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book



def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



def create_case(db: Session, case: CaseMangementCreate):
    db_case = CaseManagementModel(
        loan_amt = case.loan_amt,
        loan_duration = case.loan_duration
    )
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case



# get cases

def get_case(db: Session):
    return db.query(CaseManagementModel).all()


def get_case_by_id(db : Session, case_id: UUID):
    return db.query(CaseManagementModel).filter(CaseManagementModel.id == case_id).first() 