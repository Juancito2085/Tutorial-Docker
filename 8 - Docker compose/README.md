# Docker Compose

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker de múltiples contenedores. Con Docker Compose, podemos usar un archivo **.yaml** o **.yml** para configurar los servicios de una aplicación. Luego, con un solo comando, podemos crear e iniciar todos los servicios desde nuestra configuración.

En pocas palabras todo lo que hemos hecho en la unidad anterior lo podemos incorporar a un archivo YAML y al ejecutarlo se ejecutará todo el proceso de una vez.

Las características principales son:
1. Definición de servicios: Podemos definir todos los servicios que componen una aplicación en un solo archivo docker-compose.yml.
2. Redes y volúmenes: Podemos configurar redes y volúmenes compartidos entre contenedores.
3. Escalabilidad: Podemos escalar servicios hacia arriba o hacia abajo con un solo comando. Esto quiere decir que podemos aumentar o disminuir el número de instancias.

Veremos esto con el mismo ejemplo de la unidad anterior, es decir que crearemos un docker-compose.yaml que nos permite crear los 2 contenedores que habíamos creado, pero todas las instrucciones que utilizamos estarán en un solo archivo.

### docker-compose.yaml

A continuación presentaremos el codigo del archivo en si.
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
```

En primer lugar tenemos:

1. **version**:
    - Aquí se especifíca la versión del formato del archivo Docker Compose que se esta utilizando. Esto es de suma importancia porque diferentes versiones de Docker Compose pueden tener diferentes características y sintaxis.

2. **services:**

    - Define los servicios que componen tu aplicación. En este caso, hay dos servicios: app y db_mongo.

3. **app:**

    - **build: .**
        - Indica que Docker debe construir la imagen del servicio app usando el Dockerfile en el directorio actual.
    - **ports:**
        - "8000:8000": Mapea el puerto 8000 del contenedor al puerto 8000 de la máquina host. Esto permite acceder al servicio app desde el host a través del puerto 8000.
    - **links:**
        -db_mongo: Establece una conexión entre el servicio app y el servicio db_mongo. Esto permite que el servicio app se comunique con db_mongo usando el nombre del servicio como hostname.
4. **db_mongo:**

    - **image: mongo**
        - Especifica que Docker debe usar la imagen oficial de MongoDB para este servicio.
    - **ports:**
        - **"27017:27017"**: Mapea el puerto 27017 del contenedor al puerto 27017 de la máquina host. Esto permite acceder a MongoDB desde el host a través del puerto 27017.
    - **environment:**
        - MONGO_INITDB_ROOT_USERNAME=admin: Establece el nombre de usuario del administrador de la base de datos MongoDB.
        - MONGO_INITDB_ROOT_PASSWORD=1234: Establece la contraseña del administrador de la base de datos MongoDB.

Es **muy importante** que respetemos la sintaxis del código escrito más arriba, es decir, las identaciones, las dobles comillas, los guiones, etc.

Una vez que tengamos el Docker Compose y el Dockerfile en la misma carpeta con todos los archivos necesarios de la API podemos utilizar el siguiente comando.

```
docker compose up -d
```
Una vez que corramos este comando se va a realizar todo el proceso que hemos hecho anteriormente y todo esto mediante las instrucciones del archivo **docker-compose.yaml**.