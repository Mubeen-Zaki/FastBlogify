from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..schemas import ShowBlog, Blog, UpdateBlog, User
from ..database import get_db
from typing import List
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(request_body : Blog, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.write(request_body, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
async def get_blog(db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.read_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
async def get_blog(id : int, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.read(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, new_blog: UpdateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update(id, new_blog, db)