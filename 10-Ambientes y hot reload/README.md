# Ambientes y Hot Reload

En primer lugar vamos a crear un nuevo archivo **Dockerfile.dev** que lo utilizaremos para desarrollo.

Pero para detectar los cambios que hagamos en nuestra aplicación vamos a tener que utilizar una herramienta que nos permita hacer **hot reload** que puede ser **watchdog** o ** python-devtools**.

En este caso haremos un ejemplo con **watchdog** y veremos los cambios que le haremos al **Dockerfile.dev**

### Configuración Dockerfile.dev
```
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Instala watchdog
RUN pip install watchdog

# Copia el contenido del directorio actual en /app
COPY . .

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación con watchmedo
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "python", "app.py"]

```
Como podemos ver en el codigo de arriba se han realizado algunos cambios que vamos a explicar a continuación.

```
RUN pip install watchdog
```
Este primer cambio instala la biblioteca **watchdog** que se necesita para detectar cambios en los archivos y reiniciar la aplicación automaticamente.

```
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "python", "app.py"]
```
En este segundo cambio se configura el contenedor  para que use **watchmedo**, una herramienta proporcionada por **watchdog** para monitorear archivos **.py** en el directorio de trabajo **/app**. Cuando se detecta un cambio en alguno de los archivos, **watchmedo** reinicia automaticamente la aplicacion ejecutando **python app.py**.

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
      - .:/home/app
  db_mongo:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=1234
    volumes:
      - mongo-data:/data/db
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
  - .:/home/app
```
1. **.:/app**: monta el directorio actual del host en el directorio /app dentro del contenedor. En este caso es un volumen (bind mount), útil para el desarrollo porque permite que los cambios en el host se reflejen inmediatamente en el contenedor.