from fastapi import FastAPI
from routes.user import router as userRoutes 
from routes.blog import router as blogRoutes
from config.db import connect_db

app=FastAPI()

connect_db()

app.include_router(userRoutes,prefix="/user",tags=["Users"])
app.include_router(blogRoutes,prefix="/blog",tags=["Blogs"])

@app.get("/")
def started():
    return {"message":"Hello,World from main!"}


