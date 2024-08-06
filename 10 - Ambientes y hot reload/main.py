# Paso 1: Instalar dependencias
# Ejecuta en la terminal: pip install fastapi pymongo uvicorn

# Paso 2: Crear la aplicación FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List

app = FastAPI()

# Paso 3: Conectar a MongoDB
client = MongoClient('mongodb://admin:1234@db_mongo:27017/')
db = client['nombre_de_tu_base_de_datos']
collection = db['nombre_de_tu_coleccion']

# Paso 4: Definir los modelos de datos
class Item(BaseModel):
    nombre: str
    edad: int = None

class ItemInDB(Item):
    id: str

# Paso 5: Definir los endpoints

@app.get('/')
async def read_root():
    return {'message': 'Hello World'}
# Este endpoint crea un nuevo item en la base de datos
@app.post('/items/', response_model=ItemInDB, description="Crea un nuevo item en la base de datos")
async def create_item(item: Item):
    result = collection.insert_one(item.dict())
    return ItemInDB(id=str(result.inserted_id), **item.dict())

# Este endpoint obtiene un item de la base de datos por su ID
@app.get('/items/', response_model=List[ItemInDB], description="Se obtienen todos los items de la base de datos")
async def read_items():
    items = list(collection.find())
    for item in items:
        item['id'] = str(item['_id'])
        del item['_id']
    return items

#Este endpoint borra un item de la base de datos por su ID
@app.delete('/items/{item_id}', description="Borra un item de la base de datos por su ID")
async def delete_item(item_id: str):
    result = collection.delete_one({'_id': ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'message': 'Item deleted'}