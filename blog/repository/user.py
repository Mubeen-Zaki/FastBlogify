from sqlalchemy.orm import Session
from .. import models
from fastapi import HTTPException, status
from ..hashing import Hash

def create(request, db: Session):
    name_already_exists = db.query(models.User).filter(models.User.name==request.name).first()
    if name_already_exists:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"User with name {request.name} already exists in the db. Use other names!")
    mail_already_exists = db.query(models.User).filter(models.User.email==request.email).first()
    if mail_already_exists:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"User with mail {request.name} already exists in the db.")
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    return {"message" : "New user added!"}

def read(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found in the db!")
    return users

def read(id: int, db: Session):
    users = db.query(models.User).filter(models.User.id==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No users found in the db with id : {id}!")
    return users