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