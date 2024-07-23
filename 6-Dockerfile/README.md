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
    - ) Paso 3: Copiar archivos al contenedor
    - ) Paso 4: Instalar dependencias
    - ) Paso 5: Exponer el puerto
    - ) Paso 6: Definir el comando de ejecución
