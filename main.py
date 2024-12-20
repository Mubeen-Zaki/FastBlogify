from fastapi import FastAPI
from typing import Optional
from models import Blog

app = FastAPI()

@app.get('/blog')
async def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published == True:
        return {"data" : f"{limit} published blogs from the database"}
    else:
        return {"data" : f"{limit} blogs from the database"}

@app.get('/blog/unpublished')
async def get_unpublished():
    return {'data' : 'All unpublished blogs'}

@app.get('/blog/{id}')
async def show(id: int):
    return {'data' : id}

@app.get('/blog/{id}/comments')
async def comments(id, limit=10):
    comments = ["comment" + str(x + 1) for x in range(10)]
    return {'data': {'comments' : comments}}

@app.post('/blog')
def create_blog(blog : Blog):
    return {'message' : "Blog is created",
            'data' : blog}