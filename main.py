from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def baca_root ():

    return {"Pesan": "Halo, ini API Kasir Pintar By Syad"}