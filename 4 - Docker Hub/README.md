# Docker Hub
En esta sección se verán las características principales de Docker Hub.

![docker hub](/img/dockerhub.png)

### Qué es Docker Hub?

[Docker Hub](https://hub.docker.com/) es el repositorio de imágenes para contenedores más grande del sector IT. En él, se puede encontrar una amplia variedad de imágenes oficiales proporcionadas directamente por la plataforma de Docker. Además, Docker Hub permite acceder a imágenes de proveedores externos y contribuye a la creación automática de imágenes desde plataformas como GitHub y Bitbucket.

### Imágenes

En la página oficial poniendo el nombre de la aplicación que qerramos buscar podemos obtener informacion de las imagenes que hay disponibles. 

En este caso buscaremos *mongo*.

![img mongo](/img/img%20docker%20hub.png)
Figura 1. Página de Docker Hub.

Una vez que elijamos **mongo** podemos ver:

1 ) El comando para descargar la imagen de mongo.

2 ) Tenemos una pestaña de tags donde podemos ver las diferentes versiones.

3 ) También vamos a encontrar información de como utilizar la imagen, como por ejemplo: conexión con otros contenedores, configuración de variables de entorno, utilizar archivos de configuración, etc

### Variables de entorno
Para el caso de **MongoDB** tenemos estas 2 variables de entorno que nos permiten configurar el usuario y el password.

```
-e MONGO_INITDB_ROOT_USERNAME=mongoadmin 
-e MONGO_INITDB_ROOT_PASSWORD=secret
```
En nuestro caso y como ejemplo para crear un contenedor podemos ejecutar la siguiente línea.

```
docker create -p27017:27017 --name monguito -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=user1234 mongo 

```
Si bien esta sección es corta y muy resumida la idea es que cada vez que utilices una imagen puedas recurrir a **Docker Hub** para ver todo lo referente a su configuración.