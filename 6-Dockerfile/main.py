from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hola Mundo!!"}

@app.get("/numero")
def numero():
    #funcion que va a regresar un numero aleatorio entre el 1 y el 100
    numero = random.randint(1, 100)
    return {"numero": numero}