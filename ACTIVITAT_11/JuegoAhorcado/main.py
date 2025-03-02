from fastapi import FastAPI
from routes import game

app = FastAPI()

app.include_router(game.router)

@app.get("/")
def root():
    return {"mensaje": "API del juego Ahorcado"}
