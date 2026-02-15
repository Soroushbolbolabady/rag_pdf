from fastapi import FastAPI

from src.db.create_db import create_db_and_tables


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
