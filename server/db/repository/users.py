from sqlalchemy.orm import Session
from server.schemas.users import UserCreate
from server.db.models.users import User
from server.core.hashing import Hasher


def create_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
