from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.schemas.users import UserCreate, ShowUser
from server.db.session import get_db
from server.db.repository.users import create_user

router = APIRouter()


@router.post("/", tags=["users"], response_model=ShowUser)
def creat_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(user, db)

    return new_user
