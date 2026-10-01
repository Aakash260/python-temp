from fastapi import Depends

from models.blog import Blog
from schemas.blog import BlogSchema
from sqlalchemy.orm import Session 
from config.db import get_db

def get_allBlogs(db:Session=Depends(get_db)): 
    return db.query(Blog).all()

def create_blog(blog:BlogSchema,db:Session = Depends(get_db)):
    new_blog=Blog(title=blog.title,content=blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
def delete_blog(blog_id:int,db:Session=Depends(get_db)):
    blog=db.query(Blog).filter(Blog.id==blog_id).first()
    if not blog:
        return {"message":"Blog not found"}
    db.delete(blog)
    db.commit()
    return {"message":"Blog deleted successfully"}


def update_blog(blog_id:int,Blog:BlogSchema,db:Session=Depends(get_db)):
    blog=db.query(Blog).filter(Blog.id==blog_id).first()
    if not blog:
        return {"message":"Blog not found"}
    blog.title=Blog.title
    blog.content=Blog.content
    db.commit()
    db.refresh(blog)
    return blog

