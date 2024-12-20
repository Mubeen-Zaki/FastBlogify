from sqlalchemy.orm import Session
from .. import models
from fastapi import HTTPException, status

def read_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def read(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id : {id} does not exist in the db!")
    else:
        return blog

def write(request_body, db : Session):
    new_blog = models.Blog(title=request_body.title, body=request_body.body, published=request_body.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'message' : f"Blog created with title : {request_body.title}"}

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id : {id} does not exist in the db!")
    db.delete(blog)
    db.commit()
    return {"message" : "Blog deleted succesfully from the db!"}

def update(id: int, new_blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    if new_blog.title:
        db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.title: new_blog.title}, synchronize_session=False)
    if new_blog.body:
        db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.body: new_blog.body}, synchronize_session=False)
    if new_blog.published:
        db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.published: new_blog.published}, synchronize_session=False)
    db.commit()
    return {"message" : "Blog details updated successfully!"}