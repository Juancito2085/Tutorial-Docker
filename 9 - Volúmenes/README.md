# Volúmenes

Cuando trabajamos con contenedores y los eliminamos también se eliminan los datos almacenados en ellos. 

Como los contenedores tienen su propio sistema de archivos, ahí es donde va a estar almacenada toda la información. Si quisieramos que esta última persista luego de borrar los contenedores entonces usaríamos la herramienta **volumes**.
 
Con **volumes** se montaría la carpeta dentro del sistema operativo anfitrión y no dentro del container como se puede ver en la Figura 1.

![docker volumes](/img/docker%20volumes.png)

Figura 1. Esquema de sistema de archivos de contenedores y volúmenes.
 
### Tipos de volúmenes

1. Anónimo: estos volúmenes se crean sin un nombre específico y se utilizan principalmente cuando se necesita un almacenamiento temporal. Se eliminan automáticamente cuando el contenedor que los utiliza se elimina.

2. Nombrado: estos volúmenes tienen un nombre definido por el usuario, lo que facilita su identificación y gestión. Son útiles cuando necesitas compartir datos entre varios contenedores o cuando necesitas que los datos persistan más allá del ciclo de vida de un contenedor.

3. Anfitrión (bind mounts): a diferencia de los volúmenes, los bind mounts montan un directorio o archivo específico del sistema de archivos del host en un contenedor. Esto es útil cuando necesitamos acceso directo a archivos específicos del host, pero puede ser menos portátil que los volúmenes.

4. Tmpfs Mounts: Estos montajes almacenan datos en la memoria del host y no en el disco. Son útiles para datos temporales que no necesitan persistir después de que el contenedor se detenga.


### Volúmenes en Docker Compose
```
version: "3.9"
services:
  app:
    build: .
    ports:
      - "8000:8000"
    links:
      - db_mongo
  db_mongo:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=1234
    volumes:
        mongo_data:/data/db
volumes:
    mongo-data:
```

Con el mismo código de la Unidad anterior vamos a realizar modificaciones como se ve más arriba.

1. Definimos el volumen en **volumes** al final de todo donde le damos un nombre al volumen que vamos a utilizar en nuestro caso **mongo-data**.

2. Luego en el servicio **db-mongo** vamos a especificar el volumen que vamos a utilizar el cual lo definimos anteriormente.

3. Agregamos la ruta dentro del contenedor donde se montara el volumen **mongo-data** en este caso el directorio por defecto donde se guarda la informacion de de **MongoDB**.

### Sintaxis de los diferentes tipos de volúmenes

- **Volumen con nombre**: `mongo_data:/data/db`
  - Se crea y gestiona por Docker y se puede reutilizar entre diferentes contenedores.

- **Volumen anónimo**: `/data/db`
  - Se crea automáticamente y no tiene un nombre específico. No se reutiliza entre contenedores.

- **Bind mount**: `./data:/data/db`
  - Mapea un directorio del host a un directorio del contenedor. Útil para desarrollo.

### Persistencia de los datos

Ahora con el **docker-compose.yaml** que se encuentra en esta unidad vamos a levantar los contenedores cargar un elemento y bajar los contenedores para verificar que no se haya eliminado la información.

Con el siguiente comando levantamos los contenedores.

```
docker compose up -d
```

Vamos a insertar un elemento como se ve en la Figura 2.

![volumen insertar item](/img/volumen%20item%20creado.png)

Figura 2. Elemento insertado en la base de datos MongoDB.

Luego detenemos y eliminamos los contenedores mediante la siguiente línea de comando.

```
docker compose down
```
Esto lo podemos ver en la Figura 3.

![volumenes items](/img/volumenes%20docker%20compose%20down.png)
Figura 3. Contenedores detenidos y eliminados.

Con esto si no tendríamos configurado los volúmenes la información se habría perdido al eliminarse los contenedores. 

Pero ahora vamos a volver a levantar los contenedores como lo hemos hecho antes.

```
docker compose up -d
```

Y vamos a verificar que esté el item que habíamos creado anteriormente.

![volumenes post bajada](/img/volumenes%20post%20bajada.png)
Figura 4. Elementos de la base de datos.

Y como vemos en la Figura 4, el item que habíamos creado no se eliminó al eliminar los contenedores anteriormente.
