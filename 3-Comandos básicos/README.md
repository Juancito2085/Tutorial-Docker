# Comandos básicos

A continuación veremos los comandos básicos de Docker para imágenes y contenedores

### Imágenes

El primer comando y por demás de intuitivo es el que nos permite ver todas las imagenes que estan almacenadas en local y no solo de la carpeta donde estemos trabajando.

```
docker images
```
Como podemos ver en la siguiente imagen, solo contamos con la imagen *hello-world* que descargamos para ver si el servicio de Docker funcionaba correctamente luego de instalarlo.

![docker-images](/img/docker-images.png)

Ahora si queremos descargar una imagen utilizamos el siguiente comando.

```
docker pull nombre_de_la_imagen
```

Las cuales estan alojadas en [Docker Hub](https://hub.docker.com/), que es un servicio de registro de contenedores proporcionado por Docker. Este lugar de almacenamiento de las imagenes sera explicado en ls siguiente unidad.

Si solo utilizamos el nombre el nombre de la imagen, Docker descargará la imagen con el tag **latest**, es decir la última versión.

En el siguiente ejemplo que se ven en la imagen, se descarga la imagen de mysql y como se puede ver al no especificar la versión, descarga por defecto la que tiene el tag de *latest*. Además se aprecia como Docker descarga las capas de esta imagen, es importante destacar que si descargamos otra imagen que use las capas de alguna que descargamos Docker **no** vovlerá a descargar estas capas y de esa manera maximiza el almacenamiento.

![docker-pull-mysql](/img/docker-pull-mysql.png)

Si ahora volvemos a ejecutar el comando.

```
docker images
```
Podemos ver todas las imagenes que tenemos en local donde los nombres de las columnas indican:
- ) REPOSITORY: es el nombre de la imagen.
- ) TAG: indica la etiqueta de la imagen
- ) IMAGE ID: es un identificador unico.
- ) CREATED: fecha de la creación de la imagen.
- ) SIZE: es el tamaño de la imagen.

![imagenes en local](/img/imagenes-en-local.png)

Ahora vamos a descar la version 8.4 de *MYSQL* con el siguiente comando 

```
docker pull mysql:8.4
```
Donde luego del nombre de la imagen se separa el *tag* o la versión con **:**.

Como se ve en la siguiente imagen ahora descarga las capas de la versión especificada en el comando aterior.

![docker-mysql-84](/img/docker-mysql84.png)

Si volvemos a ver las imagenes con el comando.

```
docker images
```

Ahora tendremos los siguiente en nuestra PC.

![docker 3 imagenes](/img/docker%20con%203%20imagenes.png)

Donde se aprecia que cambió la etiqueta a pesar de tener el mismo nombre de imagen y es importante ver como cambio el identificador único de la imagen. Si hubieramos descargado la ultima versión con el tag correspondiente tendrian el mismo identificador unico. Ya que la última imagen se va a descargar sin especificar la versión o al especificar esta versión luego de **:**.

Ahora vamos a eliminar las imagenes con la siguiente línea.

```
docker image rm nombre_de_la_imgen:tag
```
Para nuestro caso vamos a proceder a borrar la imagen de *MYSQL* con la version 8.4, por lo que ejecutaremos el siguiente comando

```
docker image rm mysql:8.4
```
Y como se puede ver en la siguiente figura se elimina la imagen deseada.

![elimino mysql84](/img/elimino%20mysql84.png)

Ahora al ejecutar.

```
docker images
```
![iamgenes posteliminacion](/img/imagenes%20posteliminacion.png)

Como se puede ver arriba, no aparece la imagen de *MYSQL* que corresponde a la versión 8.4.

Ahora vamos a eliminar la otra imagen de *MYSQL* con la siguiente línea.

```
docker image rm mysql
```
Luego volvemos a ejecutar

```
docker images
```
Y vemos en la siguiente imagen como solo nos quedó la imagen *hello-world*.

![solo queda hello world](/img/todo%20eliminado%20menos%20hw.png)

### Contenedores

Para crear un contenedor vamos a necesitar una imagen y además setear las variables de configuración.

En este caso vamos a descargar la imagen de **MongoDB** con la siguiente línea.

```
docker pull mongo
```
![mogno descargado](/img/mongo%20descargado.png)
 
Una vez descargada la imagen vamos a crear un contenedor con la siguiente línea.

```
docker create nombre_de_la_imagen
```

Que en nuestro caso sería.

```
docker create mongo
```
![contenedor creado](/img/contenedor%20mongo.png)

Como se puede ver en la imagen docker nos devuelve el identificador del contenedor, el cual nos sirve para ejecutar el contenedor.

![id contenedor mogno](/img/ver%20id%20mongo%20contenedor.png)

Si quisieramos crear un contenedor con una línea mas verbosa deberíamos utilizar.

```
docker container create mongo
```

Para poder ejecutar el contenedor debemos usar la siguiente línea.

```
docker start id_contenedor
```

![docker start](/img/start%20mongo.png)

Para verificar que el contenedor está corriendo utilizamos la siguiente línea.

```
docker ps
```
![docker ps mongo](/img/dockerps%20mongo.png)

En la siguiente figura podemos ver:
- ) CONTAINER ID: el identificador del contenedor, pero este es más corto y solo con este también podemos ejecutar el contenedor
- ) IMAGE: indica en base a que imagen se ha creado el contenedor
- ) COMMAND: indica el comando que utiliza el contenedor para ejecutarse
- ) CREATE: indica hace cuanto fue creado el contenedor
- ) STATUS: indica el estado del contenedor
- ) PORTS: indica el puerto que utiliza
- ) NAME: es el nombre del contenedor

