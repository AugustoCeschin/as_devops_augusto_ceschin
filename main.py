from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"mensagem": "Olá Mundo! Bem-vindo à API utilizada na AS - DevOps"}

# http://127.0.0.1:8000/primeiro-endpoint
@app.get("/primeiro-endpoint")
def read_root():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}


# http://127.0.0.1:8000/moeda
@app.get("/moeda")
def jogar_moeda():
    return {"resultado": random.choice(["cara", "coroa"])}