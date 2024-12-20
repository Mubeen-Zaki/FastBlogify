from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..schemas import ShowBlog, Blog, UpdateBlog, ShowUser, User
from ..database import get_db
from typing import List
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request : User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[ShowUser], status_code=status.HTTP_200_OK)
async def show_users(db: Session = Depends(get_db)):
    return user.read(db)

@router.get('/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK)
async def show_user(id: int, db: Session = Depends(get_db)):
    return user.read(id, db)