Ahora para detenerlo vamos a utilizar la siguiente linea y en este caso vamos a utilizar el identificador del container obtenido recién.

```
docker stop container_id
```
Una vez detenido nuestro container verificamos que es lo que sucede si utilizamos la línea.

```
docker ps
```

Como se puede ver en la imagen, no aparece nada. Por lo que ahora vamos a utilizar la misma linea pero agregando lo siguiente.

![docker stop mongo](/img/docker%20stop%20mongo.png)

```
docker ps -a
```
![docker ps -a con mongo](/img/docker%20ps-a%20con%20mongo.png)

Con esto vamos a poder ver todos los contenedores y no solo los que están detenidos.

Ahora para eliminarlo vamos a utilizar la siguiente línea.

``` 
docker rm nombre_del_contenedor
```
![docker remove mongo](/img/mongo%20removido.png)
Y ahora verificamos que lo hemos eliminado con la línea.

```
docker ps -a
```
![verificacion de mongo removido](/img/verificacion%20de%20mongo%20removido.png)

Ahora si queremos crear un contenedor y asignarle un nombre utilizaremos los siguiente comandos.

```
docker create --name nombre_del_contenedor imagen
```

Vamos a crear un contenedor con el nombre **monguito** con la siguiente línea de comando.

```
docker create --name mongo monguito
```
![monguito creado](/img/moguito%20creado.png)

Ahora para iniciar el contenedor vamos a utilizar el nombre que le dimos, que en este caso es el mismo que el de la imagen de la siguiente manera.

```
docker start monguito
```

Ahora verificamos si esta corriendo mediante la línea.

```
docker ps
```
![monguito contenedor](/img/moguito%20contenedor.png)

Como vemos en la imagen el contenedor esta corriendo, pero si quisieramos utilizar esta base de datos no podríamos acceder ya que el puerto del contenedor no está mapeado con ningún puerto de nuestra PC (si estuviaramos trabajando con un servidor sería el puerto del servidor), por lo que no se podría acceder de manera externa.

### Puertos

Como ya dijimos antes para que se pueda utilizar algún contenedor mediante una conexión que recibe el servidor, se debe hacer un mapeo entre la mánquina (PC o servidor) y el contenedor.

![port mapping](/img//port%20%20mapping.jfif)

Como se puede ver en la imagen de arriba, vemos dos peticiones. Una petición en el puerto 8080 y otro en el 8090, estos estan mapeado al puerto interno 80 de cada servicio.

Donde la primera petición se dirige al servicio **A** y la segunda al servcio **B**.

Este mapeo de puertos permite que el tráfico de la red desde fuera del host se enrute a procesos específicos que se ejecuten en contenedores dentro del **host**(servidor).

Vamos a borrar ahora nuestro contenedor para hacer un mapeo de muerto. 

Primero detenemos el contenedor y luego lo eliminamos
```
docker stop monguito
docker rm monguito
```

Ahora para crear un nuevo contenedor y mapear sus puertos utilizamos la siguiente línea.

```
docker create -p'puerto_host':'puerto_contenedor' --name nombre_contenedor nombre_imagen
```
Para  nuestro caso utilizamos los siguiente parámetros.

```
docker create -p27017:27017 --name monguito mongo
```
Ahora inicimamos el contenedor y verificamos que el container este creado.

```
docker start monguito
docker ps
```

![monguito con puertos](/img/monguito%20con%20puertos.png)


### Logs

Para saber si nuestro servidor de mongo se ejecuto de manera correcta podemos usar.

```
docker logs id_container
```

También se puede utilizar 

```
docker logs nombre_container
```
Como podemos ver en la imagen se ven todos los logs pero nos devuelve a la consola. Para quedarnos "escuchando" y poder ver los logs podemos utilizar la siguiente línea.

![logs de monguito](/img/logs%20de%20monguito.png)

```
docker logs --follow monguito
```
Para volver a la línea de comando presionamos **Ctrl+c**.

### docker run

Ahora veremos una manera rápida y sencilla que simplifica todos los pasos anteriores. 

Si quisieros descargar la imagen, crear un contenedor e inciar el contendor con mongo solo deberíamos ejecutar lo siguiente.

```
docker run mongo
```
Con esto:

1 ) Docker busca la imagen de manera local y si no la encuentra la descarga.

2 ) Crea el contenedor

3 ) Ejecuta el contenedor

Como vemos seguimos teniendo los logs y para salir hay que presionar **Ctrl+c**. Pero si quisieramos correr el contenedor y no ver los logs para que nos devuelva a la línea de comando deberíamos ejecutar el siguiente comando.

```
docker run -d nombre_contenedor
```
Es importante destacar que todas las opciones que se vieron con **docker create** tambien se pueden aplicar a **docker run**.

Ahora vamos a detener y elimnar el contenedor con el id del contenedor

```
docker stop
docker rm 
```

Y vamos a utilizar la siguiente línea.

```
docker run --name monguito -p27017:27017 -d mongo 
```
Como vemos al ejecutar.

```
docker ps
```
![monguito con run y puertos](/img/monguito%20con%20run%20y%20puertos.png)

Es para destacar que al ejecutar **docker run** vamos a tener tantos contenedores como veces se ejecuto este comando.

