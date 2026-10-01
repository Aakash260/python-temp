from fastapi import FastAPI
from routes.user import router as userRoutes 
from config.db import connect_db

app=FastAPI()

connect_db()

app.include_router(userRoutes,prefix="/user",tags=["Users"])

@app.get("/")
def started():
    return {"message":"Hello,World!"}


