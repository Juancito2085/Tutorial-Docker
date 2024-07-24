# Dockerfile

Si quisieramos cear una imagen de nuestra aplicación u otra aplicación, tendríamos que definir varios parámetros y escribir muchas líneas y ejecutar de una en una. Y si hubiera una manera de crear un archivo con todas las instrucciones y solo ejecutarlo?

### Qué es un Dockerfile?

Es un archivo de texto que contiene instrucciones para construir una imagen de Docker. Define los pasos necesarios para crear una imagen que luego puede ser usada para ejecutar contenedores. Un Dockerfile especifica la imagen base, los archivos que se deben copiar al contenedor, los comandos que se deben ejecutar durante la construcción de la imagen, y otros parámetros.

### Tu primer Dockerfile

Vamos a aprender a construir un Dockerfile con un ejemplo muy sencillo, vamos a utilizar una API con dos endpoints, el primero será el **root** que mostrará un *Hola mundo!* y el otro **número** el cuál devolverá un número aleatorio entre 0 y 100.

1 ) Crear un requierments.txt: debemos crear este archivo donde se guardarán las dependencias necesarias para poder ejecutar esta aplicación.

2 ) Crear un archivo **Dockerfile**: necesitamos este archivo precisamente con este nombre para crear la imagen.

3 ) Instrucciones: vamos a definir los pasos a continuación en forma de pseudocódigo

    - ) Paso 1: Imagen base
    - ) Paso 2: Establecer el directorio de trabajo
    - ) Paso 3: Copiar los archivos de requisitos
    - ) Paso 4: Instalar dependencias
    - ) Paso 5: Copiar el código de la aplicación
    - ) Paso 6: Exponer los puertos
    - ) Paso 7: Comando para ejecutar la aplicación

### Dockerfile ejemplo

En este ejemplo vamos a construir un **Dockerfile** con una API muy sencilla cuyo codigo se encuentra en el archivo **main.py**. A continuación vamos a explicar cada línea del archivo de docker basandonos en los pasos anteriores para que se pueda entender mejor.

#### Imagen base
Cuando creamos una imagen, debemos especificar en base a que imagen de Docker lo vamos a hacer. En este caso lo haremos en base a la imagen de **Python** y en particular de la versióno 3.9.

Esta es la primer línea de nuestro archivo donde se especifíca dicha imagen.
```
FROM python:3.9
```
#### Establecer el directorio de trabajo

Para establecer el directorio de trabajo dentro del contenedor se utiliza la siguiente línea.

```
WORKDIR /app
```
Este directorio se convierte en el directorio actual para cualquier instrucción RUN, CMD, ENTRYPOINT, COPY, y ADD que siga en el Dockerfile. Es similar a usar el comando cd en una terminal para cambiar el directorio actual.

#### Copiar los archivos de requisitos
Debemos indicar las dependecias necesarias para que la aplicación funcione adecuadamente y esto en python se hace mediante el archivo *requirements.txt*, por lo que debemos copiarlo con la siguiente linea,

```
COPY requirements.txt .
```
Luego del comando **COPY** van 2 argumentos, el primero sería el archivo  que vamos a copiar y el segundo es un **.** este indica el destino y en este caso como en nuestra consola estamos en esa carpeta solo con poner el punto estamos indicando que es el direcotiro actual.

#### Instalar las dependencias del proyecto
Para instalar las dependencias se utiliza el comando **RUN** seguido de las instrucciones que se quieren ejecutar, esto es algo muy similar a lo que uno hace en la consola de *Visual Studio Code* al instalar alguna librería en Python.

```
RUN pip install --no-cache-dir -r requirements.txt
```
#### Copiar el resto del código de la aplicación al directorio de trabajo
Ahora debemos copiar los todos los archivos de la aplicación, en este caso es solo uno. Yesto se realiza con la siguiente línea de comando
```
COPY . .
```
Luego del comando **COPY** se indican el directorio origen (de donde voy a copiar, en terminos simples el destino de tu máquina local) y el directorio destino (que seria el directorio dentro del contenedor, en este caso el definido previamente por WORKDIR).

Vemos como los 2 destinos están representados con **.** ya que indican el actual directorio donde se esta trabajando en el primer caso y WORKDIR en el segundo.

#### Exponer el puerto en el que la aplicación estará escuchando
También necesitamos indicar que puerto vamos a exponer para que cuando se cree el contenedor en base a esta imagen no haga falta hacerlo. En nuestro caso vamos a exponer el puerto 8000 con la siguiente línea.
```
EXPOSE 8000
```
#### Comando para ejecutar la aplicación usando uvicorn
Para ejecutar la aplicación debemos utilizar el comando CMD que se ejecuta cuando se crea el contenedor a partir de la imagen que vamos a crear.
En este caso le pasamos una lista con los comandos y los argumentos siguientes:
- ) uvicorn: Es el comando que se ejecutará.
- ) main:app: Especifica el módulo y la aplicación que uvicorn debe ejecutar.
- ) --host 0.0.0.0: Indica que la aplicación debe estar disponible en todas las interfaces de red del contenedor.
```
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```