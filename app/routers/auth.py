from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserResponse, db: Session = Depends(get_db)):
    hashed_pw = auth.hash_password(user.password)

    db_user = models.UserModel(
        email=user.email,
        hash_password=hashed_pw
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.UserModel).filter(models.UserModel.email == user.email).first()

    if not db_user or not auth.verify_password(user.password, db_user.hash_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = auth.create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
