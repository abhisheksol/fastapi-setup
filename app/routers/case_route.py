

# from app import crud, schemas
# from app.database import get_db

from uuid import UUID
from app import auth
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud, schemas
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


from fastapi import Depends

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = auth.verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


router = APIRouter(
    prefix="/cases",
    tags=["Cases"]
)



@router.post("/case/", response_model = schemas.CaseManagementResponse)
def create_case(case: schemas.CaseMangementCreate, db: Session =Depends(get_db)):
    return crud.create_case(db, case)




@router.get("/get_cases/", response_model = schemas.CaseManagementResponse)
def get_case(db: Session = Depends(get_db)):
    return crud.get_case(db)


@router.get("/case/{case_id}", response_model = schemas.CaseManagementResponse)
def get_case_by_id(
    case_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    case= crud.get_case_by_id(db, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


