from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(
    user_in: schemas.UserCreate, db: Session = Depends(deps.get_db)
):
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.create(db=db, user_in=user_in)
    return user

@router.get("/me", response_model=schemas.User)
def read_user_me(
    current_user: models.User = Depends(deps.get_current_user)
):
    return current_user

