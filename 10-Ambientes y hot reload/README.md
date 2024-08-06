# Ambientes y Hot Reload

En primer lugar crearemos un nuevo archivo **Dockerfile.dev** que lo utilizaremos para desarrollo.

Pero para detectar los cambios que hagamos en nuestra aplicación vamos a tener que utilizar una herramienta que nos permita hacer **hot reload** que puede ser **watchdog** o **python-devtools**.

En este caso haremos un ejemplo con **watchdog** y veremos los cambios que le haremos al **Dockerfile.dev**

### Configuración Dockerfile.dev
```
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Instala watchdog
RUN pip install watchdog

# Copia el contenido del directorio actual en /app
COPY . .

# Expone el puerto 8000 para la aplicación
EXPOSE 8000
```
Como podemos ver en el codigo de arriba se han realizado algunos cambios que vamos a explicar a continuación.

```
RUN pip install watchdog
```
Este primer cambio instala la biblioteca **watchdog** que se necesita para detectar cambios en los archivos y reiniciar la aplicación automaticamente.

El segundo cambio que notamos es que se eliminó la ultima línea con el comando **CMD** y todos sus parámetros, esto es porque abordaremos el hot reload desde el docker-compose.

### Configuración docker-compose-dev.yml

Además de crear un nuevo Dockerfile, debemos crear un nuevo docker compose que en este caso se llamará **docker-compose-dev.yml** cuyo código se ve a continuación.

```
version: "3.9"
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    links:
      - db_mongo
    volumes:
      - .:/app
  db_mongo:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=1234
    volumes:
      - mongo-data:/data/db
    command: >
      watchmedo auto-restart --patterns=*.py --recursive -- 
      uvicorn main:app --host 0.0.0.0 --port 8000 --reload
volumes:
  mongo-data:
```
Como podemos ver hemos realizado cambios en el servicio **app** que vamos a explicar a continuación.

```
build:
    context: .
    dockerfile: Dockerfile.dev
```
1. **context**: indica el contexto de la construcción desde el cual Docker debe tomar los archivos para construir la imagen. En este caso, **.** indica que el contexto es el directorio actual.

2. **dockerfile: Dockerfile.dev**: este parámetro especifica el nombre del archivo Dockerfile que se debe utilizar para construir la imagen. En este caso, utilizimaos el archivo llamado Dockerfile.dev.

```
volumes:
  - .:/app
```
1. **.:/app**: monta el directorio actual del host en el directorio /app dentro del contenedor. En este caso es un volumen (bind mount), útil para el desarrollo porque permite que los cambios en el host se reflejen inmediatamente en el contenedor.

```
command: >
  watchmedo auto-restart --patterns=*.py --recursive -- 
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
En primer lugar **command** especifíca el comando que se ejecutará cuando se inicie el contenedor, además el signo **>** después de **:** indica que habrá un bloque de texto multilínea.

Los comandos que se usan en la primera línea son:

- **watchmedo**: Es una herramienta de línea de comandos proporcionada por el paquete watchdog que se utiliza para monitorear cambios en el sistema de archivos.
- **auto-restart**: Es una subcomando de watchmedo que reinicia automáticamente un comando cuando detecta cambios en los archivos.
- **--patterns=*.py**: Especifica que solo debe monitorear archivos con la extensión .py (archivos Python).
- **--recursive**: Indica que debe monitorear los cambios en los archivos de manera recursiva en todos los subdirectorios.
- **--**: Separa los argumentos de watchmedo de los argumentos del comando que se va a ejecutar.

Los comandos utilizados en la segunda línea:

- **uvicorn**: Es un servidor ASGI para aplicaciones web en Python.
- **main:app**: Especifica el módulo y la aplicación ASGI que uvicorn debe ejecutar. En este caso, main es el nombre del archivo (sin la extensión .py) y app es el nombre de la instancia de la aplicación dentro de ese archivo.
- **--host 0.0.0.0**: Indica que el servidor debe estar disponible en todas las interfaces de red (no solo en localhost).
- **--port 8000**: Especifica el puerto en el que el servidor debe escuchar.
- **--reload**: Activa el modo de recarga automática, lo que significa que uvicorn reiniciará el servidor cada vez que detecte cambios en el código fuente.

### Levantando los contenedores

Antes de levantar los contenedores debemos movernos al directorio donde estén los archivos de esta carpeta.

Luego utlizamos la siguiente línea para levantarlos.

```
docker compose -f docker-compose-dev.yml up -d
```

En este caso la bandera **-f** se utiliza cuando vamos a utilizar un archivo con nombre diferente a **docker-compose.yml**.

Una vez levantados podemos modificar el archivo **main.py** y los cambios se van a ver reflejados en la [https://localhost:8000](https://localhost:8000). 

En este caso podemos agregar un endpoint raíz con el mensaje **Hello World**, el cual está comentado en el código.

```
@app.get('/')
async def read_root():
    return {'message': 'Hello World'}
```
Luego volver al navegador y actualizar la página para ver el cambio en la raíz.