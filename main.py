from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"mensagem": "Olá Mundo!"}

# http://127.0.0.1:8000/primeiro-endpoint
@app.get("/primeiro-endpoint")
def read_root():
    return {"mensagem": "Primeiro Endpoint"}