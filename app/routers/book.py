# app/routers/book.py

from app.routers import case_route
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud, schemas

router = APIRouter(
    prefix="/django/books",
    tags=["Books"]
)

@router.post("/", response_model=schemas.BookResponse)
def create(book: schemas.BookCreate,
            db: Session = Depends(get_db),
            current_user = Depends(case_route.get_current_user)):
    print("---------- current_user -    ----------->", current_user)
    return crud.create_book(db, book, current_user["sub"])


@router.get("/", response_model=list[schemas.BookResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_one(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}


@router.post("/product/", response_model=schemas.productResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

