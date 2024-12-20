from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# async def create_blog(request_body : Blog, db : Session = Depends(get_db)):
#     new_blog = models.Blog(title=request_body.title, body=request_body.body, published=request_body.published, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return {'message' : f"Blog created with title : {request_body.title}"}

# @app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[ShowBlog], tags=['blogs'])
# async def get_blog(db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
# async def get_blog(id : int, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id : {id} does not exist in the db!")
#     else:
#         return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# async def delete_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     # blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id : {id} does not exist in the db!")
#     db.delete(blog)
#     db.commit()
#     return {"message" : "Blog deleted succesfully from the db!"}

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# async def update_blog(id: int, new_blog: UpdateBlog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
#     if new_blog.title:
#         db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.title: new_blog.title}, synchronize_session=False)
#     if new_blog.body:
#         db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.body: new_blog.body}, synchronize_session=False)
#     if new_blog.published:
#         db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.published: new_blog.published}, synchronize_session=False)
#     db.commit()
#     return {"message" : "Blog details updated successfully!"}

# @app.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
# async def create_user(request : User, db: Session = Depends(get_db)):
#     name_already_exists = db.query(models.User).filter(models.User.name==request.name).first()
#     if name_already_exists:
#         raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"User with name {request.name} already exists in the db. Use other names!")
#     mail_already_exists = db.query(models.User).filter(models.User.email==request.email).first()
#     if mail_already_exists:
#         raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"User with mail {request.name} already exists in the db.")
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     return {"message" : "New user added!"}

# @app.get('/user', response_model=List[ShowUser], status_code=status.HTTP_200_OK, tags=['users'])
# async def show_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found in the db!")
#     return users

# @app.get('/user/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK, tags=['users'])
# async def show_user(id: int, db: Session = Depends(get_db)):
#     users = db.query(models.User).filter(models.User.id==id).first()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No users found in the db with id : {id}!")
#     return users