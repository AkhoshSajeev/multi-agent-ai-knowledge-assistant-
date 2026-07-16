from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.schemas import (
    UserRegister,
    UserResponse,
    Token,
)
from app.auth.service import create_user, login_user
from app.db.database import get_db
from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    new_user = create_user(
        db=db,
        user=user,
    )

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return new_user


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    token = login_user(
        db=db,
        email=form_data.username,   # username field contains the email
        password=form_data.password,
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return Token(
        access_token=token,
        token_type="bearer",
    )


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user