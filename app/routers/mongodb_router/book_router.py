# app/routers/books.py

from fastapi import APIRouter
from app.schema.mongodb_schemas import Mongo_BookCreate
from app.database import books_collection as mongo_db
from bson import ObjectId
router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/mongo-db/add-book")
async def create_book_mongodb(book: Mongo_BookCreate):

    book_dict = book.model_dump()

    result = await mongo_db.insert_one(book_dict)

    return {
        "message": "Book created",
        "id": str(result.inserted_id)
    }



@router.get("/mongo-db/get-books")
async def get_books_mongodb():
    books = []
    async for book in mongo_db.find():
        books.append(
            {
                "id": str(book["_id"]),
                "title": book["title"],
                "author": book["author"],
                "price": book["price"]
            }
        )
    return books



# update the book
@router.put("/mongo-db/update-book/{book_id}")
async def update_book_mongodb(book_id: str, book: Mongo_BookCreate):

    book_dict = book.model_dump()

    print("=========== book_dict -    ----------->", book_dict)

    result = await mongo_db.update_one({"_id": ObjectId(book_id)}, {"$set": book_dict})

    if result.modified_count == 1:
        return {
            "message": "Book updated"
        }
    else:
        return {
            "message": "Book not found"
        }
    


@router.delete("/mongo-db/delete-book/{book_id}")
async def delete_book_mongodb(book_id: str, book: Mongo_BookCreate):

    result = await mongo_db.delete_one({"_id": ObjectId(book_id)})

    if result.deleted_count == 1:
        return {
            "message": "Book deleted"
        }
    else:
        return {
            "message": "Book not found"
        }
