from fastapi import FastAPI
from database import Base, engine
import models

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def baca_root ():

    return {"Pesan": "Halo, ini API Kasir Pintar By Syad"}