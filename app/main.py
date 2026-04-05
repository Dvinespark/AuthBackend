from fastapi import FastAPI
from app.routers import user
from app.db.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router, prefix="/auth")