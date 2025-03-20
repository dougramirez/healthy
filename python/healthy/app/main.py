from fastapi import FastAPI
from app.routers import healthy

app = FastAPI()

app.include_router(healthy.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the healthy API!"}
