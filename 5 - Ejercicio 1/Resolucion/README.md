# Resolución

Si bien la resolución se puede realizar de varias maneras, acá indicaremos la reolución más larga y extensa para poder aplicar todo lo aprendido hasta este punto.

1 ) Descargar la imagen de **MYSQL**: lo primero que deberíamos hacer es descargar la imagen para poder crear un contenedor y así ejecutarlo. En este caso es muy fácil ingresar a [Docker Hub](https://hub.docker.com/) y buscar la imagen que estamos buscando para poder comenzar. No debemos olvidarnos que además de obtener el comando para descargar la imagen también esta toda la información necesaria para utilizar la misma.

La primera línea de comando a utilizar sería:

```
docker pull mysql
```
Al no incluir ningún tag estaríamos descargando la última versión de la imagen.

2 ) Crear el contenedor: ahora una vez que descargamos la imagen vamos a proceder a crear el contenedor, mapear los puertos para poder acceder desde afuera del contenedor y además configurar las variables de entorno para configurar la imagen. Todo esto lo hacemos con la siguiente línea.

```
docker create --name db -p3307:3306 -e MYSQL_ROOT_PASSWORD=1234 mysql
```

Con esa línea hemos creado un contendedor llamado **db**, hemos mapeado el puerto 3307 de nuestro ordenador al puerto por defecto 3306 de **MYSQL** y además hemos configurado el password de root a **1234**.

3 ) Correr el contenedor: ya creado el contenedor podemos correrlo con el comando.

```
docker start db
```

4 ) Verificar el contenedor: ahora como buena práctica lo mejor es corroborar que el contenedor este levantado con el siguiente comando.

```
docker ps 
```

Y así verificamos que el contenedor este levantado en la columna status con la frase **up X minutes ago**.

5 ) Realizar el script o notebook: ahora solo queda crear el scrip o notebook de Python para poder realizar la otra parte del ejercicio. Los detalles se encuentran en archivo llamado **resolucion.ipynb**.