# Conexión de contenedores

En esta unidad realizaremos una conexión entre contenedores y para esto nos basaremos en una base de datos de **MongoDB** y una API relizada con **FastAPI** en Python.

### MongoDB
En este caso vamos a crear una base de datos No-SQL mediante la siguiente línea de comando.

```
docker run -d --name db_mongo -p 27017:27017-e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=1234 mongo
```

Una vez que se ejecute este comando vamos a tener nuestro contenedor llamado **db_mongo** con un user **admin** y una contraseña **1234**

### API 
La API que utilizaremos se encuentra en el archivo **main.py** y contiene 3 endpoints.

- ) El primero nos permite insertar un elemento en la base de datos
- ) El segundo nos permite ver todos los elementos
- ) El tercero nos permite elminar elementos mediante su ID

### Dockerfile para la aplicación
A continuación crearemos un archivo de docker para hacer una imagen de nuestra aplicación y poder utilizarla para crear su contenedor y conectarlo con el contenedor de **MongoDB**.

### Creación de la red
Para que dos contenedores se comuniquen es necesario que se agrupen, para esto hay que crear una red y luego al momento de crear el contenedor con la imagen que queremos le asignamos una red.

Para ver las redes que tenemos debemos utilizar la línea.

```
docker netowrk ls
```
Y como se ve en la siguiente figura tenemos una lista de todas las redes.

![lista de redes](/img/lista%20de%20redes.png)

Ahora para crear una red utilizamos.

```
docker create network mired
```
En este caso el nombre de la red es **mired** y es la que utilizaremos para agrupar los contenedores y como podemos ver en la siguiente imagen luego de crear la red volvemos a ver las redes que tenemos y aparece la nueva red creada.

![lista de redes con mi red](/img/lista%20con%20mired.png)

En el caso de que queramos eliminar la red podemos utilizar la línea.

``` 
docker network rm nombre_de_la_red
```

### Creación de contenedores y asignación de redes

Una vez creada la red debemos volver a crear los contenedores pero asignandole la red que hemos creado para que se comuniquen entre si.

Por lo que para la base de datos de mongo el comando.

```
docker create -p 27017:27017 --name db_mongo -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=1234 --network mired mongo
```
Una vez creado el contenedor lo iniciamos.

```
docker start db_mongo
```

Ahora creamos el contenedor de la API.

```
docker create -p 8000:8000 --name app --network mired app
```
Iniciamos el contenedor

```
docker start app
```
Una vez que tenemos ambos contenedores iniciados podemos ir a nuestro navegador e utilizar la dirección [localhost:8000/docs](https://localhost:8000/docs) para acceder a swagger y poder utilizar la API.

Lo que veremos será como la siguiente imagen y tendremos todos los endpoints para utilizar cada uno y ver si estos insertan, muestra y borran datos de la base de datos.

![docs](/img/docs.png)

Aquí insertaremos un elemento en la base de datos con nombre **Juan** y edad **23** como se muestra en la siguiente figura.

![ep de insertar](/img/ep%20de%20insertar.png)

Luego insertaremos otro con nombre **Pedro** y edad **32** de la misma manera.

Ahora veremos todos los elementos que hemos insertado en el endpoint correspondiente como se ve en la siguiente imagen.

![ep de mostrar](/img/ep%20de%20mostrar.png)

Ahora para eliminar un elemento en particular lo haremos con el endpoint correspondiente mediante el id como se ven el la siguiente imagen.

![elimino elemento](/img/elimino%20elemento.png)

Y como vemos el elemento fue elimnado

![elemento eliminado](/img/elemento%20eliminado.png)